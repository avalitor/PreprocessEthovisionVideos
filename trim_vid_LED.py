# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:51:12 2022

process videos using trim_vid and detect_LED functions

@author: kxu013
"""
import os
import modules.detect_LED as det
import modules.trim_vid as tv
from modules.config import RAW_FILE_DIR

'''
cut single video
'''
coord = [1512, 392]

loadtitle = RAW_FILE_DIR + '/WIN_20231018_12_49_30_Pro_M101_1.mp4'

# det.get_crop(loadtitle, coord, True) #creates a test gif to check the crop

cut_start = det.get_start_time(loadtitle, coord)
tv.edit_video(loadtitle, [cut_start])

'''
cut multiple videos
'''
# coord = [621, 93] #pixel coordinates of the LED in the video

# for f in os.listdir(os.path.join(RAW_FILE_DIR)):
#     path = os.path.join(RAW_FILE_DIR, f)
#     print(path)
#     cut_start = det.get_start_time(path, coord)
#     tv.edit_video(path, [cut_start])