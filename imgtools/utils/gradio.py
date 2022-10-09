import cv2
from .fs import asset_path

img404 = cv2.cvtColor(cv2.imread(asset_path('404.png')), cv2.COLOR_RGB2BGR)
