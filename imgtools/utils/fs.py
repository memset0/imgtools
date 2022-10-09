import sys
from os import path

cwd = path.abspath(path.join(path.dirname(__file__), '..'))


def join_path(*args):
    # todo: fix ntpath
    # print(path.join(*args), path.abspath(path.join(*args)))
    return path.abspath(path.join(*args))


def asset_path(filepath):
    return join_path(cwd, 'assets', filepath)


def read_file(filepath):
    with open(filepath, 'r+') as file:
        res = file.read()
        file.close()
    return res


def write_file(filepath, content):
    with open(filepath, 'w+') as file:
        file.write(content)
        file.close()