# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:48:32 2022

DO NOT MOVE THIS FILE
make sure this file in a folder in the root directory
Creates variable that points to the root directory and other file paths


@author: Kelly
"""

import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..')) #gets the path to the root directory (one file level up)
RAW_FILE_DIR = os.path.join(ROOT_DIR, 'Videos', 'RawVids') #Location of raw excel files
PROCESSED_FILE_DIR = os.path.join(ROOT_DIR, 'Videos', 'ProcessedVids') #location of processed mat files