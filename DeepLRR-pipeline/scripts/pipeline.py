# encoding: utf-8
"""
@author: ZiRui Ren
@contact: 1131061444@qq.com/renzirui@webmail.hzau.edu.cn
@time: 2020/12/3 22:48
@file: NBS_LRR.py
@desc:
"""
import os
import re
from random import randint

def read_fasta(fasta_file):
    with open(fasta_file, 'r') as f:
        fasta_list = []
        data = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                fasta_list.append(data)
                words = line.split()
                data = [words[0][1:], '']
            else:
                sequence = line
                data[1] = data[1] + sequence
    fasta_list.append(data)
    fasta_list.pop(0)
    return fasta_list


def rewrite_fasta(fasta_file, seqid):
    fasta_list = read_fasta(fasta_file)
    with open(fasta_file, 'w') as fasta:
        for i in fasta_list:
            if i[0] in seqid:
                fasta.write('>' + i[0] + '\n' + i[1] + '\n')


def id_read(table):
    seqid = set()
    for record in table:
        seqid.add(record[0])
    return seqid


def pfam_process_atypia(result_file, output_file, pro_type):
    tmp = r'temp_' + str(randint(1, 99999999))
    try:
        open(result_file)
    except:
        print('[ERROR] PfamScan result not exist! Check your Pfam configuration or path permission!')
        print('Session Terminated!')
        quit()
    with open(result_file) as fin:
        with open(tmp, 'w') as fout:
            fout.writelines(line for i, line in enumerate(fin) if i > 27)
    exclude = []
    with open(r'/home/lifeng/DeepLRR/exclusion/'+pro_type+r'.txt') as fin:
        exclude = [line.rstrip('\n') for line in fin.readlines()]
    table = []
    with open(tmp) as ftable:
        for line in ftable:
            value = line.split()
            if value[6] not in exclude:
                table.append([value[0], str(eval(value[2] + '-' + value[1]) + 1) + 'aa', value[1], value[2], value[6],r'Pfam_Scan'])
    os.system('rm '+tmp)
    with open(output_file, 'w') as out:
        out.write('ProteinID\tLength\tStart\tEnd\tDomain\tTool\n')
        for record in table:
            out.write('\t'.join(record) + '\n')


def pfam_process_pkinase(result_file, fastafile):
    tmp = r'temp_' + str(randint(1, 99999999))
    fastalist = read_fasta(fastafile)
    try:
        open(result_file)
    except:
        print('[ERROR] PfamScan result not exist! Check your Pfam configuration or path permission!')
        print('Session Terminated!')
        quit()

    with open(result_file) as fin:
        with open(tmp, 'w') as fout:
            fout.writelines(line for i, line in enumerate(fin) if i > 27)
    table = []
    with open(tmp) as ftable:
        for line in ftable:
            value = line.split()
            table.append([value[0], str(eval(value[2] + '-' + value[1])+1) + 'aa', value[1], value[2], value[6],r'Pfam_Scan'])
    pk_seqid = id_read(table)
    os.system('rm '+tmp)
    nopk_seqid = set()
    for data in fastalist:
        if data[0] not in pk_seqid:
            nopk_seqid.add(data[0])
    return table, pk_seqid, nopk_seqid


def pfam_process_nbslrr(result_file, fastafile):
    tmp = r'temp_' + str(randint(1,99999999))
    # print('temporary file ',tmp,' generated')
    try:
        open(result_file)
    except:
        print('[ERROR] PfamScan result not exist! Check your Pfam configuration or path permission!')
        print('Session Terminated!')
        quit()

    with open(result_file) as fin:
        try:
            with open(tmp, 'w') as fout:
                fout.writelines(line for i, line in enumerate(fin) if i > 27)
        except:
            print('IO Error!')
            exit()
    NB_ARC_table = []
    CC_table = []
    TIR_table = []
    with open(tmp) as ftable:
        for line in ftable:
            value = line.split()
            if value[6] == 'NB-ARC':
                NB_ARC_table.append(
                [value[0], str(eval(value[2] + '-' + value[1])+1) + 'aa', value[1], value[2], value[6], 'Pfam_Scan'])
            elif value[6] == 'CC':
                CC_table.append(
                [value[0], str(eval(value[2] + '-' + value[1])+1) + 'aa', value[1], value[2], value[6], 'Pfam_Scan'])
            elif value[6] == 'TIR':
                TIR_table.append(
                [value[0], str(eval(value[2] + '-' + value[1])+1) + 'aa', value[1], value[2], value[6], 'Pfam_Scan'])
    os.system('rm '+tmp)
    # print('temporary file ',tmp,' removed')
    NB_ARC_id = id_read(NB_ARC_table)
    CC_id = id_read(CC_table)
    TIR_id = id_read(TIR_table)
    id_last = NB_ARC_id & (CC_id | TIR_id)
    rewrite_fasta(fastafile, id_last)
    if not len(id_last):
        return False, False
    for table in [NB_ARC_table, CC_table, TIR_table]:
        for record in table:
            if record[0] not in id_last:
                table.remove(record)
    return [CC_table, TIR_table, NB_ARC_table], id_last


