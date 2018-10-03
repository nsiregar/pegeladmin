from os import path

BASE_PATH = path.normpath(path.join(path.abspath(path.dirname(__file__)), "."))

def path_to(*xs):
    return path.join(BASE_PATH, *xs)
    