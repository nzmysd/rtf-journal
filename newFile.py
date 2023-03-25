import os
import subprocess
from datetime import datetime

dir_path = 'C:\\Users\\nozom\\OneDrive\\Documents\\Journal\\'
date_format = 'journal-%m-%d-%y.rtf'
wordpad = "C:\Program Files (x86)\Windows NT\Accessories\wordpad.exe"

curr_time = datetime.now()
file_name = dir_path + curr_time.strftime(date_format)
if os.path.exists(file_name):
    subprocess.Popen([wordpad, file_name])
else: 
    with open(file_name, 'w') as fp:
        subprocess.Popen([wordpad, file_name])


