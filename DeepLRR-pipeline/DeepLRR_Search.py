# encoding: utf-8
"""
@author: ZiRui Ren
@contact: 1131061444@qq.com/renzirui@webmail.hzau.edu.cn
@time: 2021/6/1 20:36
@file: DeepLRR_Search.py
@desc: 
"""

import os
import getopt
import subprocess
import sys



def env_check():
    checked = True
    check_pfam = 'which pfam_scan.pl'
    back = subprocess.Popen(check_pfam, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if back[0].decode() == '':
        print('[ERROR] PfamScan not found, Please install it before LRR_Search, or check if its path has been add to $PATH!')
        checked = False
    check_sp = 'which signalp'
    back = subprocess.Popen(check_sp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if back[0].decode() == '':
        print('[ERROR] SignalP not found, Please install it before LRR_Search, or check if its path has been add to $PATH!')
        checked = False
    check_tm = 'which tmhmm'
    back = subprocess.Popen(check_tm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if back[0].decode() == '':
        print('[ERROR] TMHMM not found, Please install it before LRR_Search, or check if its path has been add to $PATH!')
        checked = False
    check_hmmscan = 'which hmmscan'
    back = subprocess.Popen(check_tm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if back[0].decode() == '':
        print('[ERROR] HMMER not found, Please install it before LRR_Search, or check if its path has been add to $PATH!')
        checked = False
    check_coils = 'which coils'
    back = subprocess.Popen(check_tm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if back[0].decode() == '':
        print('[ERROR] COILS not found, Please install it before LRR_Search, or check if its path has been add to $PATH!')
        checked = False
    check_coilsdir = 'echo $COILSDIR'
    coilsdir_back = subprocess.Popen(check_coilsdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    #print(coilsdir_back[0].decode())
    if coilsdir_back[0].decode() == '':
        print('[ERROR] environment variable $COILSDIR not found, please add COILS path to $PATH!')
        checked = False
    try:
        import torch
    except ModuleNotFoundError:
        print('[ERROR] Pytorch have not installed yet, please install pytorch!')
        checked = False
    return checked


def usage():
    print('DeepLRR_Search is an integrated tool for LRR domain searching.\n' +
          'Usages: python DeepLRR_Search.py -f <input_file> -o <output_file> -d [domain_type] -m [model_name] [-a|h|e] <Lscp> <Ldcp> <Lncp>\n' +
          '  -d [domain type]\t: the LRR domain you want to search [ NBS_LRR | LRR_RLK | LRR_RLP | LRR ]   *choose [LRR] will only run DeepLRR instead of the pipeline\n' +
          '  -f <input_file>\t: assign input file\n' +
          '  -o <output_file>\t: assign output file\n' +
          '  -m [model_name]\t: assign version of DeepLRR model, \'model-1.01\' is set for default\n'+
          '  -a --atypical\t\t: search for atypical domain, have to assign domain type at the same time, when choosing [LRR] domain, this input will be ignored\n' +
          '  -h --help\t\t: look for usages \n'+
          '  <Lscp> <Ldcp> <Lncp>\t: assign parameter of DeepLRR Search\n'+
          '  -e --envcheck\t\t: check environment dependenties\n'
          )
    quit()


def input_check(input_filename, output_filename, category, model_name):
    if not os.path.isfile(input_filename) and os.path.isdir(input_filename):
        print('\n[ERROR] Input file is a directory, not a file!')
        quit()
    if not os.path.exists(input_filename):
        print('\n[ERROR] Input file not exist!')
        quit()
    if os.path.isdir(output_filename):
        print('[ERROR] Output file cannot be a directory!')
        quit()
    if os.path.exists(output_filename):
        print('\n[WARNING] Output file has already exist! Going on will cover the former file.')
        while True:
            override = input('Override[y/n]:')
            if override == 'y':
                print('Forced override confirmed!')
                os.system('rm '+output_filename)
                break
            elif override == 'n':
                print('Session Terminated! Check your input and retry!')
                quit()
            else:
                print('[ERROR] Please input \'y\' or \'n\' and press ENTER!')
                continue
    path = '/'.join(output_filename.split('/')[:-1])
    # print(path)
    if path == '':
        path = './'
    # print(path)
    if not os.path.exists(path):
        print('\n[ERROR] Output directory not exist!')
        quit()
    if not (category == 'NBS_LRR' or category == 'LRR_RLK' or category == 'LRR_RLP' or category == 'LRR' ) :
        print('\n[ERROR] Illegal protein type!\nAvailiable input: NBS_LRR | LRR_RLK | LRR_RLP | LRR ')
        quit()
    if not model_name == 'model-1.01':
        print('\n[ERROR] Model name not exist!')
        quit()


if __name__ == '__main__':
    try:
        options, args = getopt.getopt(sys.argv[1:], "ehd:af:o:m:", ['envcheck', 'help', 'domain=', 'atypical', 'fasta=', 'output=', 'model='])
        if len(options)==0:
            usage()
            quit()
        for name, value in options:
            if name in ('-e', '--envcheck'):
                checked = env_check()
                if checked:
                    print('Environment check PASS!')
                quit()
            if name in ('-h', '--help'):
                usage()
            if name in ('-o', '--output'):
                output_file = value
            if name in ('-a', '--atypical'):
                atypical = True
            else:
                atypical = False
            if name in ('-d', '--domain'):
                domain = value
            if name in ('-f', '--fasta'):
                input_file = value
            if name in ('-m', '--model'):
                model_name = value
        # print(args)
        warn1,warn2 = False, False
        default_param = True
        model_name = 'model-1.01'
        p1,p2,p3='4','9','3'
        if len(args)==3 and domain == 'LRR':
            p1,p2,p3 = args[0], args[1], args[2]
            default_param = False
        if len(args)==3 and domain != 'LRR':
            warn1=True
        if atypical and domain == 'LRR':
            warn2=True
            atypical=False
    except getopt.GetoptError:
        usage()

    checked = env_check()
    if not checked:
        print('Session Terminated! Prerequisite unsatisified! Check your environment!')


    #    input_check(input_file, output_file, domain, model_name)

    print('#####\tDeepLRR_Search v1.01 by Zhenya Liu & Zirui Ren\t#####')
    print('---------SEARCH CONFIGURATION---------')
    print('## Input File:\t\t'+input_file)
    print('## Output File:\t\t'+output_file)
    print('## Domain Type:\t\t'+domain)
    print('## Atypical Search:\t'+str(atypical))
    print('## Model Name:\t\t'+model_name)
    if default_param:
        print('## Lscp:\t\t'+str(p1)+'(default)')
        print('## Ldcp:\t\t'+str(p2)+'(default)')
        print('## Lncp:\t\t'+str(p3)+'(default)')
    else:
        print('## Lscp:\t\t'+str(p1))
        print('## Ldcp:\t\t'+str(p2))
        print('## Lncp:\t\t'+str(p3))

    print('=======================================')
    if warn1:
        print('\n[WARNING] Parameter setting only in [LRR] domain searching! Input will be partly omitted!')
    input_check(input_file, output_file, domain, model_name)
    if warn2:
        print('\n[WARNING] When choose [LRR] search, atypical search is unavailiable, input \'-a\' omitted!')
    print('\n<---DETAIL INFO--->')
    if atypical:
        cmd_atypical = 'python scripts/atypical.py '+input_file+' '+output_file+' '+domain
        os.system(cmd_atypical)
    if not atypical:
        if domain == 'NBS_LRR':
            cmd_typical = 'python scripts/NBS_LRR.py '+input_file+' '+output_file+' '+model_name
            os.system(cmd_typical) 
        elif domain == 'LRR_RLK':
            cmd_typical = 'python scripts/LRR_RLP_RLK.py -k '+input_file+' '+output_file+' '+model_name
            os.system(cmd_typical)
        elif domain == 'LRR_RLP':
            cmd_typical = 'python scripts/LRR_RLP_RLK.py '+input_file+' '+output_file+' '+model_name
            os.system(cmd_typical)
        elif domain == 'LRR':
            print('>>Running DeepLRR...')
            cmd_typical = 'python scripts/DeepLRR-1.01/DeepLRR.py '+input_file+' '+p1+' '+p2+' '+p3+' scripts/DeepLRR-1.01 '+model_name
            os.system(cmd_typical)
            filename ='.'.join(input_file.split('/')[-1].split('.')[0:-1])
            # print(filename)
            print('>>DeepLRR Completed!')
            os.system('mv scripts/DeepLRR-1.01/outcome/'+filename+'_predict2.txt '+output_file)
            print('Completed! Result has been written to > '+output_file)
