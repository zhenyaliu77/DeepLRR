#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/11/24 16:51
#! @Auther  :liuzhenya
#! @File    :DeepLRR.py
#run the pipeline of DeepLRR
import os
import sys

argv_list = sys.argv
#print(len(sys.argv))
#print(sys.argv)
if len(argv_list) == 2 and argv_list[1] == '-h':
    print('DeepLRR version 1.01 by Zhenya Liu (zhenyaliu77@gmail.com)\n'
          'Usage:\n'
          'python DeepLRR.py *.fasta Lscp Ldcp Lncp\n'
          '*.fasta      query input files are FASTA .fasta(default)\n'
          'Lscp <int>   Leucine-rich repeat score control parameter are in [1,11] 4(default)\n'
          'Ldcp <int>   Leucine-rich repeat distance control parameter are in [1,∞] 9(default)\n'
          'Lncp <int>   Leucine-rich repeat distance control parameter are in [2,∞] 3(default)\n'
          '-h           print this usage message\n'
          'output files in ../DeepLRR-1.01/outcome\n')
if len(argv_list) == 2 and argv_list[1] != '-h':
    print('Please input control parameters!')

if len(argv_list) == 3:
    print('Please input Ldcp and Lncp !')

if len(argv_list) == 4:
    print('Please input Lncp !')

if len(argv_list) == 7:
    fasta_path = sys.argv[1]
    Lscp = sys.argv[2]
    Ldcp = sys.argv[3]
    Lncp = sys.argv[4] 
    #deeplrr_path = sys.argv[0]
    #print(deeplrr_path)

    #deeplrr_path_m = deeplrr_path.split('/')
    #deeplrr_path_m.pop()
    #curr_dir = '/'.join(deeplrr_path_m)
    #print(deeplrr_path_m)
    #print(curr_dir)
    curr_dir = sys.argv[5]
    model_name = sys.argv[6] 
    #print(len(sys.argv))
    #print(sys.argv) 
    out_dir = os.path.exists(curr_dir+'/outcome')
    if out_dir == False:
        os.mkdir(curr_dir+'/outcome')

    fasta_name = fasta_path.split('/')[-1]
    command1 = 'python '+curr_dir+'/fastaTosegment.py '+fasta_path+' '+curr_dir+'/outcome'+'/'+fasta_name.split('.')[0]+'_segment.txt'

    command2 = 'python '+curr_dir+'/predict1.py '+curr_dir+'/outcome'+'/'+fasta_name.split('.')[0]+'_segment.txt'+' '+curr_dir+'/outcome'+'/'+fasta_name.split('.')[0]+'_predict1.txt'+' '+model_name+'.pt'

    command3 = 'python '+curr_dir+'/predict2.py '+curr_dir+'/outcome'+'/'+fasta_name.split('.')[0]+'_predict1.txt'+' '+str(Lscp)+' '+str(Ldcp)+' '+str(Lncp)+' '+curr_dir+'/outcome'+'/'+fasta_name.split('.')[0]+'_predict2.txt'
    
    command4 = 'python '+curr_dir+'/gapsequence.py '+fasta_path+' '+curr_dir+'/outcome/'+fasta_name.split('.')[0]+'_predict2.txt'+' '+str(Ldcp)+' '+curr_dir+'/gapsequence.txt'
    os.system(command1)
    os.system(command2)
    os.system(command3)
    os.system(command4)
    # print("done")
