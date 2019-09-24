#!/usr/bin/env python
# -*- coding:utf-/ -*-
__author__ = '&USER'

import numpy as np
import cv2

rh = 2
rl = 0.25
c = 1
D0 = 100

img = cv2.imread('img/bone.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.array(img)
row = len(img)
column = len(img[0])

P = 2 * row
Q = 2 * column

img_ln = np.log(img + np.ones((row, column)))  # 求对数，方便下一步进行傅里叶变换

img_mid = np.zeros((P, Q))
for i in range(row):
    for j in range(column):
        img_mid[i][j] = img_ln[i][j] * np.power(-1, i + j)

img_fft = np.fft.fft2(img_mid)  # 傅里叶变换

img_homo = np.zeros((P, Q))
a = np.square(D0)
r = rh - rl
for i in range(P):
    for j in range(Q):
        temp = np.square(i - (row + 1)) + np.square(j - (column + 1))
        img_homo[i][j] = (r * (1 - np.exp((-c) * (temp / a))) + rl) * img_fft[i][j]  # 使用滤波器H(u,v)进行滤波

img_ifft = np.fft.ifft2(img_homo)  # 反傅里叶变换
img_exp = np.zeros((row, column))
for i in range(row):
    for j in range(column):
        img_ifft[i][j] = img_ifft[i][j] * np.power(-1, i + j)
        img_exp[i][j] = np.exp(img_ifft[i][j]) - 1  # 指数运算，对数的逆运算
max = img_exp.max()
min = img_exp.min()
minus = max - min
for i in range(row):
    for j in range(column):
        img_exp[i][j] = 255 * (img_exp[i][j] - min) / minus  # 归一化后恢复值
cv2.imshow('homoBlur', img_exp)
cv2.waitKey(0)
