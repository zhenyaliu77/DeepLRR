#! /usr/bin/env python
#! -*-coding:utf-8 -*-
#! @Time   :2019/9/2 10:53
#! @Author :liuzhenya
#! @File   :plot_LRRNet.py.py
import matplotlib.pyplot as plt


def plot_history(train_accracy,train_loss,validation_accracy,validation_loss,acc_path,loss_path):
    # summarize history for accuracy
    plt.plot(train_accracy)
    plt.plot(validation_accracy)
    plt.title('LRRNet Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch Number')
    plt.legend(['Train', 'Validation'], loc='lower right')
    plt.savefig(acc_path)
    plt.show()


    # summarize history for loss
    plt.plot(train_loss)
    plt.plot(validation_loss)
    plt.title('LRRNet Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch Number')
    plt.legend(['Train', 'Validation'], loc='upper right')
    plt.savefig(loss_path)
    plt.show()

