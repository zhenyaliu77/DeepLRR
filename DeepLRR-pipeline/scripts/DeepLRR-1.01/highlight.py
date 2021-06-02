#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2021/1/30 12:42
#! @Auther  :liuzhenya
#! @File    :highlight.py
import sys


def CollectInfo(path):
    info = {}
    fin = open(path,'r')
    for i in fin.readlines():
        i = i.strip()
        if 'Score' not in i:
            if i.split('\t')[0] not in info.keys():
                info[i.split('\t')[0]] = []
                info[i.split('\t')[0]].append(i)
            else:
                info[list(info.keys())[-1]].append(i)
        else:
            continue
    return info

def GenerateSeqSegment(sequence,start,end):
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

def Score(aa,index):
    score_0 = {'L':9,'I':3,'V':3,'M':3,'T':3,'F':3,'A':1,'Y':1,'C':1,'S':1,'P':1,'Q':1,'D':1,'N':1,'K':1,'G':1,'E':1}
    score_3 = {'L':9,'I':3,'V':3,'F':3,'M':3,'A':1,'C':1,'W':1,'T':1,'S':1}
    score_5 = {'L':9,'V':3,'I':3,'F':3,'M':3,'A':3,'C':3,'T':1,'G':1,'Y':1,'W':1,'R':1,'Q':1}
    score_8 = {'N':9,'C':3,'T':3,'S':3,'V':1,'A':1,'M':1,'L':1,'Q':1,'Y':1,'I':1,'G':1,'K':1,'H':1,'D':1,'R':1,'P':1,'F':1,'W':1}
    score_10 = {'L':9,'I':3,'F':3,'V':3,'M':3,'S':3,'N':3,'K':1,'R':1,'Q':1,'E':1,'Y':1,'G':1,'D':1,'H':1,'A':1,'W':1,'T':1,'P':1,'C':1}
    matrix = [score_0,0,0,score_3,0,score_5,0,0,score_8,0,score_10]
    if aa not in matrix[index].keys():
        return 0
    else:
        return matrix[index][aa]

def Highlight(lrr):
    segment = GenerateSeqSegment(lrr,0,11)
    segment_dic = {}
    for seg in segment:
        segment_dic[seg] = Score(seg[0],0)+Score(seg[3],3)+Score(seg[5],5)+Score(seg[8],8)+Score(seg[10],10)
    c = sorted(segment_dic.items(),key=lambda x:x[1])
    max_pair = []
    max_score = int(c[-1][1])
    for i in c:
        if int(i[1]) == max_score:
            max_pair.append(i)
        else:
            continue
    if int(max_pair[0][1]) < 5:
        return 'None'
    else:
        return max_pair[0][0]


def Rewrite(info,outpath):
    fw = open(outpath, 'w')
    fw.write('Protein ID\tSequence\tLength\tStart\tEnd\tScore\tStatus\n')
    for key in info.keys():
        for i in info[key]:
            if 'None' not in i:
                hcs = Highlight(i.split('\t')[1])
                new_hcs = ''
                for j in range(len(hcs)):
                    if j in [0,3,5,8,10]:
                        new_hcs += hcs[j].lower()
                    else:
                        new_hcs += hcs[j]
                if hcs != 'None':
                    a = i.split('\t')[1].split(hcs)
                    b = a[0] + new_hcs + a[1]
                    c = i.split('\t')
                    c[1] = b
                    fw.write('\t'.join(c) + '\n')
                else:
                    fw.write(i + '\n')
            else:
                fw.write(i + '\n')


if __name__ == '__main__':
    predict2_path = sys.argv[1]
    highlight_path = sys.argv[2]
    info = CollectInfo(predict2_path)
    Rewrite(info,highlight_path)

