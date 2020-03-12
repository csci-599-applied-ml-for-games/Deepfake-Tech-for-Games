import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

import matplotlib.pyplot as plt
from PIL import Image

from math import sin, cos, pi

num_example = 204
num_training = 190

def rotate_theta(label, theta):
	x0 = (label[0] - 0.5) * cos(theta) - (label[1] - 0.5) * sin(theta) + 0.5
	y0 = (label[0] - 0.5) * sin(theta) + (label[1] - 0.5) * cos(theta) + 0.5
	x1 = (label[2] - 0.5) * cos(theta) - (label[3] - 0.5) * sin(theta) + 0.5
	y1 = (label[2] - 0.5) * sin(theta) + (label[3] - 0.5) * cos(theta) + 0.5
	return [x0, y0, x1, y1]

with open('label_left_eye.txt') as file:
	label_left_eye = file.read().split('\n')
	for i in range(len(label_left_eye)):
		label_left_eye[i] = label_left_eye[i].split(' ')
		label_left_eye[i][0] = float(label_left_eye[i][0])
		label_left_eye[i][1] = float(label_left_eye[i][1])
label_left_eye = np.array(label_left_eye) / 64

with open('label_right_eye.txt') as file:
	label_right_eye = file.read().split('\n')
	for i in range(len(label_right_eye)):
		label_right_eye[i] = label_right_eye[i].split(' ')
		label_right_eye[i][0] = float(label_right_eye[i][0])
		label_right_eye[i][1] = float(label_right_eye[i][1])
label_right_eye = np.array(label_right_eye) / 64

label = []
for i in range(len(label_left_eye)):
	label.append(np.concatenate([label_left_eye[i], label_right_eye[i]]))
label = np.array(label)

num_theta = 12
theta = [
			5, -5, 
			10, -10, 
			15, -15, 
			20, -20, 
			25, -25, 
			30, -30,
		]
for i in range(num_theta):
	theta[i] = theta[i] / 180 * pi

feature = []
feature_rotate = [[] for i in range(num_theta)]
for i in range(num_example):
	img = Image.open('/Users/dingding/Desktop/test/data/image' + str(i) + '.jpg')
	feature.append(np.array(img))
	for j in range(num_theta):
		feature_rotate[j].append(np.array(img.rotate(-theta[j] * 180 / pi)))
feature = np.array(feature).astype('float32') / 255
for i in range(num_theta):
	feature_rotate[i] = np.array(feature_rotate[i]).astype('float32') / 255

label_rotate = [[] for i in range(num_theta)]
for i in range(num_example):
	for j in range(num_theta):
		label_rotate[j].append(rotate_theta(label[i], theta[j]))
for i in range(num_theta):
	label_rotate[i] = np.array(label_rotate[i])

feature_training = feature[:num_training]
label_training = label[:num_training]
for i in range(num_theta):
	feature_training = np.concatenate([feature_training, feature_rotate[i][:num_training]])
	label_training = np.concatenate([label_training, label_rotate[i][:num_training]])

model = Sequential()
model.add(Conv2D(32, kernel_size = (3, 3), activation = 'relu', input_shape = (64, 64, 3)))
#model.add(Conv2D(32, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (3, 3)))
model.add(Conv2D(64, kernel_size = (3, 3), activation = 'relu'))
#model.add(Conv2D(64, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Conv2D(64, kernel_size = (3, 3), activation = 'relu'))
#model.add(Conv2D(64, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Conv2D(128, kernel_size = (3, 3), activation = 'relu'))
#model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dense(4))

model.compile(loss = 'mean_squared_error', optimizer='adam')

model.fit(feature_training, label_training, batch_size = 32, epochs = 50, validation_data = (feature[num_training:], label[num_training:]))

prediction = model.predict(feature)

# show result
print('training result')
for i in range(10):
	plt.figure()
	plt.imshow(Image.open('/Users/dingding/Desktop/test/data/image' + str(i) + '.jpg'))
	plt.plot(label_left_eye[i][0] * 64, label_left_eye[i][1] * 64, marker = 'o', markersize = 5, color = 'red')
	plt.plot(label_right_eye[i][0] * 64, label_right_eye[i][1] * 64, marker = 'o', markersize = 5, color = 'red')
	plt.plot(prediction[i][0] * 64, prediction[i][1] * 64, marker = 'o', markersize = 5, color = 'green')
	plt.plot(prediction[i][2] * 64, prediction[i][3] * 64, marker = 'o', markersize = 5, color = 'blue')
	plt.show()

print('test result')
for i in range(num_training, num_example):
	plt.figure()
	plt.imshow(Image.open('/Users/dingding/Desktop/test/data/image' + str(i) + '.jpg'))
	plt.plot(label_left_eye[i][0] * 64, label_left_eye[i][1] * 64, marker = 'o', markersize = 5, color = 'red')
	plt.plot(label_right_eye[i][0] * 64, label_right_eye[i][1] * 64, marker = 'o', markersize = 5, color = 'red')
	plt.plot(prediction[i][0] * 64, prediction[i][1] * 64, marker = 'o', markersize = 5, color = 'green')
	plt.plot(prediction[i][2] * 64, prediction[i][3] * 64, marker = 'o', markersize = 5, color = 'blue')
	plt.show()