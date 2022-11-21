import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from timecode import Timecode
import os
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mtcnn.mtcnn import MTCNN
import cv2
import moviepy.video.io.ImageSequenceClip
import numpy as np

def load_video(path):
    frames = []

    cap = cv2.VideoCapture(path)

    frames = []

    while(cap.isOpened()):
        frame_exists, curr_frame = cap.read()
        if frame_exists is not True:
            break
        # curr_frame = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
        curr_frame = cv2.resize(curr_frame, (64, 64)) 
        frames.append(curr_frame/255.)

    frames = np.array(frames)

    three_dee = np.zeros(shape=(64, 64, 75, 3))

    for i in range(len(frames)):
        three_dee[:, :,  i, :] = frames[i]


    # print(three_dee.shape, 'frames shape')

    return three_dee

files = os.listdir('./crops/')
for f in files:
    three_dee = load_video('./crops/'+f)
    np.save('./3d-crops/'+f, three_dee)
    