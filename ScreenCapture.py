import numpy as np
import cv2
from PIL import ImageGrab

# windows
FOURCC = 'DIVX'
# linux
#  FOURCC = 'XVID'
p = ImageGrab.grab()
a, b = p.size
fourcc = cv2.VideoWriter_fourcc(*FOURCC)
video = cv2.VideoWriter('video.mp4', fourcc, 60, (a, b))

while True:
    im = ImageGrab.grab()
    cv_im = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    video.write(cv_im)
video.release()
