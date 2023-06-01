# 功能：将单张图片保存为视频
# 状态：已实现

import cv2
import os
# './assets/ADSC07921.JPG'
# set the directory containing the images
# img_dir = './assets/840_iSXIa0hE8Ek'

# set the output video file name and codec
out_file = './assets/b1.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# get the dimensions of the first image
# img_path = os.path.join(img_dir, os.listdir(img_dir)[0])
img = cv2.imread('./assets/b1.JPG')
height, width, channels = img.shape

# create the VideoWriter object
out = cv2.VideoWriter(out_file, fourcc, 10, (width, height))

# loop through the images and write them to the video
# for img_name in sorted(os.listdir(img_dir)):
    # img_path = os.path.join(img_dir, img_name)
    # img = cv2.imread(img_path)
    # out.write(img)
img = cv2.imread('./assets/b1.JPG')
out.write(img)
# release the VideoWriter object and close the video file
out.release()
