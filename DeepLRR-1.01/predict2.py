#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/10/13 16:48
#! @Auther  :liuzhenya
#! @File    :process.py
import sys


def GroupSite(path):
    fin = open(path,'r')
    allgroupsite = {}
    for i in fin.readlines():
        i = i.strip()
        if '>' not in i and i != 'No LRR repeat!':
            if int(i.split('\t')[1]) not in allgroupsite[list(allgroupsite.keys())[-1]].keys():
                allgroupsite[list(allgroupsite.keys())[-1]][int(i.split('\t')[1])] = []
                allgroupsite[list(allgroupsite.keys())[-1]][int(i.split('\t')[1])].append(i)
            else:
                allgroupsite[list(allgroupsite.keys())[-1]][int(i.split('\t')[1])].append(i)
        if '>' in i and i != 'No LRR repeat!':
            allgroupsite[i] = {}
    return allgroupsite

def HoldBestOne(dic):
    dic_new = {}
    for key in dic.keys():
        score_list = []
        for i in dic[key]:
            score_list.append(float(i.split('\t')[2]))
        dic_new[key] = dic[key][score_list.index(max(score_list))]
    return dic_new

def DrawHeatMap(groupsite):
    complete_value = {}
    for key in groupsite.keys():
        value = {}
        for i in groupsite[key]:
            complete_value[int(i.split('\t')[1])] = []
            value[len(i.split('\t')[0])] = float(i.split('\t')[2])
        complete_value[list(complete_value.keys())[-1]].append(value)
    for i in range(min(list(complete_value.keys())), max(list(complete_value.keys())) + 1):
        if i not in complete_value.keys():
            complete_value[i] = [{20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0}]
            sorted_value = zip(complete_value[i][0].keys(), complete_value[i][0].values())
            complete_value[i] = list(sorted(sorted_value))
        else:
            for j in range(20, 31):
                if j not in complete_value[i][0].keys():
                    complete_value[i][0][j] = 0
                else:
                    continue
            sorted_value = zip(complete_value[i][0].keys(), complete_value[i][0].values())
            complete_value[i] = list(sorted(sorted_value))
    return complete_value

def GroupInterval(path):
    fin = open(path, 'r')
    groupinterval = {}
    for i in fin.readlines():
        i = i.strip()
        if '>' in i:
            groupinterval[i] = []
        else:
            groupinterval[list(groupinterval.keys())[-1]].append(i.split('\t')[0])
    interval = {}
    for key in groupinterval.keys():
        # print(groupinterval[key])
        site_list = []
        for i in range(len(groupinterval[key])):
            if i == 0:
                site_list.append(int(groupinterval[key][i].split('-')[1]))
            if i == len(groupinterval[key]) - 1:
                site_list.append(int(groupinterval[key][i].split('-')[0]))
            if 0 < i < len(groupinterval[key]) - 1:
                site_list.append(int(groupinterval[key][i].split('-')[0]))
                site_list.append(int(groupinterval[key][i].split('-')[1]))
        # print(site_list)
        i = 0
        while i < len(site_list) - 1:
            if site_list[i + 1] - site_list[i] not in interval.keys():
                interval[site_list[i + 1] - site_list[i]] = 1
                i += 2
            else:
                interval[site_list[i + 1] - site_list[i]] += 1
                i += 2
    interval_sorted = sorted(interval.items(), key=lambda x: x[0])
    for i in interval_sorted:
        print(str(i[0]) + '\t' + str(i[1] / sum(interval.values())))

def FastQ(groupsite,n):   #n为连通度
    n_list = []
    for i in range(20,20+n):
        n_list.append(i)
    for key in list(groupsite.keys()):
        key_len = []
        for lrr in groupsite[key]:
            key_len.append(len(lrr.split('\t')[0]))
        for i in n_list:
            if i not in key_len:
                del groupsite[key]
                break
            else:
                continue
    return groupsite

def CalculateFirst(groupsite):
    #为什么不算平均，因为在两个LRR之间的片段往往会平均分很高
    #同样的道理也不能求最大值
    #最好的就是取20aa的得分
    mean_dic = {}
    for key in groupsite.keys():
        mean_dic[key] = float(groupsite[key][0].split('\t')[2])
    return mean_dic

def Clip(a,b):
    count = int(a/b)
    clip_list = []
    for i in range(count):
        clip = (i*b+1,(i+1)*b)
        clip_list.append(clip)
    return clip_list

