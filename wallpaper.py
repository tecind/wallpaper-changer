import os
from os.path import isfile, join

folderpath = r"E:\All Projects\Auto Wallpaper"
# folderpath = "."
all_files = [ f for f in os.listdir(folderpath) if isfile(join(folderpath, f))]

print(all_files)
