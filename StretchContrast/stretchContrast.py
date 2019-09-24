#!/usr/bin/env python
# -*- coding:utf-/ -*-
__author__ = '&USER'
import cv2
import numpy as np

min = 0
max = 255

img = cv2.imread('img/pollen.jpg')
img = np.array(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
imin = img.min()
imax = img.max()
delta = imax - imin
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i][j] = (max - min) * (img[i][j] - imin) / delta
cv2.imshow('pollen', img)
cv2.waitKey(0)
