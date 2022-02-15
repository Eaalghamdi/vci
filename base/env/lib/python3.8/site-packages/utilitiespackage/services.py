import sys

if sys.version_info.major < 3:
    sys.exit("Python 3 required but lower version found. Aborted.")

import socket


def service_is_up(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return_value = False
    try:
        s.connect(("localhost", port))
        s.close()
        return_value = True
    except (socket.error):
        return_value = False
    return return_value
