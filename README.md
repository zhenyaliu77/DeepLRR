# DeepLRR
**An online webserver for leucine-rich-repeat containing protein characterization based on deep learning**

We introduce our method DeepLRR based on a convolutional neural network (CNN) model and LRR features, for predicting number and location of LRR unit in LRR proteins. We compared DeepLRR to six existing methods on a dataset containing 874 LRR proteins, and DeepLRR outperformed the competing methods in overall F1-score. In addition, DeepLRR has integrated the pipeline of identifying plant disease-resistance proteins (NLR、RLK、RLP) and atypical domains

DeepLRR is available at http://lifenglab.hzau.edu.cn/DeepLRR

============================================================================
# DeepLRR-data
**This part contains all the raw data we used**   

LRRproteins_1748_swissprot.fasta--------------Sequences of the LRR protein we ultimately retained

LRRproteins_1849_swissprot.fasta--------------All LRR protein sequences downloaded from Swiss-Prot database

LRRproteins_874_compare.fasta-----------------Comparison of DeepLRR and other software performance based on the test sample

LRRproteins_874_parameter.fasta---------------Analyze the adjustable parameters of DeepLRR based on the test sample

LRRunits_17388.txt----------------------------The sequence of LRR units before using CD-Hit

LRRunits_17388_information.txt----------------The information of LRR units before using CD-Hit

LRRunits_18039_information.txt----------------The information of all LRR units in 1849 LRR proteins from Swiss-Prot database

NOLRRproteins_174800_swissprot.fasta----------Protein sequences that don't contain LRR unit in the Swiss-Prot database

negativesampledataset.txt---------------------Negative samples used to train,validation and test the CNN model

positivesampledataset.txt---------------------Positive samples used to train,validation and test the CNN model

============================================================================
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


