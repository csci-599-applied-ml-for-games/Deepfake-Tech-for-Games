import matplotlib.pyplot as plt
from PIL import Image

with open('./labels.txt') as file:
	lines = file.read().split('\n')
	for line in lines:
		line = line.split(' ')
		for i in range(1, len(line)):
			line[i] = float(line[i])
		print(line[0])
		img = Image.open(line[0])
		plt.figure()
		plt.imshow(img)
		plt.plot([line[1], line[1]], [line[2], line[4]], color = 'red', linestyle = '-', linewidth = '0.5')
		plt.plot([line[3], line[3]], [line[2], line[4]], color = 'red', linestyle = '-', linewidth = '0.5')
		plt.plot([line[1], line[3]], [line[2], line[2]], color = 'red', linestyle = '-', linewidth = '0.5')
		plt.plot([line[1], line[3]], [line[4], line[4]], color = 'red', linestyle = '-', linewidth = '0.5')
		for i in range(32):
			plt.text(line[2*i+5], line[2*i+6], str(i), color = 'red', fontsize = 5)
			plt.plot(line[2*i+5], line[2*i+6], marker = 'o', markersize = 0.5, color = 'red')
		plt.show()