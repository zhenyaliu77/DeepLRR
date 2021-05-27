#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/8/31 19:35
#! @Auther  :liuzhenya
#! @File    :fastaTosegment.py
import re
import sys




def ProteinToDict(path):
    #Return a dictionary with id as key and sequence as value
    protein_seq = ''
    new_protein_seq = ''
    protein_id = ''
    protein_id_seq = {}
    fin_protein = open(path,'r')
    for i in fin_protein.readlines():
        i = i.strip('\n')
        if re.search('>',i) != None and protein_seq != '':
            for j in protein_seq:
                    new_protein_seq += j
            protein_id_seq[protein_id] = new_protein_seq
            new_protein_seq = ''
            protein_seq = ''
            protein_id = ''
        if re.search('>',i) != None:
            protein_id = i.split(' ')[0]
            continue
        protein_seq += i
    for j in protein_seq:
        new_protein_seq += j
        protein_id_seq[protein_id] = new_protein_seq
        fin_protein.close()
    return protein_id_seq

def GenerateSeqSegment(sequence,start,end):
    #Sequence represents the input sequence
    #Start represents the start position
    #End represents the end position
    pattern = ''
    len_seq = len(sequence)
    all_pattern = len_seq - end +1
    segment = []
    for i in range(0,all_pattern):
        for i in range(start,end):
            pattern += sequence[i]
        segment.append(pattern)
        start += 1
        end += 1
        pattern = ''
    return segment

def GenerateWindow(seq,start,end):   
	#return[[],[],[],...]
    Window = []
    for i in seq:
        window = GenerateSeqSegment(i,start,end)
        Window.append(window)
    return Window

def GenerateInfo(key,window_list,outpath):
    fw = open(outpath,'a')
    fw.write(key+'\n')
    for window in window_list:
        for one_protein in window:
            for n in range(len(one_protein)):
                fw.write(one_protein[n]+'\t'+str(n+1)+'\n')
    fw.close()


if __name__ == '__main__':
    fasta_path = sys.argv[1]
    output_path = sys.argv[2]
    stay_dict = ProteinToDict(fasta_path)
    for key in stay_dict.keys():
        window_list = []
        for n in range(20,31):
            window = GenerateWindow([stay_dict[key]], 0, n)
            window_list.append(window)
        GenerateInfo(key,window_list,output_path)
