#!/usr/bin python
"""
@author: ZiRui Ren
@contact: 1131061444@qq.com/renzirui@webmail.hzau.edu.cn
@time: 2020/12/9 15:00
@file: NBS_LRRv1.py
@desc: 
"""
import os
import sys
import pipeline
import getopt
from random import randint


opts, args = getopt.getopt(sys.argv[1:], '-h', ["help"])
for opt_name, opt_value in opts:
    if opt_name in ('-h', '--help'):
        print('DeepLRR Pipeline (NBS-LRR) v1.0beta by ZiRui Ren\n'
              '  Usage:\n'
              '\tpython NBS_LRR.py <inputfile> <outputfile>\n\n'
              '  <-h> or <--help> if need help'
              )
        exit()
if len(args) < 3:
    print("ERROR! lack of argument!")
    print(args)
if len(args) > 3:
    print("ERROR! too much argument!")
if len(args) == 3:
    input_file_old = args[0]
    input_file = args[0]
    input_filename = '.'.join(input_file.split('.')[0:-1])
    rand_id = str(randint(1,99999999))
    os.system('cp '+input_file+' '+input_filename+'_temp'+rand_id+'.fa')
    input_filename += '_temp'+rand_id
    input_file = input_filename + '.fa'
    input_filename_noprefix = input_filename.split(r'/')[-1]
    #print(input_file)
    #print(input_filename)
    #print(input_filename_noprefix)
    output_file = args[1]
    modelname = args[2]
    #print(args)
    curr_dir = os.getcwd()
    if len(pipeline.read_fasta(input_file)) > 1:
        multi = True
    else:
        multi = False

    cmd_pfam_nbslrr = r'pfam_scan.pl -fasta ' +input_file + r' -dir HMMs/NBS_LRR_HMM -outfile ' + input_filename_noprefix + '_pfam.out'
    cmd_deeplrr = r'python scripts/DeepLRR-1.01/DeepLRR.py '+input_file + ' 4 9 3 '+ 'scripts/DeepLRR-1.01 ' + modelname#/home/lifeng/DeepLRR/scripts/DeepLRR-1.02'
    print('>>Running PfamScan...')
    os.system(cmd_pfam_nbslrr)
    print('>>PfamScan Successful!')
    integrated_table, integrated_id = pipeline.pfam_process_nbslrr(input_filename_noprefix + '_pfam.out', input_file)
    if not integrated_table:
        print('NO DOMAIN IDENTIFIED')
        os.system('rm ' + input_file)
        os.system('rm '+input_filename_noprefix+'_pfam.out')
        quit()
    os.system('rm ' + input_filename_noprefix +'_pfam.out')
    print('>>Running DeepLRR...')
    os.system(cmd_deeplrr)
    lrr_table, lrr_id = pipeline.deeplrr_process(r'scripts/DeepLRR-1.01/outcome/'+input_filename_noprefix+r'_predict2.txt')
    print('>>DeepLRR Successful!')
    os.system('rm scripts/DeepLRR-1.01/outcome/'+input_filename_noprefix+r'_*')
    #print(lrr_table)
    thereis = pipeline.output_nbs_lrr(integrated_id, lrr_id, integrated_table, lrr_table, output_file, multi)
    if not thereis:
        print('NO DOMAIN IDENTIFIED')
        os.system('rm '+output_file)
        os.system('rm '+input_file)
        quit()
    print('\nSearch Completed! Results has written to > '+output_file+'\n')
    os.system('rm '+input_file)
