import os
from os.path import isfile, join
import time
import ctypes

folderpath = r"E:\All Projects\Auto Wallpaper"

all_files = [ f for f in os.listdir(folderpath) if isfile(join(folderpath, f))]

for image in all_files:
    print(image)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, folderpath+ "\\" + image, 0)
    time.sleep(1)
