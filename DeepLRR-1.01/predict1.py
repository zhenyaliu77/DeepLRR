#! /usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time   :2020/9/2 20:47
#! @Author :liuzhenya
#! @File   :predict1.py
from model import *
from seqTomatrix import *
import torch
import re
import sys
import os


def aa_dataset_predict(lrr):
    lrr_x = []
    for i in lrr:
        lrr_x.append(aa_matrix(i.split('\t')[0]))
    nplrr_x = np.array(lrr_x)
    return nplrr_x

def Predict(torch_lrr,model):
    model.eval()
    predict_y = model(torch_lrr)
    predict_y = predict_y.data.numpy()
    return predict_y

def Main(initial_path,out_path):
    fin = open(initial_path, 'r')
    fw = open(out_path, 'w')
    info = {}
    for i in fin.readlines():
        i = i.strip()
        if re.search('>',i) != None:
            info[i] = []
        else:
            info[list(info.keys())[-1]].append(i)
    for key in info.keys():
        fw.write(key+'\n')
        if info[key] == []:
            fw.write('No LRR repeat!\n')
        else:
            filter_lrr = []
            lrr = aa_dataset_predict(info[key])
            torch_lrr = torch.from_numpy(lrr).float()
            predict_lrr = Predict(torch_lrr, LRRNet)
            for i in range(len(predict_lrr)):
                if predict_lrr[i][0] > predict_lrr[i][1]:
                    filter_lrr.append(info[key][i]+'\t'+str(predict_lrr[i][0])+'\t'+'LRR\n')
                else:
                    continue
                    #filter_lrr.append(info[key][i] + '\t' + str(predict_lrr[i][0]) + '\t' + 'NOLRR\n')
            #filtered_lrr = sorted(filter_lrr, key=lambda x: float(x.split('\t')[1]))
            if filter_lrr == []:
                fw.write('No LRR repeat!\n')
            else:
                for i in filter_lrr:
                    fw.write(i)

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    model_name = sys.argv[3]
    deeplrr_path = sys.argv[0]
    deeplrr_path_m = [i for i in deeplrr_path.split('/')]
    deeplrr_path_m.pop()
    curr_dir = '/'.join(deeplrr_path_m)
    cnnmodel_path = curr_dir + r'/model/'+model_name
    LRRNet = LRRCNN()
    LRRNet = LRRNet.float()
    LRRNet.load_state_dict(torch.load(cnnmodel_path))
    Main(input_path, output_path)