def BestScoreAA(groupsite,clip_n):
    #20aa最多只能有1个LRRrepeat
    groupsite_sorted = sorted(groupsite.items(), key=lambda x: x[0])
    clip_list = Clip(groupsite_sorted[-1][0]+30,clip_n)
    protein_value = []
    for clip in clip_list:
        clip_value = {}
        for info in groupsite_sorted:
            if clip[0] <= info[0] <= clip[1]:
                clip_value[info[0]] = info[1]
            else:
                continue
        if clip_value != {}:
            protein_value.append(str(sorted(clip_value, key=lambda x: clip_value[x])[-1])+'\t'+str(clip_value[sorted(clip_value, key=lambda x: clip_value[x])[-1]]))
        else:
            continue
    return protein_value

def DeleteOther(onecluster):          #make sure the best score infos >= 20aa
    new_onecluster = []
    Blacklist = []
    for i in range(len(onecluster)):
        if i <= len(onecluster) - 2:
            if int(onecluster[i].split('\t')[0]) + 20 > int(onecluster[i+1].split('\t')[0]):
                #distance < 20aa
                if float(onecluster[i].split('\t')[1]) >= float(onecluster[i+1].split('\t')[1]):
                    #onecluster[i]'s score >= onecluster[i+1]'s score
                    if onecluster[i] not in new_onecluster and onecluster[i] not in Blacklist:
                        if new_onecluster != []:
                            if int(new_onecluster[-1].split('\t')[0]) + 20 > int(onecluster[i].split('\t')[0]):
                                #the distance between new_onecluster[-1] and onecluster[i] < 20aa
                                if float(new_onecluster[-1].split('\t')[1]) < float(onecluster[i].split('\t')[1]):
                                    #compare the score of both
                                    del new_onecluster[-1]
                                    new_onecluster.append(onecluster[i])
                                    #onecluster[i] replace new_onecluster[-1] successfully
                                else:
                                    continue
                                    #onecluster[i] faid to replace new_onecluster[-1]
                            else:
                                new_onecluster.append(onecluster[i])
                                #the distance between new_onecluster[-1] and onecluster[i] >= 20aa
                        else:
                            new_onecluster.append(onecluster[i])
                            #new_onecluster is [] so onecluster[i] become the new_onecluster[-1] directly
                    if onecluster[i+1] not in Blacklist:
                        Blacklist.append(onecluster[i+1])
                        #take the onecluster[i+1] to blacklist
                else:
                    if onecluster[i+1] not in new_onecluster and onecluster[i+1] not in Blacklist:
                        if new_onecluster != []:
                            if int(new_onecluster[-1].split('\t')[0]) + 20 > int(onecluster[i+1].split('\t')[0]):
                                if float(new_onecluster[-1].split('\t')[1]) < float(onecluster[i+1].split('\t')[1]):
                                    del new_onecluster[-1]
                                    new_onecluster.append(onecluster[i+1])
                                else:
                                    continue
                            else:
                                new_onecluster.append(onecluster[i+1])
                        else:
                            new_onecluster.append(onecluster[i+1])
                    if onecluster[i] not in Blacklist:
                        Blacklist.append(onecluster[i])
            else:
                if onecluster[i] not in new_onecluster and onecluster[i] not in Blacklist:
                    new_onecluster.append(onecluster[i])
                if i == len(onecluster) - 2:
                    new_onecluster.append(onecluster[i+1])
        else:
            break
    return new_onecluster

def Domain(onecluster,n,lrr_num,len_dic):
    #if the distance between onecluster[i] and onecluster[i+1] > 30aa,it will generate the second cluster of onecluster[i+1]
    tem_cluster = []
    all_cluster = []
    #print(onecluster)
    for LRR in onecluster:
        if tem_cluster == []:
            tem_cluster.append(LRR)
        else:
            if int(LRR.split('\t')[0]) - int(tem_cluster[-1].split('\t')[0]) <= n+len(len_dic[int(tem_cluster[-1].split('\t')[0])].split('\t')[0]):
                tem_cluster.append(LRR)
            else:
                if len(tem_cluster) >= lrr_num:
                    all_cluster.append(tem_cluster)
                    tem_cluster = []
                    tem_cluster.append(LRR)
                else:
                    if len(all_cluster) != 0 and len(tem_cluster) > 1:
                        all_cluster.append(tem_cluster)
                        tem_cluster = []
                        tem_cluster.append(LRR)
                    else:
                        tem_cluster = []
                        tem_cluster.append(LRR)
    if len(tem_cluster) >= lrr_num:
        all_cluster.append(tem_cluster)
    if all_cluster != []:
        while len(all_cluster[-1]) < lrr_num:
            all_cluster.pop()
    #print(all_cluster)
    return all_cluster

