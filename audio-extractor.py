import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from timecode import Timecode
import os
import datetime


files = os.listdir('./segments/')

for f in files:
    name = './audios/'+f
    name = name.replace(".mp4", "")
    os.system("ffmpeg -i ./segments/"+f+" -ab 160k -ac 2 -ar 44100 -vn "+name+".wav")