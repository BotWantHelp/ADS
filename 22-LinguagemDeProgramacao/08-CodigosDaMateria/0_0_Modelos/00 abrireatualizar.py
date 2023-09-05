import pyautogui as pa
import time as t
import os
import subprocess as sp

rootFolder = "C:\Delphi"
folders = [folder for folder in os.listdir(rootFolder) if 
          os.path.isdir(os.path.join(rootFolder, folder))]

print(folders)

for folder in folders:
    if "rapha" in folder.lower():
        folder_path = os.path.join(rootFolder, folder)
        sp.run(["explorer", folder_path])
        t.sleep(1)

        pa.moveTo(400, 450, duration=0.5)
        pa.rightClick()
        t.sleep(1)

        pa.moveTo(360, 400, duration=0.5)
        pa.click()
        t.sleep(3)
        pa.hotkey('alt', 'f4')