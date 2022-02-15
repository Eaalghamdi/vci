import sys

if sys.version_info.major < 3:
    sys.exit("Python 3 required but lower version found. Aborted.")

import requests


def api_is_up():
    r = requests.get("http://127.0.0.1:5000/api/v1.0/system/test")
    response_dict = r.json()
    if response_dict["status"] == "good":
        return True
    else:
        return False
