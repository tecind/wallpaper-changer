import ctypes

img = r"E:\All Projects\Auto Wallpaper\download.jpg"
print("start..")

ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)

print("over!")