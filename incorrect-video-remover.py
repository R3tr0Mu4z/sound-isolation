import os
audio_files = os.listdir('./audios-noisy/')

for f in audio_files:
    v = f.replace("seg_", "")
    v = v.split("_")
    v = v[0]+"_"+v[1]+"_"+v[2]+".mp4_"+v[3]
    v = v.replace("wav", "mp4")
    ls = {}
    
    video_path = './crops/'+v
    if os.path.isfile(video_path):
        if os.path.getsize(video_path) == 258:
            os.remove(video_path)
            os.remove('./audios-noisy/'+f)
    else:
        os.remove('./audios-noisy/'+f)