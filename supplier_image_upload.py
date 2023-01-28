#!/usr/bin/env python3
import requests, os

images_folder = 'supplier-data/images'
url = "http://localhost/upload/"

image_list = os.listdir(images_folder)
# print("images in image_list",image_list)
for image in image_list:
    image_path = images_folder + "/" + image
    # print("image_path suffix: ",os.path.splitext(image_path)[1])
    # if the image is a jpeg file attempt to upload to server
    if os.path.splitext(image_path)[1] == '.jpeg':
        # print("attempting to upload", image)
        with open((image_path), 'rb') as opened:
        # note requests.post wants a dictionary of files with key file
            # print("opening",image_path)
            r = requests.post(url, files={'file': opened})
            # print(r.text)
