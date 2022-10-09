import cv2
from .fs import asset_path


def image(filepath, is_asset=True):
    return cv2.imread(asset_path(filepath) if is_asset else filepath)


def process(func, *args, open=False):
    res = func(*args)
    if open:
        cv2.imshow('image', res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return res