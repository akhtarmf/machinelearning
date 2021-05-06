# ChE 788 Assignment 4 Q2
# Mohammad Akhtar, 001209524

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


kernel = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])  
img = cv2.filter2D(image, -1, kernel)

fig1 = plt.figure(figsize=[12,8])
org = plt.imshow(image)

fig2 = plt.figure(figsize=[12,8])
filt = plt.imshow(img)

fig1.savefig('original.png', format = 'png')
fig2.savefig('filtered.png', format = 'png')

plt.show()