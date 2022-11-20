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
image_folder='./temp/'


files = os.listdir('./segments/')
detector = MTCNN()
for f in files:
    cap = cv2.VideoCapture('./segments/'+f)

    wait = 0

    vid_data = []

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    video = cv2.VideoWriter('./crops/'+f, fourcc, 25, (128, 128))

    save = True
    while(cap.isOpened()):
        frame_exists, curr_frame = cap.read()
        if frame_exists is not True:
            break
        
        print(f)
        img = curr_frame

        if wait == 0:
            faces = detector.detect_faces(curr_frame)
            if len(faces) == 1:
                bb = faces[0]['box']
                print(bb)

                x = bb[0]
                y = bb[1]
                h = bb[-1]
                w = bb[2]
                
                # break
            else:
                save = False
                # os.remove('./segments/'+f)


        

        if save is True:

            crop_img = img[y:y+h, x:x+w]

            crop_img = cv2.resize(crop_img, (128, 128)) 
            video.write(crop_img)




        wait = wait + 1

        # if wait == 25:
        #     wait = 0


    cv2.destroyAllWindows()
    video.release()

    # break


    

    cap.release()
    # break