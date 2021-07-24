DeepLRR Pipeline 1.0 by Zirui Ren (renzirui@webmail.hzau.edu.cn)

==Usages==

This Pipeline includes 2 steps with 3 available proteins for identification:

STEP-1 Protein Identification:

For NBS-LRR Protein:
>python NBS_LRR.py <fasta> <resultfile>

For LRR-RLP Protein:
>python LRR_RLP_RLK.py <fasta> <resultfile>

For LRR-RLK Protein:
>python LRR_RLP_RLK.py -k <fasta> <resultfile>

    <fasta>  Filename of the fasta file to submit
    <resultfile> The file to record result


STEP-2 Atypia Domain Identification:

>python atypia.py <fasta> <resultfile> <protein type>

    <fasta>  Filename of the fasta file to submit
    <resultfile> The file to record result
    <protein type> The type of the protein, only three proteins available
    	NBS_LRR
    	LRR_RLP
    	LRR_RLK
    
**usage eg. >python atypia.py *.fa *.txt NBS_LRR

==Used Softwares==
1.Pfam_Scan w/ Pfam33.1 database
2.TMHMM 2.0b (*it has updated to 2.0c for now)
3.SignalP-5.0
4.DeepLRR
5.COILS
