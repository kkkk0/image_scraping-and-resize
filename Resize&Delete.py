import os
from PIL import Image
import fnmatch
import time

LINK = str(input('Input the full directory path of the image folder:'))
print('Previous directory:\t' + os.getcwd())
path = LINK
os.chdir(path)
print('Current directory:\t' + os.getcwd())
HOR = int(input('Input the horizontal pixel value for the new image:'))
VER = int(input('Input the vertical pixel value for the new image:'))

input("Recheck your path. Press Enter to proceed with image resizing process...")

FILENAME = str(input('Input the abbreviation for your new images:'))

fl=[]
for a in os.listdir(path):
    print(a)
    if fnmatch.fnmatch(a, '*.jpg'):
        fl.append(a)
    else:
        continue

count = 1
for f in fl:
    print(f)
    if f.endswith(".jpg"):
        try:
            img = Image.open(f)
            print(img.format)
            print(img.size)
            newimg = img.resize((HOR, VER))
            newimg.save(str(FILENAME) + str(count) + '.jpg')
            print(newimg.size)
            print('saved')
            count = count + 1
        except:
            pass
    else:
        continue

a = int(input("Please check your file. If everything is okay, press 1 to delete the duplicated images. If you don't want to delete, press 2..."))

if a == 1:
    for f in os.listdir(path):
        if fnmatch.fnmatch(f, '*.jpg'):
            img = Image.open(f)
            if img.size == (HOR, VER):
                pass
            else:
                img.close()
                os.remove(str(f))
        else:
            continue
else:
    print('TQ. All done.')
    time.sleep(2)

print('TQ. All done.')
time.sleep(2)
