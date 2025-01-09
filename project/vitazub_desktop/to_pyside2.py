import os
import subprocess
from pathlib import Path

pwd = Path(__file__).parent
files = os.listdir(f'{pwd}/ui')

for i in files:
    if i.endswith('.ui'):
        file = i.split('.')[0]
        subprocess.run(['pyside2-uic',  f'{pwd}/ui/{file}.ui',  '-o', f'{pwd}/widgets_descriptions/{file}.py'])
