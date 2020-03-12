This MTCNN codebase is cloned from https://github.com/LeslieZhoa/tensorflow-MTCNN with modifications listed below.
1. Change the data input format. 
2. Add pretrained model as CNN initialization. 
3. Change the config file to modify the threshold for each MTCNN detection step.
4. In most cases, our target game character appear in the image only once, so modify the detection process such that only the highest confidence face is shown.