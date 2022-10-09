import sys
from os import path

cwd = path.abspath(path.join(path.dirname(__file__), '..'))


def join_path(*args):
    # todo: fix ntpath
    # print(path.join(*args), path.abspath(path.join(*args)))
    return path.abspath(path.join(*args))


def asset_path(filepath):
    return join_path(cwd, 'assets', filepath)
