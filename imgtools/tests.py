import os
import sys
import cv2

sys.path.append(os.getcwd())
from imgtools.utils import asset_path

# cv2 img read
img = cv2.imread(asset_path('example.png'))
print(img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()