import sys, os

INTERP = os.path.expanduser("~/flask_venv/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from ApiE import index as application

