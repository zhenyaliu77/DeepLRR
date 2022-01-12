#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/12/22 22:27
#! @Auther  :liuzhenya
#! @File    :manual_check.py
import re
import sys


def ProteinToDict(path):
    # 返回序列号为键，序列为值的字典
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

def Gap_Sequence(path):
    fin = open(path,'r')
    lrr_motif = {}
    for i in fin.readlines():
        i = i.strip()
        if 'LRR' in i:
            if '>'+i.split('\t')[0] not in lrr_motif.keys():
                lrr_motif['>'+i.split('\t')[0]] = []
                lrr_motif['>'+i.split('\t')[0]].append(i.split('\t')[3]+'-'+i.split('\t')[4])
            else:
                lrr_motif[list(lrr_motif.keys())[-1]].append(i.split('\t')[3]+'-'+i.split('\t')[4])
        else:
            continue
   # print(lrr_motif)
    new_lrr_motif = {}
    for key in lrr_motif.keys():
        new_lrr_motif[key] = []
        for n in range(len(lrr_motif[key]) - 1):
            new_lrr_motif[key].append(lrr_motif[key][n].split('-')[1]+'-'+lrr_motif[key][n+1].split('-')[0])
    #print(new_lrr_motif)
    lrr_gap = {}
    for key in new_lrr_motif.keys():
        lrr_gap[key] = []
        for n in range(len(new_lrr_motif[key])):
            #print(int(new_lrr_motif[key][n].split('-')[1])-int(new_lrr_motif[key][n].split('-')[0]))
            if 21 <= int(new_lrr_motif[key][n].split('-')[1])-int(new_lrr_motif[key][n].split('-')[0]) <= 41:
                lrr_gap[key].append(new_lrr_motif[key][n])
            else:
                continue
    return lrr_gap

def SaveGap(lrr_gap,protein,outpath):
    fw = open(outpath,'a')
    for key in lrr_gap:
        if lrr_gap[key] != []:
            fw.write(key+'\n')
            for i in lrr_gap[key]:
                fw.write(protein[key][int(i.split('-')[0]):int(i.split('-')[1])-1]+'\n')
        else:
            continue
    fw.close()




if __name__ == '__main__':
    protein_path = sys.argv[1]
    predict2_path = sys.argv[2]
    outpath = sys.argv[3]
    protein = ProteinToDict(protein_path)
    #print(protein)
    lrr_gap = Gap_Sequence(predict2_path)
    #print(lrr_gap)
    SaveGap(lrr_gap,protein,outpath)
