# PreprocessEthovisionVideos
crop videos based on LED signal for tracking in Ethovision

Video files are not stored on Github because of size

Place videos to be processed in the folder `Videos/RawVids`

Run `trim_vid_LED.py`

- Make sure coordinates for the location of the LED are correct 
- Get coordinates by opening a screenshot of the video in Paint and mousing over the area of interest
- I suggest testing the coordinates are correct before running the file by uncommenting the create gif command in get_crop

Processed videos are in the folder `Videos/ProcessedVids`

## Install
Dependencies: 

'conda install python numpy spyder pyqtwebengine'

'pip install moviepy'

Make sure moviepy version is at least 2.0.0.dev2
