#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2021/3/20 14:00
#! @Auther  :liuzhenya
#! @File    :split_train_test.py
import random
import sys
import os


def CollectLrr(path,label):
    fin = open(path,'r')
    lrr_dic = {}
    for i in fin.readlines():
        i = i.strip()
        if len(i) not in lrr_dic.keys():
            lrr_dic[len(i)] = []
            lrr_dic[len(i)].append(i+'\t'+label)
        else:
            lrr_dic[len(i)].append(i + '\t' + label)
    return lrr_dic

def CreateRange(number):
    rangenum = []
    for i in range(0,number):
        rangenum.append(i)
    return rangenum

def DeleteSome(one_index,two_index):
    one_index = set(one_index)
    two_index = set(two_index)
    index = list(one_index - two_index)
    return index

def Group(lrr_list):
    group_dic = {}
    all_index = CreateRange(len(lrr_list))
    for i in range(1,6):
        group_dic[i] = []
        index_20 = random.sample(all_index,int(0.2*len(lrr_list)))
        #print(index_20[0])
        for j in index_20:
            group_dic[i].append(lrr_list[j])
        #print(len(all_index),len(index_20))
        all_index = DeleteSome(all_index,index_20)
    return group_dic

def CreateInfo(group_pos,group_neg,index_train,index_test,path_train,path_test):
    fw_train = open(path_train,'a')
    fw_test = open(path_test,'a')
    #生成测试集
    for i in group_pos[index_test]:
        fw_test.write(i+'\n')
    for i in group_neg[index_test]:
        fw_test.write(i+'\n')
    #生成训练集
    for index in index_train:
        for i in group_pos[index]:
            fw_train.write(i + '\n')
        for i in group_neg[index]:
            fw_train.write(i + '\n')
    fw_train.close()
    fw_test.close()

def DeleteLabel(path,outpath,label):
    fin = open(path,'r')
    fw = open(outpath,'w')
    for i in fin.readlines():
        i = i.strip()
        if i.split('\t')[1] == label:
            fw.write(i.split('\t')[0]+'\n')
        else:
            continue



if __name__ == '__main__':
    curr_path = os.getcwd()
    pos_input = sys.argv[1]
    #Path of the positive sample dataset
    neg_input = sys.argv[2]
    #Path of the negative sample dataset
    train_path = curr_path+'/train.txt'
    test_path = curr_path+'/test.txt'
    #training set : testing set = 4:1
    lrr_pos = CollectLrr(pos_input,'LRR')
    lrr_neg = CollectLrr(neg_input,'NOLRR')
    for key in lrr_pos.keys():
        group_pos = Group(lrr_pos[key])
        group_neg = Group(lrr_neg[key])
        CreateInfo(group_pos,group_neg,[1,2,3,4],5,train_path,test_path)
