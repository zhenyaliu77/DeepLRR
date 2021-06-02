#!/usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time    :2020/10/4 21:49
#! @Auther  :liuzhenya
#! @File    :model.py
import torch
import torch.nn as nn


class LRRCNN(nn.Module):
    def __init__(self):
        super(LRRCNN,self).__init__()
        self.conv1 = nn.Sequential(                          #30x5
            nn.Conv2d(1,128,kernel_size=(2,5),stride=1),     #29x1
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2,1),stride=2)             #14x1
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(1, 128, kernel_size=(4, 5), stride=1),  # 27x1
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2, 1), stride=2)        # 13x1
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(1, 128, kernel_size=(8, 5), stride=1),  # 23x1
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2, 1), stride=2)        # 11x1
        )
        self.layer = nn.Sequential(
            nn.Linear(in_features=128 * 39 * 1, out_features=128),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(in_features=128, out_features=2),
            nn.Softmax(dim=1)
        )

    def forward(self,x):
        conv1_out = self.conv1(x)
        conv1_out = conv1_out.view(conv1_out.size(0), -1)
        #print(conv1_out.shape)
        conv2_out = self.conv2(x)
        conv2_out = conv1_out.view(conv2_out.size(0), -1)
        #print(conv2_out.shape)
        conv3_out = self.conv3(x)
        conv3_out = conv3_out.view(conv3_out.size(0), -1)
        #print(conv3_out.shape)
        final_out = torch.cat((conv1_out,conv2_out),1)
        final_out = torch.cat((final_out, conv3_out), 1)
        out = self.layer(final_out)
        return out