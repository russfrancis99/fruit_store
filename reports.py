#! /usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report(pdf_filepath, title, paragraph_content):
    """The purpose is this function is to generate a pdf report and save it as /tmp/processed.pdf"""
    report = SimpleDocTemplate(pdf_filepath)
    styles = getSampleStyleSheet()
    empty_line = Spacer(1,20)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph_content, styles["BodyText"])
    report.build([report_title, empty_line, report_info])
    # msg = "pdf report created at" + pdf_filepath
    return 0

# # method generate paragrpah under for report_mail
# def generate_paragraph(fruit_data_folder):
# ## expected format of paragraph
#     report_text = ""  # string to be returned. 
#     #iterate through each 00x.txt in "textdata_folder""
#     for f in os.listdir(fruit_data_folder):
#         file = fruit_data_folder + "/" + f
#         with open(file, "r") as file_object:
#             #split content of file into lines separated by \n"
#             data_list = file_object.read().split('\n')
#             fruit = data_list[0]
#             weight = data_list[1]
#             # add and format data to report text string with xml tag <br> for line breaks
#             report_text += "name: {}".format(fruit)
#             report_text += "<br></br>"
#             report_text += "weight: {}".format(weight)
#             report_text += "<br></br>"
#             file_object.close()
#     return report_text

# note this is for dev only the arguments for generate report will need
# to be provided from the call to generate report in report.email module

# test_title = "Processed title on: {insert todays date}"
# test_para = generate_paragraph("supplier-data/descriptions")
# generate_report("test.pdf",test_title, test_para)

# form of pdf report
        #blank
        #name: kiwi
        #weight: 500 lbs
        #blank
        #name: oranges
        #weight: 300 lbs