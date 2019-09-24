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
(row, column) = img.shape

P = 2 * row
Q = 2 * column

img_ln = np.log(img + np.ones((row, column)))  # 求对数，方便下一步进行傅里叶变换
img_mid = np.zeros((P, Q))
for i in range(row):
    for j in range(column):
        img_mid[i][j] = img_ln[i][j]  # 图像长宽分别扩大两倍，填充0
img_fft = np.fft.fft2(img_mid)  # 傅里叶变换

Homo = np.zeros((P, Q))
a = np.square(D0)
r = rh - rl
for i in range(P):
    for j in range(Q):
        temp = np.square(i - row) + np.square(j - column)
        Homo[i][j] = r * (1 - np.exp((-c) * (temp / a))) + rl  # 滤波器H(u,v)
Homo = np.fft.ifftshift(Homo)  # 滤波器去中心化
img_ifft = np.fft.ifft2(np.multiply(Homo, img_fft))  # 对滤波器和傅里叶变换后的mat按位相乘
img_exp = np.zeros((row, column))
for i in range(row):
    for j in range(column):
        img_exp[i][j] = np.exp(img_ifft[i][j]) - 1  # 指数运算，对数的逆运算
max = img_exp.max()
min = img_exp.min()
minus = max - min
for i in range(row):
    for j in range(column):
        img_exp[i][j] = 255 * (img_exp[i][j] - min) / minus  # 归一化后恢复值
cv2.imshow('homoBlur', img_exp)
cv2.waitKey(0)
