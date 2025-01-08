import os
import subprocess
dirname = '../ui'
files = os.listdir(dirname)

for i in files:
    if i.endswith('.ui'):
        file = i.split('.')[0]
        subprocess.run(['pyside2-uic',  '../ui/' + file + '.ui',  '-o', file + '.py'])
