#!/usr/bin/env python
# -*- coding:utf-/ -*-
__author__ = '&USER'
import cv2
import numpy as np

img = cv2.imread('img/hide.jpg')
img = np.array(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
dim = 3
partDim = np.power(dim, 2)
L = 256
row, column = img.shape
for i in range(int(dim / 2), row - int(dim / 2)):
    for j in range(int(dim / 2), column - int(dim / 2)):
        flag = np.zeros(L)
        temp = 0
        for dim_i in range(i - int(dim / 2), i + int(dim / 2)):
            for dim_j in range(j - int(dim / 2), j + int(dim / 2)):
                flag[img[dim_i][dim_j]] += 1
        for k in range(img[i][j]):
            temp += flag[k]
        img[i][j] = (L - 1) * temp / partDim
cv2.imshow('partHisEqual', img)
cv2.waitKey(0)
