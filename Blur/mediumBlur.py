#!/usr/bin/env python
# -*- coding:utf-/ -*-
__author__ = '&USER'
import cv2
import numpy as np


def medianNum(mat, idx_i, idx_j, scope, hatchway):
    arr = []
    for i in range(int(idx_i - scope), int(idx_i + scope + 1)):
        for j in range(int(idx_j - scope), int(idx_j + scope + 1)):
            arr.append(mat[i][j][hatchway])
    arr = sorted(arr)
    arr = np.array(arr)
    scope = scope * 2 + 1
    return arr[int(scope * scope / 2)]


img = cv2.imread('img/flower.jpg')
img_data = np.array(img)
img_output = np.array(img)
row = len(img_data)
column = len(img_data[0])
area_scope = 3
line_scope = (area_scope - 1) / 2
for i in range(row):
    for j in range(column):
        if line_scope <= i < row - line_scope and line_scope <= j < column - line_scope:
            for k in range(3):
                img_output[i][j][k] = medianNum(img_data, i, j, line_scope, k)
img_median = cv2.medianBlur(img, 3)
cv2.imshow('flower', img)
cv2.imshow('medianBlur', img_median)
cv2.imshow('medianBlur2', img_output)
cv2.waitKey(0)
