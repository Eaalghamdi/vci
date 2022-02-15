import os
import tempfile

APPDIR = os.path.abspath(os.path.abspath(os.path.dirname(__file__)))
SETUPFILEDIR = os.path.abspath(os.path.join(APPDIR, ".."))
TESTDIR = os.path.abspath(os.path.join(APPDIR, "tests"))

MEMTEMPDIR = "/dev/shm"
if os.path.isdir(MEMTEMPDIR):
    tempfile.tempdir = MEMTEMPDIR
