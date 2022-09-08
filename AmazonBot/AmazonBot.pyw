from subprocess import Popen
import subprocess
import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.startswith('BOT'):
            os.startfile(file)
