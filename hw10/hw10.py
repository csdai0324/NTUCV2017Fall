import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
%matplotlib inline

def convolve(A, B):
    assert A.shape == B.shape
    value = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            value += (A[i, j] * B[B.shape[0] - i - 1, B.shape[1] - j - 1])
    return value

def laplace_mask1(img, kerenl, threshold):
    height, width = img.size
    new_img = np.empty(shape=(height, width))
    img = np.asarray(img)
    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])
    for i in range(width):
        for j in range(height):
            if convolve(img[i:i+kernel.shape[0], j:j+kernel.shape[1]], kernel) >= threshold:
                new_img[i][j] = convolve(img[i:i+kernel.shape[0], j:j+kernel.shape[1]], kernel)
    return new_img.astype('uint8') 

def laplace_mask2(img, kerenl, threshold):
    height, width = img.size
    new_img = np.empty(shape=(height, width))
    img = np.asarray(img)
    kernel = np.array([[1., 1, 1],
                       [1, -8, 1],
                       [1, 1, 1]]) / 3
    for i in range(width):
        for j in range(height):
            if convolve(img[i:i+kernel.shape[0], j:j+kernel.shape[1]], kernel) >= threshold:
                new_img[i][j] = convolve(img[i:i+kernel.shape[0], j:j+kernel.shape[1]], kernel)
    return new_img.astype('uint8')

def laplace_gaussian(img, kerenl, threshold):
    height, width = img.size
    new_img = np.empty(shape=(height, width))
    img = np.asarray(img)
    kernel = np.array([[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0],
                       [0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
                       [0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
                       [-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
                       [-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
                       [-2, -9, -23, -1, 103, 178, 103, -1, -23, -9, -2],
                       [-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
                       [-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
                       [0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
                       [0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
                       [0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0]])
    for i in range(width):
        for j in range(height):
            if convolve(img[i:i+kernel.shape[0], j:j+kernel.shape[1]], kernel) >= threshold:
                new_img[i][j] = convolve(img[i:i+kernel.shape[0], j:j+kernel.shape[1]], kernel)
    return new_img.astype('uint8')

def difference_gaussian(img, kerenl, threshold):
    height, width = img.size
    new_img = np.empty(shape=(height, width))
    img = np.asarray(img)
    kernel = np.array([[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1],
                       [-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
                       [-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
                       [-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
                       [-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
                       [-8, -13, -17, 15, 160, 283, 160, 15, -17, -13, -8],
                       [-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
                       [-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
                       [-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
                       [-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
                       [-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1]])

    for i in range(width):
        for j in range(height):
            if convolve(img[i:i+kernel.shape[0], j:j+kernel.shape[1]], kernel) >= threshold:
                new_img[i][j] = convolve(img[i:i+kernel.shape[0], j:j+kernel.shape[1]], kernel)
    return new_img.astype('uint8')