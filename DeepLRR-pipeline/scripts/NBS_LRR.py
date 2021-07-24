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
    wdir = '/var/www/lifenglab/DeepLRR/Upfile/NBS_file/'
    input_file = args[0]
    # print(input_file)
    input_filename = '.'.join(input_file.split('.')[0:-1])
    # print(input_filename)
    output_file = args[1]
    modelname = args[2]
    print(args)
    curr_dir = os.getcwd()
    if len(pipeline.read_fasta(wdir+input_file)) > 1:
        multi = True
    else:
        multi = False
    cmd_pfam_nbs = r'pfam_scan.pl -fasta ' +wdir+ input_file + r' -dir /home/lifeng/DeepLRR/HMMs/NBS_HMM -outfile ' + wdir + input_filename + '_pfam.out'
    cmd_pfam_tir = r'pfam_scan.pl -fasta ' +wdir+ input_file + r' -dir /home/lifeng/DeepLRR/HMMs/TIR_HMM -outfile ' + wdir + input_filename + '_pfam.out'
    cmd_deeplrr = r'python /home/lifeng/DeepLRR/scripts/DeepLRR-1.02/DeepLRR.py '+ wdir +input_file+' 4 9 3 '+'/home/lifeng/DeepLRR/scripts/DeepLRR-1.02 ' + modelname#/home/lifeng/DeepLRR/scripts/DeepLRR-1.02'
    cmd_coils = r'coils < ' + wdir + input_file + ' -c -min_seg 1 > ' + wdir + input_filename + '_coils.out'
    
    #FIND NB-ARC @PfamScan
    print('Running PfamScan...')
    os.system(cmd_pfam_nbs)
    print('PfamScan Successful!')
    nbs_table, nbs_id = pipeline.pfam_process_nbslrr_v2(wdir + input_filename + '_pfam.out', wdir + input_file, wdir)
    if not nbs_table:
        print('NO DOMAIN IDENTIFIED!')
        os.system('rm '+wdir+input_file)
        os.system('rm '+wdir+input_filename+'_pfam.out')
        exit()
    os.system('rm ' + wdir + input_filename+'_pfam.out')
    pipeline.rewrite_fasta(wdir + input_file, nbs_id)
    
    #FIND LRR @DeepLRR
    print('Running DeepLRR...')
    os.system(cmd_deeplrr)
    lrr_table, lrr_id = pipeline.deeplrr_process(r'/home/lifeng/DeepLRR/scripts/DeepLRR-1.02/outcome/'+input_filename+r'_predict2.txt')
    print('DeepLRR Successful!')
    if not len(lrr_id):
        print('NO DOMAIN IDENTIFIED!')
        os.system('rm '+wdir+input_file)
        os.system('rm /home/lifeng/DeepLRR/scripts/DeepLRR-1.02/outcome/'+input_filename+r'_*')
        exit()
    os.system('rm /home/lifeng/DeepLRR/scripts/DeepLRR-1.02/outcome/'+input_filename+r'_*')
    #print(lrr_table)
    pipeline.rewrite_fasta(wdir + input_file, lrr_id)
    
    #FIND TIR @DeepLRR
    print('Running PfamScan...')
    os.system(cmd_pfam_tir)
    print('PfamScan Successful!')
    tir_table, tir_id = pipeline.pfam_process_tir(wdir + input_filename + '_pfam.out', wdir + input_file, wdir)
    os.system('rm ' + wdir + input_filename+'_pfam.out')
    
    #FIND CC @COILS
    print('Running COILS...')
    os.system(cmd_coils)
    print('COILS Successful!')
    cc_table, cc_id = pipeline.coils_process(wdir + input_filename + '_coils.out')
    os.system('rm ' + wdir + input_filename+'_coils.out')
    
    thereis = pipeline.output_nbs_lrr(nbs_id, lrr_id, tir_id, cc_id, nbs_table, lrr_table, tir_table, cc_table, wdir+output_file, multi)
    if not thereis:
        print('NO DOMAIN IDENTIFIED!')
        os.system('rm '+wdir+output_file)
        os.system('rm '+wdir+input_file)
        exit()
    print('Completed! Results has written to > '+output_file)
    os.system('rm '+wdir+input_file)
