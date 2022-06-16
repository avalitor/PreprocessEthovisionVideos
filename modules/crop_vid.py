# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:56:05 2022

Automatically crop videos based on LED turning on

@author: kxu013
"""

import  moviepy.editor as mpy
from modules.config import RAW_FILE_DIR, PROCESSED_FILE_DIR


def edit_video(loadtitle, savetitle, cuts):
    # load file
    video = mpy.VideoFileClip(loadtitle)

    # cut file
    clips = []
    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        clips.append(clip)

    final_clip = mpy.concatenate_videoclips(clips) #combine all clippings

    # add text
    # txt = mpy.TextClip('Please Subscribe!', font='Courier',
    #                    fontsize=120, color='white', bg_color='gray35')
    # txt = txt.set_position(('center', 0.6), relative=True)
    # txt = txt.set_start((0, 3)) # (min, s)
    # txt = txt.set_duration(4)
    # txt = txt.crossfadein(0.5)
    # txt = txt.crossfadeout(0.5)

    # final_clip = mpy.CompositeVideoClip([final_clip, txt])

    # save file
    final_clip.write_videofile(savetitle, threads=20, fps=30,
                               codec = 'libx264', #default is libx264 for mp4, or png for avi
                               audio = False,
                               preset = 'slow', #this does not affect video quality, just video size. slower = smaller file
                               ffmpeg_params=["-crf", '17']) #lower value = better quality, range 17-28

    video.close()


if __name__ == '__main__':    
    title = "LED_test1"
    loadtitle = RAW_FILE_DIR + '/' + title + '.avi'
    savetitle = PROCESSED_FILE_DIR + '/' + title + '.mp4'
    
    # modify these start and end times for your subclips, unit is seconds
    cuts = [('3', '10')]
    
    edit_video(loadtitle, savetitle, cuts)