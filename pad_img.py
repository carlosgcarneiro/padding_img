'''
Created by Carlos Augusto Guerra Carneiro
email: carlosgcarneyro@gmail.com

This code gets an image and makes another one doing a padding with zeros on the original image.
This is usefull when you need to compare some images with different dimentions.
'''

import cv2
import numpy as np

def pad_img(channel_array,w,h):
	zeros = np.zeros(w*h).reshape( (w,h) )
	zeros[:channel_array.shape[0], :channel_array.shape[1]] = channel_array
	return zeros

im = cv2.imread("icon.png")

height, width, channels = im.shape

height += 100  #size what you need to padding
width += 100

im_pad = np.zeros(shape=(height, width, channels))

for x in range(0, channels):
	im_pad[:,:,x] = pad_img(im[:,:,x],height, width)


cv2.imwrite( "aaaaaaaaaaa.jpg", im_pad ); #saving image
