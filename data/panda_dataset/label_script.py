import os
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image

def on_press_mouse(event):
	global result
	global plotted_points

	result.append('{0:.2f} {1:.2f} '.format(event.xdata, event.ydata))
	tmp, = plt.plot(event.xdata, event.ydata, marker = 'o', markersize = 1, color = 'red')
	plotted_points.append(tmp)
	fig.canvas.draw()

	if len(result) == 34:
		plt.close()

def on_press_key(event):
	global result
	global plotted_points

	if len(result) > 0:
		result.pop()
		plotted_points[-1].remove()
		fig.canvas.draw()
		plotted_points.pop()

image_name_list = os.listdir('./images')
image_name_list = list(filter(lambda x: x[-4:] == '.jpg', image_name_list))

for image_name in image_name_list:
	image_name = './images/' + image_name
	result = []
	plotted_points = []
	print(image_name, end = ' ')
	fig = plt.figure()
	img = Image.open(image_name)
	plt.imshow(img, animated = True)
	fig.canvas.mpl_connect('button_press_event', on_press_mouse)
	fig.canvas.mpl_connect('key_press_event', on_press_key)
	plt.show()
	result[-1] = result[-1][:-1]
	for tmp in result:
		print(tmp, end = '')
	print()