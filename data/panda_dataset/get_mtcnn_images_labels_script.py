import cv2
import math

with open('./mtcnn_labels.txt', 'w') as target_file:
	with open('./labels.txt') as source_file:
		lines = source_file.read().split('\n')
		for line in lines:
			line = line.split(' ')
			print(line[0])

			img = cv2.imread(line[0])
			line = line[0:5] + line[39:41] + line[43:45] + line[53:55] + line[57:59] + line[63:65]

			scale = math.sqrt((200 * 200) / (img.shape[0] * img.shape[1]))

			img = cv2.resize(img, (int(scale * img.shape[1]), int(scale * img.shape[0])))
			img = cv2.Laplacian(img, cv2.CV_64F)
			for i in range(1, len(line)):
				line[i] = str(float(line[i]) * scale)

			#print(img.shape)
			#cv2.imshow('image', img)
			#cv2.waitKey(0)
			cv2.imwrite('./mtcnn_' + line[0][2:], img)

			new_line = ''
			for tmp in line:
				new_line += tmp
				new_line += ' '
			new_line = new_line[:-1] + '\n'
			target_file.write(new_line)