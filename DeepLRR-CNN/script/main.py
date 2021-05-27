#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/10/4 21:52
#! @Auther  :liuzhenya
#! @File    :main.py
from model import *
from input_matrix import *
from train import *
from plot_LRRNet import *
import torch
from torch.utils.data import DataLoader,TensorDataset
import sys


if __name__ == '__main__':
    train_path = sys.argv[1] 
    #The path of training set
    test_path = sys.argv[2] 
    #The path of testing set
    model_dir = sys.argv[3] 
    #The folder that saves nn models
    trainlrr_x, trainlrr_y = aa_dataset(train_path)
    testlrr_x, testlrr_y = aa_dataset(test_path)

    torch_trainx = torch.from_numpy(trainlrr_x).float()
    torch_trainy = torch.from_numpy(trainlrr_y).float()
    inittrain_dataset = TensorDataset(torch_trainx, torch_trainy)
    train_loader = DataLoader(dataset=inittrain_dataset,
                              batch_size=128,
                              shuffle=True
                              )

    torch_valx = torch.from_numpy(testlrr_x).float()
    torch_valy = torch.from_numpy(testlrr_y).float()
    initval_dataset = TensorDataset(torch_valx, torch_valy)
    test_loader = DataLoader(dataset=initval_dataset,
                                   batch_size=1,
                                   shuffle=False
                                   )
    LRRNet = LRRCNN()
    LRRNet = LRRNet.float()
    train_accracy, train_loss, test_accracy, test_loss = train(train_loader, test_loader, LRRNet,0.001, 51, 1, 137, 1370,model_dir)
    plot_history(train_accracy, train_loss, test_accracy, test_loss,model_dir+'/accracy.pdf',model_dir+'/loss.pdf')


    #5-fold cross validation
'''for i in range(1,6):
        trainlrr_x,trainlrr_y = aa_dataset('D:/LRRNet/relife/data/cdhit/norandom_dataset/data/train_cv'+str(i)+'.txt')
        vallrr_x,vallrr_y = aa_dataset('D:/LRRNet/relife/data/cdhit/norandom_dataset/data/val_cv'+str(i)+'.txt')
        #trainlrr_x, trainlrr_y = aa_dataset('D:/LRRNet/relife/data/cdhit/norandom_dataset/train_initial.txt')
        #vallrr_x,vallrr_y = aa_dataset('D:/LRRNet/relife/data/cdhit/norandom_dataset/data/test_initial.txt')

        torch_trainx = torch.from_numpy(trainlrr_x).float()
        torch_trainy = torch.from_numpy(trainlrr_y).float()
        inittrain_dataset = TensorDataset(torch_trainx,torch_trainy)
        train_loader = DataLoader(dataset = inittrain_dataset,
                                batch_size = 128,
                                shuffle = True
                                )

        torch_valx = torch.from_numpy(vallrr_x).float()
        torch_valy = torch.from_numpy(vallrr_y).float()
        initval_dataset = TensorDataset(torch_valx,torch_valy)
        validation_loader = DataLoader(dataset = initval_dataset,
                                batch_size = 1,
                                shuffle = False
                                )

        LRRNet = LRRCNN()
        LRRNet = LRRNet.float()
        train_accracy,train_loss,validation_accracy,validation_loss = train(train_loader,validation_loader,LRRNet,0.001,51,1,109,1090,'D:/LRRNet/relife/data/cdhit/norandom_dataset/model/new-1-multi-1-0.001/model_'+str(i)+'_LRRNet')
        plot_history(train_accracy,train_loss,validation_accracy,validation_loss,'D:/LRRNet/relife/data/cdhit/norandom_dataset/model/new-1-multi-1-0.001/model_'+str(i)+'_LRRNet/accracy.pdf','D:/LRRNet/relife/data/cdhit/norandom_dataset/model/new-1-multi-1-0.001/model_'+str(i)+'_LRRNet/loss.pdf')



    #模型在测试集上的表现
    testlrr_x,testlrr_y = aa_dataset('D:/LRRNet/relife/data/cdhit/norandom_dataset/data/test_initial.txt')
    LRRNet = LRRCNN()
    LRRNet = LRRNet.float()
    LRRNet.load_state_dict(torch.load('D:/LRRNet/relife/data/cdhit/norandom_dataset/model/1CNN-multiscalefilter-1fullconnect/model_5_LRRNet/best_steps_2180.pt'))

    torch_testx = torch.from_numpy(testlrr_x).float()
    torch_testy = torch.from_numpy(testlrr_y).float()
    inittest_dataset = TensorDataset(torch_testx,torch_testy)

    test_loader = DataLoader(dataset = inittest_dataset,
                              batch_size = 1,
                              shuffle = False
                              )


    def test(test_loader,model):
        model.eval()
        count = 0
        corrects = 0
        avg_loss = 0
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        loss_fuc = nn.BCELoss()
        for i,batch in enumerate(test_loader):
            test_x,test_y = batch
            predict_y = model(test_x)
            loss = loss_fuc(predict_y,test_y)
            avg_loss += loss.item()
            if int(torch.max(test_y.data, 1)[1][0]) == 0:    #positive samples
                if torch.max(predict_y, 1)[1] == torch.max(test_y.data, 1)[1]:
                    tp += 1
                else:
                    fn += 1
            else:
                if torch.max(predict_y, 1)[1] == torch.max(test_y.data, 1)[1]:
                    tn += 1
                else:
                    fp += 1
            corrects += (torch.max(predict_y, 1)[1] == torch.max(test_y.data, 1)[1]).sum().data.numpy()
            count += 1
        acc = (tp+tn)/(tp+tn+fp+fn)
        pre = tp/(tp+fp)
        rec = tp/(tp+fn)
        spe = tn/(tn+fp)
        f1 = 2*pre*rec/(pre+rec)
        mcc = (tp*tn-fp*fn)/(((tn+fn)*(tn+fp)*(tp+fn)*(tp+fp))**0.5)
        size = len(test_loader.dataset)
        avg_loss /= count
        accuracy = corrects / size
        print('\nTest - loss: {:.6f}  acc: {:.4f}({}/{}) \n'.format(avg_loss,
                                                                      accuracy,
                                                                      corrects,
                                                                      size))
        print('acc '+str(acc))
        print('pre '+str(pre))
        print('rec '+str(rec))
        print('spe '+str(spe))
        print('f1 '+str(f1))
        print('mcc '+str(mcc))
    test(test_loader,LRRNet)'''
