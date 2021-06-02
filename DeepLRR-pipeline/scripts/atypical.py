# encoding: utf-8
"""
@author: ZiRui Ren
@contact: 1131061444@qq.com/renzirui@webmail.hzau.edu.cn
@time: 2020/12/17 1:26
@file: atypia.py
@desc: Finding atypia domains in giving sequences
"""
import os
import getopt
import sys
import pipeline


opts, args = getopt.getopt(sys.argv[1:], '-h', ["help"])
for opt_name, opt_value in opts:
    if opt_name in ('-h', '--help'):
        print('DeepLRR Pipeline (Atypia Domain) v1.0beta by ZiRui Ren\n'
              '  Usage:\n'
              '\tpython atypia.py <inputfile> <outputfile> <protein type>\n\n'
              '  <-h> or <--help> if need help\n'
              '  <protein type> only has three options:\n'
              '     NBS_LRR|LRR_RLK|LRR_RLP'
              )
        quit()
if len(args) < 3:
    print("[ERROR] lack of argument!")
if len(args) > 3:
    print("[ERROR] too much argument!")
if len(args) == 3:

    input_file = args[0]
    # print(input_file)
    input_filename = '.'.join(input_file.split('.')[0:-1])
    print(input_filename)
    # print(input_filename)
    output_file = args[1]
    protein_type = args[2]

    cmd_pfam = cmd_pfam_nbslrr = r'pfam_scan.pl -fasta ' + input_file + r' -dir HMMs/atypia_HMM -outfile '+ input_filename + '_pfam.out'
    os.system(cmd_pfam)
    pipeline.pfam_process_atypia(input_filename + '_pfam.out',output_file , protein_type)
    os.system('rm ' + input_filename + '_pfam.out')