def ReturnMaxLrr(lrr_list,nextsite):
    score_list = []
    for i in range(len(lrr_list)):
        if int(lrr_list[i].split('\t')[1])+len(lrr_list[i].split('\t')[0])-1 < nextsite:
            score_list.append(lrr_list[i])
        else:
            break
    score = []
    for lrr in score_list:
        score.append(float(lrr.split('\t')[2]))
    return score_list[score.index(max(score))]

def ReturnMaxLrrProcess(lis,dic):
    new_dic = {}
    for i in range(len(lis)):
        if i < len(lis) - 1:
            new_dic[int(lis[i].split('\t')[0])] = ReturnMaxLrr(dic[int(lis[i].split('\t')[0])],int(lis[i+1].split('\t')[0]))
        if i == len(lis) - 1:
            new_dic[int(lis[i].split('\t')[0])] = ReturnMaxLrr(dic[int(lis[i].split('\t')[0])],int(lis[i].split('\t')[0])+30)
    return new_dic


def ShortPredict(allgroupsite,outpath,connect,interval,lrr_num):
    fw = open(outpath,'w')
    fw.write('Protein ID\tSequence\tLength\tStart\tEnd\tScore\tStatus\n')
    for key in allgroupsite.keys():
        if allgroupsite[key] != {}:
            groupsite = CalculateFirst(FastQ(allgroupsite[key],connect))
            if groupsite != {}:
                len_dic = ReturnMaxLrrProcess(DeleteOther(BestScoreAA(groupsite,20)),allgroupsite[key])
                groupsite_new = Domain(DeleteOther(BestScoreAA(groupsite,20)),interval,lrr_num,len_dic)
                if groupsite_new != []:
                    for onedomain in groupsite_new:
                        for i in range(len(onedomain)):
                            if i < len(onedomain) - 1:
                                deeplrr = ReturnMaxLrr(allgroupsite[key][int(onedomain[i].split('\t')[0])],int(onedomain[i+1].split('\t')[0]))
                                newdeeplrr = key.split('>')[1]+'\t'+deeplrr.split('\t')[0]+'\t'+str(len(deeplrr.split('\t')[0]))+'\t'+deeplrr.split('\t')[1]+'\t'+str(int(deeplrr.split('\t')[1])+len(deeplrr.split('\t')[0])-1)+'\t'+deeplrr.split('\t')[2]+'\tLRR\n'
                                fw.write(newdeeplrr)

                            if i == len(onedomain) - 1:
                                deeplrr = ReturnMaxLrr(allgroupsite[key][int(onedomain[i].split('\t')[0])],int(onedomain[i].split('\t')[0])+30)
                                newdeeplrr = key.split('>')[1]+'\t'+deeplrr.split('\t')[0]+'\t'+str(len(deeplrr.split('\t')[0]))+'\t'+deeplrr.split('\t')[1]+'\t'+str(int(deeplrr.split('\t')[1])+len(deeplrr.split('\t')[0])-1)+'\t'+deeplrr.split('\t')[2]+'\tLRR\n'
                                fw.write(newdeeplrr)

                else:
                    fw.write(key.split('>')[1]+'\t'+'None\t'+'None\t'+'None\t'+'None\t'+'None\t'+'None\n')
            else:
                fw.write(key.split('>')[1]+'\t'+'None\t'+'None\t'+'None\t'+'None\t'+'None\t'+'None\n')
        else:
            fw.write(key.split('>')[1]+'\t'+'None\t'+'None\t'+'None\t'+'None\t'+'None\t'+'None\n')
    fw.close()


if __name__ == '__main__':
    input_path = sys.argv[1]
    Lscp = sys.argv[2]
    Ldcp = sys.argv[3]
    Lncp = sys.argv[4]
    output_path = sys.argv[5]
    allgroupsite = GroupSite(input_path)
    ShortPredict(allgroupsite, output_path, int(Lscp), int(Ldcp), int(Lncp))

