import sys
from os import path

cwd = path.abspath(path.join(path.dirname(__file__), '..'))


def joinpath(*args):
    print(path.join(*args), path.abspath(path.join(*args)))
    return path.abspath(path.join(*args))


def assetpath(filepath):
    print(cwd)
    return joinpath(cwd, 'assets', filepath)
