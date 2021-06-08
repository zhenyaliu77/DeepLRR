# encoding: utf-8
"""
@author: ZiRui Ren
@contact: 1131061444@qq.com/renzirui@webmail.hzau.edu.cn
@time: 2020/12/9 15:39
@file: LRR_RLP_RLK.py
@desc: 
"""
import os
import getopt
import pipeline
import sys
from random import randint


opts, args = getopt.getopt(sys.argv[1:], '-h-k', ["help", "kinase"])
kinase = False
for opt_name, opt_value in opts:
    if opt_name in ('-h', '--help'):
        print('DeepLRR Pipeline (LRR-RLP/RLK) v1.0beta by ZiRui Ren\n'
              '  Usage:\n'
              '\tpython LRR_RLP_RLK.py <-k> <inputfile> <outputfile>\n\n'
              '  <-k> or <--kinase>  if need LRR_RLK protein\n'
              '  <-h> or <--help> if need help\n'
              )
        exit()
    if opt_name in ('-k', '--kinase'):
        kinase = True
if len(args) < 3:
    print("ERROR! lack of argument!")
    exit()
elif len(args) > 3:
    print("ERROR! too much argument!")
    exit()
elif len(args) == 3:   
    scriptdir = 'scripts/DeepLRR-1.01'
    input_file = args[0]
    input_filename = '.'.join(input_file.split('.')[0:-1])
    rand_id = str(randint(1,99999999))
    os.system('cp '+input_file+' '+input_filename+'_temp'+rand_id+'.fa')
    input_filename += '_temp'+rand_id
    input_file = input_filename + '.fa'
    input_filename_noprefix = input_filename.split(r'/')[-1]
    output_file = args[1]
    modelname = args[2]
    curr_dir = os.getcwd()
    #print(input_file, input_filename)
    #quit()
    if len(pipeline.read_fasta(input_file)) > 1:
        multi = True
    else:
        multi = False
    cmd_pfam = r'pfam_scan.pl -fasta '+input_file + r' -dir HMMs/Pkinase_HMM -outfile '+ input_filename_noprefix + '_pfam.out'
    cmd_sp = r'signalp -org euk -format summary -fasta '+ input_file
    cmd_tm = r'tmhmm ' + input_file + r' > '+ input_filename_noprefix + '_TMHMM.out'
    cmd_deeplrr = r'python scripts/DeepLRR-1.01/DeepLRR.py ' + input_file + r' 4 9 3 '+ scriptdir +' '+ modelname
    #print(kinase)
    print('>>Running PfamScan...')
    os.system(cmd_pfam)
    pk_table, pk_seqid, nopk_seqid = pipeline.pfam_process_pkinase(input_filename_noprefix + '_pfam.out', input_file)
    print('>>PfamScan Completed!')
    #print(pk_seqid)
    os.system('rm ' + input_filename_noprefix + '_pfam.out')
    print('>>Running SignalP...')
    os.system(cmd_sp)
    sp_table, sp_seqid = pipeline.signalp_process( input_filename_noprefix + '_summary.signalp5', input_file)
    print('>>SignalP Completed!')
    #print(sp_seqid)
    os.system('rm ' + input_filename_noprefix + '_summary.signalp5')
    if not len(sp_seqid):
        print('NO DOMAIN IDENTIFIED')
        os.system('rm '+ input_file)
        quit()
    print('>>Running TMHMM...')
    os.system(cmd_tm)
    tm_table, tm_seqid = pipeline.tmhmm_process( input_filename_noprefix + '_TMHMM.out', input_file)
    print('>>TMHMM Completed!')
    #print(tm_seqid)
    if not len(tm_seqid):
    	os.system('rm '+ input_filename_noprefix + '_TMHMM.out')
    	os.system('rm -rf TMHMM_*')
    	print('NO DOMAIN IDENTIFIED')
    	os.system('rm '+ input_file)
    	quit()
    os.system('rm ' + input_filename_noprefix + '_TMHMM.out')
    os.system('rm -rf TMHMM_*')
    print('>>Running DeepLRR...')
    os.system(cmd_deeplrr)
    lrr_table, lrr_seqid = pipeline.deeplrr_process(r'scripts/DeepLRR-1.01/outcome/'+input_filename_noprefix+r'_predict2.txt')
    print('>>DeepLRR Completed!')
    #print(lrr_seqid)
    #os.system('chmod 777 scripts/DeepLRR-1.01/outcome/'+input_filename_noprefix+r'_*')
    os.system('rm scripts/DeepLRR-1.01/outcome/'+input_filename_noprefix+r'_*')
    print('>>Generating output...')
    thereis = pipeline.output_lrr_rlpk(nopk_seqid, pk_seqid, sp_seqid, tm_seqid, lrr_seqid, pk_table, sp_table, tm_table, lrr_table, output_file, multi, kinase)
    if not thereis:
        print('NO DOMAIN IDENTIFIED!')
        os.system('rm ' + output_file)
        os.system('rm ' + input_file)
    os.system('rm ' + input_file)
    print('\nSearch Completed! Results has written to > '+output_file+'\n')

