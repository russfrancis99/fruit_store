#! /usr/bin/env python3
import os
import json
import requests
import reports

url = "http://localhost/upload/"     # url of server required here
descriptions = "supplier-data/descriptions/"
file_list = os.listdir(descriptions)
for file in file_list:
    # print("Processing file",file)
    # The dayta in each file found in description directory is opened and parsed for data
    # used to popular a dictionary object and then serialised into json and then uploaded 
    # to a webserver using the requests.post() method.  
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
        # Note: I might want to change this to also write a copy to file so it can be accessed by reports. 
        # as it stands reports is re-parsing the files in descriptions to create a report. 
        # This is a 'state' issue. How to I ensure accurate confirmation. Use code returned from server (r below)
        fruit_json = json.dumps(fruit_dict)
        print("")
        print(f"Printing file {file} as fruit_json ready for upload: \n\n ",fruit_json)
        
        r = requests.post(url, fruit_json)
        
        # to do: if request.post is sucessful call report email (with fruit dict as an argument?)
        print(f"Attempting to upload fruit_data to server. Returned {r.status_code} which means {r.reason}")
        if (r.ok):    # (r.ok) should return true if response code is in success range (code 200 -400?)    
            [print("upload successful. Producing report and sending notificaiton email to supplier")]
            report_email.py(fruit_dict)
        else:
            print("sorry there was a problem")
            
        # The above (if necessary at all) probably needs to be re-written in a try ... exception clause 
        # Next: create a pdf report and send to supplier