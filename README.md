# DeepLRR
**An online webserver for leucine-rich-repeat containing protein characterization based on deep learning**

We introduce our method DeepLRR based on a convolutional neural network (CNN) model and LRR features, for predicting number and location of LRR unit in LRR proteins. We verified that the CNN model has a stronger ability to predict LRR units than the other three machine learning models (SVM, RF, NB). In order to better meet different research needs, we set three adjustable parameters (Lscp, Ldcp, Lncp) for DeepLRR based on LRR features. We compared DeepLRR to six existing methods on a dataset containing 874 LRR proteins, and DeepLRR outperformed the competing methods in overall F1-score. In addition, DeepLRR has integrated the pipeline of identifying plant disease-resistance proteins (NLR、RLK、RLP) and atypical domains

DeepLRR is available at http://lifenglab.hzau.edu.cn/DeepLRR   

![image](https://github.com/zhenyaliu77/DeepLRR/blob/master/deeplrr.png)

# DeepLRR-data
**This part contains all the raw data we used**   

- Data
  |File name | Introduction|
  |---|---|
  |LRRproteins_1748_swissprot.fasta  | Sequences of the LRR protein we ultimately retained|
  |LRRproteins_1849_swissprot.fasta  | All LRR protein sequences downloaded from Swiss-Prot database|
  |LRRproteins_874_compare.fasta | Comparison of DeepLRR and other software performance based on the test sample|
  |LRRproteins_874_parameter.fasta | Analyze the adjustable parameters of DeepLRR based on the test sample|
  |LRRunits_17388.txt  | The sequence of LRR units before using CD-Hit|
  |LRRunits_17388_information.txt  | The information of LRR units before using CD-Hit|
  |LRRunits_18039_information.txt  | The information of all LRR units in 1849 LRR proteins from Swiss-Prot database|
  |NOLRRproteins_174800_swissprot.fasta  | Protein sequences that don't contain LRR unit in the Swiss-Prot database|
  |negativesampledataset.txt | Negative samples used to train,validation and test the CNN model|
  |positivesampledataset.txt | Positive samples used to train,validation and test the CNN model|

# DeepLRR-CNN
**This part is designed to help interested parties quickly divide the training set,validation set and testing set, in addition to train a new CNN model of DeepLRR**

==To divide the training set,validation set and testing set==   

python ./split_train_val_test.py  ./positivesampledataset.txt  ./negativesampledataset.txt   

eg:  python split_train_val_test.py /home/lona/DeepLRR-CNN/data/LRR_10938.txt /home/lona/DeepLRR-CNN/data/NOLRR_10938.txt

==To train a new CNN model of DeepLRR==   

python ./main.py ./train.txt ./test.txt ./model   

eg:  python main.py /home/lona/DeepLRR-CNN/script/train.txt /home/lona/DeepLRR-CNN/script/test.txt /home/lona/DeepLRR-CNN/script/model

If you want to use the two commands successfully,you should make sure that your python version is above 3.5.x and torch has been installed   

Please manually change the parameter of the number of training set in train.py

============================================================================
# DeepLRR-1.01
**This part aims to predict the position,length and number of LRR units in the unknown protein sequence**

==To predict the position,length and number of LRR units in the unknown protein sequence==   

python ./DeepLRR.py ./input.fasta Lscp Ldcp Lncp current_path model_name   

eg:   python DeepLRR.py /home/lona/DeepLRR-1.01/demo/Q96FE5.fasta 4 9 3 /home/lona/DeepLRR-1.01 model-1.01.pt

============================================================================

# DeepLRR-pipeline

The DeepLRR-pipeline is an integrated tool for LRR domain searching. It's online version is available on http://lifenglab.hzau.edu.cn/DeepLRR. Here provides its portable version which can execute on local computers. This pipeline consists of four major parts, which is PfamScan, SignalP, TMHMM and our novel DeepLRR method. 

## 1.Prerequisites

DeepLRR-pipeline requires these software below: 

- Softwares
  1. Python3
  2. Perl5
  3. PfamScan
  4. hmmer
  5. SignalP
  6. TMHMM

- Python Packages
  1. torch
- Perl Packages
  1. Moose
  2. bioperl

## 2. Environment Configuration

### 2.1 Software configuration

Check Python and Perl environment in shell

```shell
python -V
perl -v
```

Then change directory into DeepLRR-pipeline using command

```shell
cd DeepLRR-pipeline/
```

Using the command to check software environment

```shell
python DeepLRR_Search.py -e
```

And the program will show the required software which is lacked, as is shown below

```
[ERROR] PfamScan not found, Please install it before LRR_Search, or check if its path has been add to $PATH!
[ERROR] SignalP not found, Please install it before LRR_Search, or check if its path has been add to $PATH!
[ERROR] TMHMM not found, Please install it before LRR_Search, or check if its path has been add to $PATH!
[ERROR] hmmer not found, Please install it before LRR_Search, or check if its path has been add to $PATH!
[ERROR] Pytorch have not installed yet, please install pytorch!
```

To make the software installation process easier, we have packed the software needed in `tools.tar.gz`, and a shell script `auto_deploy.sh` to deploy it, the four software can be easily deployed by the command:

```shell
bash auto_deploy.sh
```

When it finished, you can see the prompt "`Then input 'source ~/.bashrc' in the console to finish deployment!`", follow the prompt by the command

```shell
source ~/.bashrc
```

If Pytorch isn't installed, go to the [PyTorch](https://pytorch.org/)  website to get the installation command for your system environment.

After finished the steps above, go to the next step to check if these software is correctly configured.

### 2.2 Check software configuration

Then rerun the command below to check if the software is available

```shell
python DeepLRR_Search.py -e
```

If the ERROR message still exist, check the $PATH manually by

```shell
vi ~/.bashrc
```

or

```shell
echo $PATH
```

If there isn't any ERROR message shown, go to the next step.

### 2.3 PfamScan Configuration

PfamScan requires 2 perl modules: Moose and bioperl

The installation method is written in `tools/PfamScan/README`, follow its instruction and install the two modules.

After installation, you can check the installation by execute `pfam_scan.pl`, help message means the PfamScan is configured properly.

### 2.4 Pfam Database Download and Preparation

**[NOTICE] If you don't need the atypical domain search, you can skip this step!**

First change to the directory of HMM Store by the command

```shell
cd HMMs
```

 make the directory `atypical_HMM/` under the directory `HMMs/` for download

```shell
mkdir atypical_HMM
```

then use `wget` to download the Pfam-hmm file, here using Pfam-34.0 as example:

```shell
wget http://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam34.0/Pfam-A.hmm.gz
wget http://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam34.0/Pfam-A.hmm.dat.gz
```

After download, unzip them by the command

```shell
gunzip Pfam-A.hmm.gz Pfam-A.hmm.dat.gz
```

Last, use `hmmpress` to prepare the data for use

```shell
hmmpress Pfam-A.hmm
```

Four file named `Pfam-A.hmm.h3m`, `Pfam-A.hmm.h3i`, `Pfam-A.hmm.h3f`, `Pfam-A.hmm.h3p` will generated,  finished this step.

## 3.Usages

### 3.1 Usage info

You can look up the usage of DeepLRR-pipeline by the command

```shell
python DeepLRR-Search.py -h
```

The usages will be printed on the screen.

```
DeepLRR_Search is an integrated tool for LRR domain searching.
Usages: python DeepLRR_Search.py -f <input_file> -o <output_file> -d [domain_type] -m [model_name] [-a|h] <Lscp> <Ldcp> <Lncp>
  -d [domain type]      : the LRR domain you want to search [ NBS_LRR | LRR_RLK | LRR_RLP | LRR ]   *choose [LRR] will only run DeepLRR instead of the pipeline
  -f <input_file>       : assign input file
  -o <output_file>      : assign output file
  -m [model_name]       : assign version of DeepLRR model, 'model-1.01' is set for default
  -a --atypical         : search for atypical domain, have to assign domain type at the same time, when choosing [LRR] domain, this input will be ignored
  -h --help             : look for usages
  <Lscp> <Ldcp> <Lncp>  : assign parameter of DeepLRR Search
  -e --envcheck         : check environment dependenties
```

### 3.2 Usage examples

#### 3.2.1 LRR Domain Search

You can specify the parameters of DeepLRR

```shell
python DeepLRR_Search.py -f <input_file> -o <output_file> -d LRR -m [model_name] <Lscp> <Ldcp> <Lncp>
```

If parameters of DeepLRR is omitted, they will be set as default which are 4 9 3 for Lscp, Ldcp, Lncp respectively

```shell
python DeepLRR_Search.py -f <input_file> -o <output_file> -d LRR -m [model_name]
```

#### 3.2.2 NBS-LRR/LRR-RLP/LRR-RLP Domain Search

**\*\*When searching for these three domains, the input parameter setting will omitted and use default parameters instead.**

```shell
python DeepLRR_Search.py -f <input_file> -o <output_file> -d [ NBS_LRR | LRR_RLK | LRR_RLP ] -m [model_name]
```

#### 3.2.3 Atypical Domain Search

```shell
python DeepLRR_Search.py -f <input_file> -o <output_file> -d [ NBS_LRR | LRR_RLK | LRR_RLP ] -m [model_name] -a
```
