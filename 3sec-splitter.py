import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from timecode import Timecode
import os
import datetime


files = os.listdir('./train/')

for f in files:
    cap = cv2.VideoCapture('./train/'+f)
    frame_no = 0
    start_frame = 0
    end_frame = 74
    segment = 0

    while(cap.isOpened()):
        frame_exists, curr_frame = cap.read()
        if frame_exists is not True:
            break
        

        if frame_no == (start_frame):
            t_start = cap.get(cv2.CAP_PROP_POS_MSEC)


        if frame_no == (end_frame):
            start_frame = start_frame + 75
            end_frame = end_frame + 75
            segment = segment + 1
            t_end = cap.get(cv2.CAP_PROP_POS_MSEC)
            name = "./segments/"+f+"_"+ str(segment)

            t_end = datetime.datetime.fromtimestamp(round(t_end/1000.0))
            t_end = t_end.strftime("%H:%M:%S").replace("06:", "00:")


            t_start = datetime.datetime.fromtimestamp(round(t_start/1000.0))
            t_start = t_start.strftime("%H:%M:%S").replace("06:", "00:")


            os.system("ffmpeg -ss "+t_start+" -to "+t_end+" -i ./train/"+f+"  -vcodec libx264 -acodec aac -async 1 "+name+".mp4")

        frame_no += 1

    cap.release()