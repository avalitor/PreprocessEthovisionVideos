# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 17:07:53 2022

extract video and detect if LED turns on

@author: kxu013
"""
# import cv2
import  moviepy.editor as mpy
from modules.config import RAW_FILE_DIR, PROCESSED_FILE_DIR

#gets sum of RGB pixel colour from coordinate in frame
def coord_to_colour(frame, coord):
    sample_color = frame[coord[0], coord[1], :]
    pix_sum = sum(sample_color)
    return pix_sum     
        
#crops a 20x20 box around the LED
def get_crop(video_path, coords, save_clip=False):
    
    clip = (mpy.VideoFileClip(video_path)
         .subclip(0, 160) #trims video after 60 seconds (usually 30)
         .crop(x_center=coords[0],
               y_center=coords[1],
               width=20,height=20)) 
    
    #save clip as gif
    if save_clip:
        clip.write_gif(PROCESSED_FILE_DIR+"/test.gif")
    return clip

def detect_LED(video):
    # cap = cv2.VideoCapture(video_path)
    # success = cap.grab() # get the next frame
    # fno = 0
    # while success:
    #  	if fno % sample_rate == 0:
    #          _, img = cap.retrieve()
    #          record = fno
    #  	# read next frame
    #  	success, img = cap.grab()
        
    # # De-allocate any associated memory usage
    # cv2.destroyAllWindows()
    
    framecount = 0
    for t, frame in video.iter_frames(with_times=True):  #returns the frame as H x W index of rbg values
        framecount = framecount + 1
        cut_start = 0.
        if coord_to_colour(frame, [9,9]) >= 200.: #checks if LED is on, usually 600
            print('start time: %s'%t)
            cut_start = t
            break
    
    if cut_start == 0.: print('Warning ::: video not cut')
    return cut_start

def get_start_time(video_path, coord):
    clip = get_crop(video_path, coord)
    return detect_LED(clip)

if __name__ == '__main__':
    video_path = RAW_FILE_DIR + '/WIN_20231018_12_49_30_Pro_M101_1.mp4'
    coord = [1512, 392]
        
    cut_start = get_start_time(video_path, coord)
    
    
