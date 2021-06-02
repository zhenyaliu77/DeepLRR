#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/10/4 21:51
#! @Auther  :liuzhenya
#! @File    :train.py
import os
import sys
import torch
import torch.nn as nn

def train(train_loader,validation_loader,model,lr,epoch,log_interval,test_interval,early_stopping,save_dir):#,weight_decay):
    optimizer = torch.optim.Adam(model.parameters(),lr=lr)#,weight_decay=weight_decay)
    loss_fuc = nn.BCELoss()
    steps = 0
    best_acc = 0
    last_step = 0
    train_accracy = []
    train_loss = []
    validation_accracy = []
    validation_loss = []
    model.train()
    for epoch in range(0,epoch):
        avg_loss = 0
        avg_corrects = 0
        for i,batch in enumerate(train_loader):
            train_x,train_y = batch
            optimizer.zero_grad()
            predict_y = model(train_x)
            loss = loss_fuc(predict_y,train_y)
            avg_loss += loss.item()
            loss.backward()
            optimizer.step()
            steps += 1
            if steps % log_interval == 0:
                corrects = (torch.max(predict_y, 1)[1] == torch.max(train_y.data, 1)[1]).sum().data.numpy()
                avg_corrects += corrects
                train_acc = corrects / train_y.size()[0]
                sys.stdout.write(
                    '\rBatch[{}] - loss: {:.6f}  acc: {:.4f}({}/{})'.format(steps,
                                                                             loss.item(),
                                                                             train_acc,
                                                                             corrects,
                                                                             train_y.size()[0])
                )
            if steps % test_interval == 0:
                validation_acc,validation_los = validation(validation_loader,model)
                validation_accracy.append(validation_acc)
                validation_loss.append(validation_los)
                train_loss.append(avg_loss/test_interval)
                train_accracy.append(avg_corrects/13928)  #13928 109/17464 137
                if validation_acc > best_acc:
                    best_acc = validation_acc
                    last_step = steps
                    if True:
                        print('Saving best model, acc: {:.4f}\n'.format(best_acc))
                        save(model, save_dir, 'best', steps)
                else:
                    if steps - last_step >= early_stopping:
                        print('\nearly stop by {} steps, acc: {:.4f}'.format(early_stopping, best_acc))

    return train_accracy,train_loss,validation_accracy,validation_loss

def validation(validation_loader,model):
    model.eval()
    count = 0
    corrects = 0
    avg_loss = 0
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    loss_fuc = nn.BCELoss()
    for i,batch in enumerate(validation_loader):
        val_x,val_y = batch
        predict_y = model(val_x)
        loss = loss_fuc(predict_y,val_y)
        avg_loss += loss.item()
        if int(torch.max(val_y.data, 1)[1][0]) == 0:  # positive samples
            if torch.max(predict_y, 1)[1] == torch.max(val_y.data, 1)[1]:
                tp += 1
            else:
                fn += 1
        else:
            if torch.max(predict_y, 1)[1] == torch.max(val_y.data, 1)[1]:
                tn += 1
            else:
                fp += 1
        corrects += (torch.max(predict_y, 1)[1] == torch.max(val_y.data, 1)[1]).sum().data.numpy()
        count += 1
    acc = (tp + tn) / (tp + tn + fp + fn)
    pre = tp / (tp + fp)
    rec = tp / (tp + fn)
    spe = tn / (tn + fp)
    f1 = 2 * pre * rec / (pre + rec)
    mcc = (tp*tn-fp*fn)/(((tn+fn)*(tn+fp)*(tp+fn)*(tp+fp))**0.5)
    size = len(validation_loader.dataset)
    avg_loss /= count
    accuracy = corrects / size
    print('\nEvaluation - loss: {:.6f}  acc: {:.4f}({}/{}) \n'.format(avg_loss,
                                                                           accuracy,
                                                                           corrects,
                                                                           size))
    print('acc ' + str(acc))
    print('pre ' + str(pre))
    print('rec ' + str(rec))
    print('spe ' + str(spe))
    print('f1 ' + str(f1))
    print('mcc ' + str(mcc))
    return accuracy,avg_loss

def save(model,save_dir,save_prefix,steps):
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    save_prefix = os.path.join(save_dir,save_prefix)
    save_path = '{}_steps_{}.pt'.format(save_prefix,steps)
    torch.save(model.state_dict(),save_path)

