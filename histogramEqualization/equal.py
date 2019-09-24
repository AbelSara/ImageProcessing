#!/usr/bin/env python
# -*- coding:utf-/ -*-
__author__ = '&USER'
import cv2
import numpy as np

pollen = cv2.imread('img/pollen.jpg')
pollen = np.array(cv2.cvtColor(pollen, cv2.COLOR_RGB2GRAY))

row, column = pollen.shape
max = row * column
L = 256
flag = np.zeros(L)
for i in range(row):
    for j in range(column):
        flag[pollen[i][j]] += 1
for i in range(row):
    for j in range(column):
        temp = 0
        for k in range(int(pollen[i][j])):
            temp += flag[k]
        pollen[i][j] = (L - 1) * temp / max
cv2.imshow('histogramEqual', pollen)
cv2.waitKey(0)
