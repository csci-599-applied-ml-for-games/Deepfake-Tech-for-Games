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