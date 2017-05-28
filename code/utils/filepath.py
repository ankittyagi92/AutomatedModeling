import os

def local_path(path):
    path = os.path.expanduser(path)
    load_dir = os.path.dirname(os.path.abspath(__file__))
    if len(path) == 0:
        return load_dir
    if path[0] != os.sep:
        return load_dir + '/../' + path
    return path