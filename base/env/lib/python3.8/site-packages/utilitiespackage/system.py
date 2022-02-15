import sys

if sys.version_info.major < 3:
    sys.exit("Python 3 required but lower version found. Aborted.")

import os

from termcolor import colored


def abort(message):
    sys.exit(colored("".join(["ABORTED - ", message]), "red", attrs=["bold"]))


def set_env_var(name, value, prefix):
    """Set an environment variable in all caps that is prefixed
    """
    os.environ[prefix.upper() + "_" + name.upper()] = value


def get_env_var(name, prefix):
    """Get an environment variable in all caps that is prefixed
    """
    return os.environ.get(prefix.upper() + "_" + name.upper())
