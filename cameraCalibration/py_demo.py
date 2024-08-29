filename = 'calibration/Image__2018-10-05__10-29-04.png'

import cv2 as cv
import re

print('OpenCV version:', cv.__version__)
# print(cv.getBuildInformation())
cv_info = [re.sub('[\t\n]', ' ', ci.strip()) for ci in cv.getBuildInformation().strip().split('\n') 
               if len(ci) > 0 and re.search(r'(qt[ ]*:?)', ci.lower()) is not None]
print(cv_info)

img = cv.imread(filename)
cv.imshow('to be shown', img)