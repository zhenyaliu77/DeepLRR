#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/10/4 20:24
#! @Auther  :liuzhenya
#! @File    :input_matrix.py
import numpy as np


def aa_vector(aa):
    score_dic = {
        'A':[0,0,0,0,1],
        'C':[0,0,0,1,0],
        'D':[0,0,0,1,1],
        'E':[0,0,1,0,0],
        'F':[0,0,1,0,1],
        'G':[0,0,1,1,0],
        'H':[0,0,1,1,1],
        'I':[0,1,0,0,0],
        'K':[0,1,0,0,1],
        'L':[0,1,0,1,0],
        'M':[0,1,0,1,1],
        'N':[0,1,1,0,0],
        'P':[0,1,1,0,1],
        'Q':[0,1,1,1,0],
        'R':[0,1,1,1,1],
        'S':[1,0,0,0,0],
        'T':[1,0,0,0,1],
        'V':[1,0,0,1,0],
        'W':[1,0,0,1,1],
        'Y':[1,0,1,0,0],
        'padding':[1,0,1,0,1]
    }
    if aa in score_dic.keys():
        return score_dic[aa]
    else:
        return [1,0,1,0,1]

def aa_matrix(pro_seq):
    matrix = []
    for aa in pro_seq:
        matrix.append(aa_vector(aa))
    for i in range(len(pro_seq),30):
        matrix.append(aa_vector('padding'))
    return [matrix]

def aa_dataset(path):
    fin = open(path,'r')
    lrr_x = []
    lrr_y = []
    pick_y = [[1.0,0.0],[0.0,1.0]]
    for i in fin.readlines():
        i = i.strip()
        if i.split('\t')[1] == 'LRR':
            lrr_x.append(aa_matrix(i.split('\t')[0]))
            lrr_y.append(pick_y[0])
        else:
            lrr_x.append(aa_matrix(i.split('\t')[0]))
            lrr_y.append(pick_y[1])
    nplrr_x = np.array(lrr_x)
    nplrr_y = np.array(lrr_y)
    return nplrr_x,nplrr_y



