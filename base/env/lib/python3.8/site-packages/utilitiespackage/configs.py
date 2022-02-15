import sys

if sys.version_info.major < 3:
    sys.exit("Python 3 required but lower version found. Aborted.")

import os
import json

from utilitiespackage.fs import list_files_in_dir, list_dirs_in_dir


def get_json_dict_from_dir(name, dir):
    assert len(list_dirs_in_dir(dir)) == 0
    raw_names = list_files_in_dir(dir)
    names = [os.path.splitext(x)[0] for x in raw_names]
    if name in names:
        with open(os.path.join(dir, name + ".json"), "r") as f:
            dic = json.load(f)
    return dic
