#! /usr/bin/env python3
import os
import json
import requests

url = "http://localhost/upload/"     # url of server required here

descriptions = "supplier-data/descriptions/"
file_list = os.listdir(descriptions)
for file in file_list:
    # print("Processing file",file)
    # The data in each file found in description directory is opened and parsed for data which is then
    # used to popular a dictionary object. The dictionary object is then serialised into a json and then uploaded 
    # to a webserver using the requests.post() method. Question what type is a json object? 
    with open(descriptions + file, 'r') as fileobject:
        fruit_data = fileobject.read().split("\n")
        # print(fruit_data)
        file_name = file
        fruit_name = fruit_data[0]
        weight = int(fruit_data[1].rstrip(" lbs"))     # .rstrip needed to str lbs and cast as int
        summary = fruit_data[2]
        (base, ext) = os.path.splitext(file)
        image_name = base + ".jpeg"
        # print(f" File: {file}\n Fruit: {fruit_name} Weight: {weight} Summary:\n {fruit_summary}")
        # The above shows file data is accurately read and assigned to descriptive variables
        # Variables are now ready populate a keyworded dictionary ready for serialisation and upload 
        fruit_dict = {
            "name": fruit_name,
            "weight": weight,
            "description": summary,
            "image_name": image_name}
        
        # print(fruit_dict)

        # serialising dictionary object to json
        fruit_json = json.dumps(fruit_dict)
        print("")
        print(f"Printing file {file} as fruit_json ready for upload: \n\n ",fruit_json)
        # r = requests.post(url, fruit_json)