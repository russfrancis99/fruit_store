#!/usr/bin/env python3

import os
import reports
import emails
from datetime import date

# the purpose of this module is to 
# 1: analyse supplier-date in the descriptions directory and produce a summary paragraph 
# 2: make a call to the method report.generate report() - passing the filename for attachment, title for the pdf and the summary paragrap
# 3: make a call to emails.generate_email()
# 4: send the email using the email.send_email() method

# write a script to process text data from supplier-data/descriptions directory
# dev copy in reports.py that needs refactoring
def generate_paragraph(fruit_data_folder):
    report_text = ""  # string to be returned.
    email_text = ""
    #iterate through each 00x.txt in fruit_data_folder
    for f in os.listdir(fruit_data_folder):
        file = fruit_data_folder + "/" + f
        with open(file, "r") as file_object:
            #split content of file into lines separated by \n"
            data_list = file_object.read().split('\n')
            fruit = data_list[0]
            weight = data_list[1]
            # add and format data to report text string with xml tag <br> for line breaks
            report_text += "name: {}".format(fruit)
            report_text += "<br></br>"
            report_text += "weight: {}".format(weight)
            report_text += "<br></br>"
            report_text += "<br></br>"     
            file_object.close()
    return report_text

def main():
    fruit_data = "supplier-data/descriptions"
    pdf_filepath = "/tmp/processed.pdf"
    report_body = generate_paragraph(fruit_data)
    todays_date = str(date.today())
    title = "Processed Update on " + todays_date
    result = reports.generate_report(pdf_filepath, title, report_body)

    # preparing and sending email confirmation
    sender = 'weetabix4@gmail.com'   # for testing. comment in production. Note this is NOT the smtp server. 
    receiver = 'russfrancis99@gmail.com' # for testing only. comment in production 
    # sender = 'automation@example'
    # receiver = 'username@example'  replace with address given in connections panel 
    subject_line = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    msg = emails.generate_email(sender, receiver, subject_line, body, pdf_filepath)
    # emails.send_email(msg) # uncomment for production environment
    emails.send_gmail(msg) # for testing in gmail acount

if __name__ == "__main__": 
    main()