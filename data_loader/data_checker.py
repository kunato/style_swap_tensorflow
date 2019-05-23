import os
import sys
import cv2

_IMAGE_SIZE = 512

image_folder = '/Users/kunato/Downloads/train/'

filenames = [os.path.join(image_folder, filename)
             for filename in next(os.walk(image_folder))[-1]]

for fname in filenames:
    print(
        "\r>> Reading file [%s] image" % fname)
    try:
        img = cv2.imread(fname, cv2.IMREAD_COLOR)
        img = img[:, :, ::-1]
        img = cv2.resize(img, (_IMAGE_SIZE, _IMAGE_SIZE))
    except:
        print("\r>> [ERROR] Reading file [%s] image" % fname)
