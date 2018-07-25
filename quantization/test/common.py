import sys
import fcntl
import os

_run_once_file_handle = 0


def run_once():
    global _run_once_file_handle

    host_script_file_path = os.path.realpath(sys.argv[0])
    _run_once_file_handle = open(host_script_file_path, 'r')
    try:
        fcntl.flock(_run_once_file_handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except:
        sys.exit('Another instance already running')
