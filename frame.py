import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import os
import time
import sys

os.system("gnome-terminal -e 'bash -c \"ssh -tt root@r630-098-idrac < en.fifo > en2.fifo; bash\" '")
#os.system("ls")
#time.sleep(2)
os.system("python OneServer.py en.fifo en2.fifo")
#os.system("gnome-terminal -e 'bash -c \"ls; bash\" '")
#time.sleep(2)
#os.system("ls")
