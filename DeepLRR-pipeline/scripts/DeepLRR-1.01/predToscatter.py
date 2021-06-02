#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/11/24 21:37
#! @Auther  :liuzhenya
#! @File    :predToscatter.py
import matplotlib.pyplot as plt
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

def Title(dic):
    if '>' in list(dic.keys())[0]:
        protein_id = list(dic.keys())[0].split('>')[1]
    else:
        protein_id = 'None'
    length = len(list(dic.values())[0])
    return protein_id,length

def PredToDict(path):
    fin_pred = open(path, 'r')
    pred_x = []
    pred_y = []
    for i in fin_pred.readlines():
        i = i.strip('\n')
        if 'LRR' in i:
            pred_x.append(int(i.split('\t')[3]))
            pred_y.append(float(i.split('\t')[5]))
        else:
            continue
    return pred_x,pred_y

def Drawing(protein_id,protein_len,pred_x,pred_y,pred2_path):
    plt.figure(figsize=(16, 8))
    plt.title(protein_id)
    plt.xlabel('Sites')
    plt.ylabel('Score')
    plt.ylim(0, 1.05)
    plt.hlines(0.5,0,protein_len,colors='#FF0000',linestyles='dashed')
    plt.scatter(pred_x,pred_y,label='LRR',alpha=1,s=5)
    plt.legend(loc='upper right')
    plt.savefig(plot_path)
    plt.show()


if __name__ == '__main__':
    fasta_path = sys.argv[1]
    pred2_path = sys.argv[2]
    plot_path = sys.argv[3]
    #print title information
    dic = ProteinToDict(fasta_path)
    protein_id,protein_len = Title(dic)
    #print(protein_id,specie,protein_len)

    #draw scatter plot
    pred_x,pred_y = PredToDict(pred2_path)
    #print(pred_x)
    #print(pred_y)
    Drawing(protein_id,protein_len,pred_x,pred_y,plot_path)




