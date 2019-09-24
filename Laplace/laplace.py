#!/usr/bin/env python
# -*- coding:utf-/ -*-
__author__ = '&USER'
import cv2
import numpy as np
from PIL import Image
import math

img = cv2.imread('img/moon.jpg')
img = np.array(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
laplace = np.zeros(img.shape)
laplace = laplace.astype(np.uint8)
row, column = img.shape
# 自定义laplace算子
for i in range(1, row - 1):
    for j in range(1, column - 1):
        laplace[i][j] = math.fabs(
            8 * img[i][j] - img[i - 1][j] - img[i][j - 1] - img[i][j + 1] - img[i + 1][j] - img[i + 1][j + 1] -
            img[i + 1][j - 1] - img[i - 1][j - 1] - img[i - 1][j + 1])
output = Image.fromarray(np.zeros(laplace.shape))
output = img + laplace
gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(gray_lap)  # opencv中laplace算子
cv2.imshow('originalDrawing', img)
cv2.imshow('laplace', laplace)
cv2.imshow('output', output)
cv2.imshow('cv', dst)
cv2.waitKey(0)
