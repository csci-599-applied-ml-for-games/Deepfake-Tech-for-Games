
#--------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from PIL import Image

with open('/Users/dingding/Desktop/data/labels.txt') as file:
	labels = file.read().split('\n')
	for line in labels:
		line = line.split(' ')
		for i in range(1, len(line)):
			line[i] = float(line[i])
		plt.figure()
		print(line[0])
		img = Image.open('/Users/dingding/Desktop/data/' + line[0])
		plt.imshow(img)
		plt.plot([line[1], line[1]], [line[2], line[4]], color = 'red', linestyle = '-', linewidth = '2')
		plt.plot([line[3], line[3]], [line[2], line[4]], color = 'red', linestyle = '-', linewidth = '2')
		plt.plot([line[1], line[3]], [line[2], line[2]], color = 'red', linestyle = '-', linewidth = '2')
		plt.plot([line[1], line[3]], [line[4], line[4]], color = 'red', linestyle = '-', linewidth = '2')
		plt.plot(line[5], line[6], marker = 'o', markersize = 5, color = 'red')
		plt.plot(line[7], line[8], marker = 'o', markersize = 5, color = 'red')
		plt.plot(line[9], line[10], marker = 'o', markersize = 5, color = 'red')
		plt.plot(line[11], line[12], marker = 'o', markersize = 5, color = 'red')
		plt.plot(line[13], line[14], marker = 'o', markersize = 5, color = 'red')
		plt.show()

#--------------------------------------------------------------------------------------------------------------
'''
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image

def on_press(event):
	global cnt
	cnt += 1
	if cnt < 7:
		print(event.xdata, event.ydata, end = ' ')
	else:
		print(event.xdata, event.ydata)
		plt.close()

for i in range(94, 205):
	cnt = 0
	print('images/image' + str(i) + '.jpg', end = ' ')
	fig = plt.figure()
	img = Image.open('/Users/dingding/Desktop/data/images/image' + str(i) + '.jpg')
	plt.imshow(img, animated = True)
	fig.canvas.mpl_connect('button_press_event', on_press)
	plt.show()
'''
#--------------------------------------------------------------------------------------------------------------

'''
import matplotlib.pyplot as plt
from PIL import Image
import math

theta = 30

with open('label_left_eye.txt') as file:
	label = file.read().split('\n')
	for i in range(len(label)):
		label[i] = label[i].split(' ')
		label[i][0] = float(label[i][0])
		label[i][1] = float(label[i][1])

for i in range(5):
	fig = plt.figure()
	img = Image.open('/Users/dingding/Desktop/test/data/image' + str(i) + '.jpg').rotate(-theta)
	plt.imshow(img)
	x = (label[i][0] - 32) * math.cos(theta / 180 * math.pi) - (label[i][1] - 32) * math.sin(theta / 180 * math.pi) + 32
	y = (label[i][0] - 32) * math.sin(theta / 180 * math.pi) + (label[i][1] - 32) * math.cos(theta / 180 * math.pi) + 32

	plt.plot(x, y, marker = 'o', markersize = 5, color = 'red')
	plt.show()

#--------------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image

def on_press(event):
	print(event.xdata, event.ydata)

for i in range(104):
	fig = plt.figure()
	img = Image.open('/Users/dingding/Desktop/test/data/image' + str(i) + '.jpg')
	plt.imshow(img, animated = True)
	fig.canvas.mpl_connect('button_press_event', on_press)
	plt.show()

#--------------------------------------------------------------------------------------------------------------

import imageio
import numpy as np

for i in range(104):
	im = np.array(imageio.imread('/Users/dingding/Desktop/test/data/image' + str(i) + '.jpg'))
	print(im.shape)
	if im.shape[0] != im.shape[1]:
		print(i)

#--------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from PIL import Image

with open('label.txt') as file:
	label = file.read().split('\n')
	for i in range(len(label)):
		label[i] = label[i].split(' ')
		label[i][0] = float(label[i][0])
		label[i][1] = float(label[i][1])

for i in range(104):
	fig = plt.figure()
	img = Image.open('/Users/dingding/Desktop/test/data/image' + str(i) + '.jpg')
	plt.imshow(img)
	plt.plot(label[i][0], label[i][1], marker = 'o', markersize = 5, color = 'red')
	plt.show()

#--------------------------------------------------------------------------------------------------------------

import os
a = os.listdir('/Users/dingding/Desktop/test/more_data_cropped')
for i in range(len(a)):
	os.rename('/Users/dingding/Desktop/test/more_data_cropped/' + a[i], '/Users/dingding/Desktop/test/more_data_cropped/image' + str(i) + '.jpg')

#--------------------------------------------------------------------------------------------------------------

from PIL import Image

for i in range(107):
	im = Image.open('/Users/dingding/Desktop/test/more_data_resized/image' + str(i) + '.jpg')
	im = im.resize((128, 128))
	im.save('/Users/dingding/Desktop/test/more_data_resized/image' + str(i) + '.jpg')
'''