import os
import sys
import cv2
import numpy as np
import numba as nb

sys.path.append(os.getcwd())
from imgtools.utils import test, img404


def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def to_rgb_numba(img, r=255, g=0, b=0):

    @nb.njit
    def transform(rgb, gray, r, g, b, w, h):
        for i in range(w):
            for j in range(h):
                rgb[i][j][0] = 255 - gray[i][j] * r // 255
                rgb[i][j][1] = 255 - gray[i][j] * g // 255
                rgb[i][j][2] = 255 - gray[i][j] * b // 255

    w, h, _ = img.shape
    gray = to_gray(img)
    gray_rev = np.subtract(255, gray)

    rgb = np.zeros((w, h, 3), np.uint8)
    transform(rgb, gray_rev, 255 - r, 255 - g, 255 - b, w, h)

    return rgb


def to_rgb(img, r=255, g=0, b=0):
    gray = to_gray(img)
    gray_rev = np.subtract(255, gray)
    col = np.array([255 - r, 255 - g, 255 - b], np.uint16)
    einsum = np.einsum('ij,k->ijk', gray_rev, col)
    rgb_rev = np.floor_divide(einsum, 255).astype(np.uint8)
    rgb = np.subtract(255, rgb_rev)
    return rgb


def tests(open=False):
    test.process(to_rgb, test.image('example.png'), open=open)


def bench_rgb():
    n = 100
    img = test.image('example.png')

    def test1():
        for _ in range(n):
            to_rgb(img)

    def test2():
        for _ in range(n):
            to_rgb_numba(img)

    test.bench(test1, f'np.einsum * {n} times')
    test.bench(test2, f'numba.njit * {n} times')
    # print(f'np.einsum: to_rgb() * {n} times')
    # cProfile.runctx('test1()', None, locals())
    # print(f'numba.njit: to_rgb() * {n} times')
    # cProfile.runctx('test2()', None, locals())


if __name__ == '__main__':
    # tests(open=True)
    bench_rgb()
