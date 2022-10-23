import numpy as np


def apply(img, scale, mode):
    scale = int(scale)
    is_darker = True if mode == 'Darker' else False
    if is_darker:
        img = 255 - img
    img = img.astype(np.int32)
    print('before', img)
    img = np.floor_divide(img * scale, 100)
    print('after', img)
    img = img.astype(np.int16)
    img = np.maximum(np.minimum(img, 255), 0)
    if is_darker:
        img = 255 - img
    return img