# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:00:16 2022

change video fps, also changes duration
note: requires the most recent version of moviepy (installed in env vid2)

@author: kxu013
"""
import os
import  moviepy.editor as mpy
from modules.config import RAW_FILE_DIR, PROCESSED_FILE_DIR

#vid paths
loadtitle = RAW_FILE_DIR+"/2022-09-08 141351 060 Test1-compress.mp4"
savetitle = os.path.join(PROCESSED_FILE_DIR, os.path.basename(loadtitle).split('.')[0] + '.mp4')


video = mpy.VideoFileClip(loadtitle) #load video


new_fps = video.with_fps(24.93, change_duration=True)

new_fps.write_videofile(savetitle, threads=20,
                        codec = 'libx264', #default is libx264 for mp4, or png for avi
                        audio = False,
                        preset = 'slow', #this does not affect video quality, just video size. slower = smaller file
                        ffmpeg_params=["-crf", '17']) #lower value = better quality, range 17-28

video.close()