def signalp_process(result_file, fasta_file):
    tmp = r'temp_' + str(randint(1,99999999))
    try:
        open(result_file)
    except:
        print('[ERROR] SignalP result not exist! Check your SignalP configuration or work directory permission!')
        print('Session Terminated!')
        quit()

    with open(result_file, 'r') as fin:
        with open(tmp, 'w') as fout:
            fout.writelines(line for i, line in enumerate(fin) if i > 0)
    table = []
    with open(tmp) as ftable:
        for line in ftable:
            value = line.split()
            if value[1] == r'SP(Sec/SPI)':
                table.append([value[0], 'N/A', 'N/A', 'N/A', 'SP', 'signalp-5.0b'])
    os.system('rm '+tmp)
    sp_seqid = id_read(table)
    rewrite_fasta(fasta_file, sp_seqid)

    return table, sp_seqid


def tmhmm_process(result_file, fasta_file):
    tm_seqid = set()
    table = []
    try:
        open(result_file)
    except:
        print('[ERROR] TMHMM result not exist! Check your TMHMM configuration or path permission!')
        print('Session Terminated!')
        quit()

    with open(result_file) as result:
        regexp1 = re.compile(r'predicted')
        for line in result:
            if re.search(regexp1, line, flags=0):
                l = line.split()
                if l[6] != '0':
                    tm_seqid.add(l[1])
    with open(result_file) as result:
        regexp1 = re.compile(r'TMhelix')
        for line in result:
            l = line.split()
            if re.search(regexp1, line, flags=0) and l[0] in tm_seqid:
                temp = [l[0], str(eval(l[4] + '-' + l[3]) + 1) + 'aa', l[3], l[4], 'TM', 'tmhmm2.0c']
                table.append(temp)
    rewrite_fasta(fasta_file, tm_seqid)
    return table, tm_seqid


def deeplrr_process(result_file):
    table = []
    lrr_seqid = set()
    try:
        open(result_file)
    except:
        print('[ERROR] DeepLRR result not exist! Check your path permission!')
        print('Session Terminated!')
        quit()

    with open(result_file) as fout:
        for line in fout:
            if line.startswith('Protein ID'):
                continue
            else:
                record = line.split()
                if record[1] == 'None':
                    continue
                seqid = record[0]
                table.append([seqid, record[2] + 'aa', record[3], record[4], 'LRR', 'DeepLRR'])
                lrr_seqid.add(seqid)
    return table, lrr_seqid


def write_domain(seqid, table, outputfile):
    outstr = ''
    for domain in table:
    	if domain[0] in seqid:
            outstr += ('\t'.join(domain)+'\n')     
    with open(outputfile, 'a') as out:
        out.write(outstr)


def output_lrr_rlpk(nopk_seqid, pk_seqid, sp_seqid, tm_seqid, lrr_seqid, pk_table,sp_table, tm_table, lrr_table,
                    output, multi=False, kinase=False):
    head = 'ProteinID\tLength\tStart\tEnd\tDomain\tTool\n'
    with open(output,'a') as result:
    	result.write(head)
    thereis = True
    if kinase:
        selected_seqid = pk_seqid & sp_seqid & tm_seqid & lrr_seqid
        #print(selected_seqid)
    else:
        selected_seqid = nopk_seqid & sp_seqid & tm_seqid & lrr_seqid
    if not len(selected_seqid):
        thereis = False
    if kinase:
        write_domain(selected_seqid, pk_table, output)
    for table in [sp_table, tm_table, lrr_table]:
        write_domain(selected_seqid, table, output)
    if multi:
        with open(output, 'a') as result:
            if kinase:
                result.write('\n'+'Potential LRR-RLK Proteins:'+'\n')
            else:
                result.write('\n'+'Potential LRR-RLP Proteins:'+'\n')
            result.writelines([seqid+'\n' for seqid in selected_seqid])
    return thereis


def output_nbs_lrr(integrated_seqid, lrr_seqid, table_integrated, lrr_table, output, multi=False):
    head = 'ProteinID\tLength\tStart\tEnd\tDomain\tTool\n'
    with open(output,'a') as result:
    	result.write(head)
    thereis = True
    selected_seqid = integrated_seqid & lrr_seqid
    if not len(selected_seqid):
        thereis = False
    for table in table_integrated:
        #print(table)
        write_domain(selected_seqid, table, output)
    for table in [lrr_table]:
    	#print(table)
    	write_domain(selected_seqid, table, output)
    if multi:
        with open(output, 'a') as result:
            result.write('\n'+'Potential NBS-LRR Proteins:'+'\n')
            result.writelines([seqid+'\n' for seqid in selected_seqid])
    return thereis


if __name__ == '__main__':
    print("Don't call it as main!")
