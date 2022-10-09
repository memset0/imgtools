import cv2
import numpy as np
import numba as nb

__import__('sys').path.append(__import__('os').getcwd())
from imgtools import test


def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def to_rgb(img, r=255, g=0, b=0):

    @nb.njit
    def transform(rgb, gray, r, g, b, w, h):
        for i in range(w):
            for j in range(h):
                rgb[i][j][0] = 255 - gray[i][j] * b // 255
                rgb[i][j][1] = 255 - gray[i][j] * g // 255
                rgb[i][j][2] = 255 - gray[i][j] * r // 255

    w, h, _ = img.shape
    gray = to_gray(img)
    gray_rev = np.subtract(255, gray)

    rgb = np.zeros((w, h, 3)).astype(np.uint8)
    transform(rgb, gray_rev, 255 - r, 255 - g, 255 - b, w, h)

    return rgb


def tests(open=False):
    test.process(to_rgb, test.image('example.png'), open=open)


if __name__ == '__main__':
    tests(open=True)
