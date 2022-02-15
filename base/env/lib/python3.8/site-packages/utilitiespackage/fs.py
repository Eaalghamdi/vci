import sys

if sys.version_info.major < 3:
    sys.exit("Python 3 required but lower version found. Aborted.")

import os
import sys

from pathlib import Path
from shutil import copyfile, move, rmtree


def dir_exists(path):
    return os.path.isdir(path)


def dir_create(path):
    if not os.path.exists(path):
        os.makedirs(path)


def dir_delete(path):
    rmtree(path)


def file_delete(path):
    os.remove(path)


def file_copy(src, dst):
    copyfile(src, dst)


def file_rename(src, dst):
    os.rename(src, dst)


def file_move(src, dst):
    move(src, dst)


def get_user_home():
    return str(Path.home())


def list_files_in_dir(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    return f


def list_dirs_in_dir(path):
    d = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        d.extend(dirnames)
        break
    return d
