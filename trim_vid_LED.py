# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:51:12 2022

process videos using trim_vid and detect_LED functions

@author: kxu013
"""
import os
import modules.detect_LED as det
import modules.trim_vid as tv
from modules.config import RAW_FILE_DIR, PROCESSED_FILE_DIR
import pickle
from collections import defaultdict


'''
cut single video
'''
coord = [1469, 488]
# coord = [1513, 383]
# loadtitle = RAW_FILE_DIR + '/WIN_20241121_12_34_42_Pro_m38_t31.mp4'

# det.get_crop(loadtitle, coord, True) #creates a test gif to check the crop

# cut_start = det.get_start_time(loadtitle, coord)
# tv.edit_video(loadtitle, [cut_start]) #create the video

'''
cut multiple videos
'''
# coord = [1512, 392] #pixel coordinates of the LED in the video

# for f in os.listdir(os.path.join(RAW_FILE_DIR)):
#     path = os.path.join(RAW_FILE_DIR, f)
#     print(path)
#     cut_start = det.get_start_time(path, coord)
#     tv.edit_video(path, [cut_start])

'''
just get start offset times
'''
   
offset_dict = defaultdict(dict)
# trial_dict = {}
for f in os.listdir(os.path.join(RAW_FILE_DIR)):
    path = os.path.join(RAW_FILE_DIR, f)
    trial_name = os.path.basename(path).split('_')[-1].split('.')[0]
    mouse_no = os.path.basename(path).split('_')[-2].split('.')[0]
    print(mouse_no + " " + trial_name)
    cut_start = det.get_start_time(path, coord)
    # trial_dict[trial_name] = cut_start
    offset_dict[mouse_no][trial_name] = cut_start
    
mouse_no = 'm38'
dict_subset = offset_dict[mouse_no]

#save data one mouse at a time (write a loop for this)
file = open(PROCESSED_FILE_DIR+'/offset_dict_'+mouse_no+'.pydict', 'wb') #opens a writable binary file
pickle.dump(dict_subset, file) # dump information to that file
file.close()

# #load data
file = open(PROCESSED_FILE_DIR+'/offset_dict_m35.pydict', 'rb')
data = pickle.load(file)
file.close()


