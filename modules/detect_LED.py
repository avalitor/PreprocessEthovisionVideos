# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 17:07:53 2022

extract video and detect if LED turns on

@author: kxu013
"""

def coord_to_colour(value):
    new_coord = (value[0], value[1])
    img = screenGrab()
    pix_color = img.getpixel(new_coord)
    pix_sum = sum(pix_color)
    return pix_sum

#solve row A
def solve_A():
    if coord_to_colour(hexCoord['A1']) >= 600.: #this number determines colour detection threshold
        print("solve A1")
        press('B2')
        
        
        
def get_crop(videofile):
    pass

def detect_LED():
    pass

def extract_crop():
    return cut_start, cut_end

cut_start, cut_end = extract_crop()