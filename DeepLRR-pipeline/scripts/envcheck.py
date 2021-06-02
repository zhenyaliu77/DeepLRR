# encoding: utf-8
"""
@author: ZiRui Ren
@contact: 1131061444@qq.com/renzirui@webmail.hzau.edu.cn
@time: 2021/6/2 07:22
@file: envcheck.py
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
        print('[ERROR] hmmer not found, Please install it before LRR_Search, or check if its path has been add to $PATH!')
        checked = False
    try:
        import torch
    except ModuleNotFoundError:    
        print('[ERROR] Pytorch have not installed yet, please install pytorch!')
        checked = False

if __name__ == '__main__':
    checked = env_check()
    if not checked:
        quit()
    else:
