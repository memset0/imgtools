import cv2
import timeit
import datetime
from .fs import asset_path


def image(filepath, is_asset=True):
    img = cv2.imread(asset_path(filepath) if is_asset else filepath)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def process(func, *args, open=False):
    res = func(*args)
    if open:
        cv2.imshow('image', cv2.cvtColor(res, cv2.COLOR_RGB2BGR))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return res


def bench(func, name='unnamed_bench'):
    start = timeit.default_timer()
    func()
    end = timeit.default_timer()
    print(name + ':', datetime.timedelta(seconds=end - start))
