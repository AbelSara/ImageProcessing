#!/usr/bin/env python
# -*- coding:utf-/ -*-
__author__ = '&USER'
import cv2
import numpy as np

img = np.array(cv2.imread('img/dollar.jpg'))
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('dollor', img)
row, column = img.shape
outputImg = np.zeros((8, row, column))
for i in range(row):
    for j in range(column):
        base = 1
        for k in range(8):
            if base == (base & img[i][j]):
                outputImg[k][i][j] = 1
            base = base << 1
for i in range(8):
    cv2.imshow('bit' + str(1 + i), outputImg[i])
reshow = np.zeros(img.shape)
for i in range(8):
    reshow = reshow + outputImg[i] * np.power(2, i)
reshow = reshow.astype(np.uint8)
cv2.imshow('reshow', reshow)
cv2.waitKey(0)
