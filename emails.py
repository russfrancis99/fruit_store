#! /usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import getpass

# This module provides methods to generate an email and attach pdf report (generate_email)
# and send emails to the supplier (send_email() or send_gmail())

def generate_email(sender, receiver, subject_line, body, attachment_path):
  """This method creates an email.EmailMessage() object sets the ("From", "To", "Subject") parameters, 
  sets the body content with .set_content() and attaches a pdf document with .add_attachment() """
  # 1: create an Email Message Obect (to encasulate header, body and attachment data)
  msg = email.message.EmailMessage()
  # 2: instantiate EmailMessage object header properties
  msg["From"] = sender
  msg["To"]= receiver
  msg["Subject"] = subject_line
  # set the content of the body content 
  msg.set_content(body)

  # Add the pdf file to the Email_Message instance (filepath, filename and mime_type/subtype required)
  # extract attachment filename from its path
  pdf_filename = os.path.basename(attachment_path)
  # guess the mimetype & subtype of the document  
  mime_type, _ = mimetypes.guess_type(attachment_path)
  # split the mimetype tuple return above into type and subtype. Is this only way?
  mime_type, mime_subtype = mime_type.split('/', 1)
  # open the pdf for byte reading in a context manager
  with open(attachment_path, 'rb') as ap:     # open the pdf in mode 'rb' (read bytes) 
  # new attachment to Email Message (requires read file content (as bytes), filename and mimetype/subtype 
      msg.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=pdf_filename)
  # return the Email_Message object created 
  return msg

def send_email(message):
  """ connect to 'local host' smtp server without authentication """
  with smtplib.SMTP('localhost') as mail_server:
    # turn up debug feedback
    mail_server.set_debuglevel(1) 
    # authenticate with smpt server.
    response = mail_server.send_message(message)
    # close connection
    # mail_server.quit() (note required if open within a with block)
  

def send_gmail(message):
  """connect to smtp.gmail.com, authenticate and send message (and handle errors?"""
  with smtplib.SMTP_SSL('smtp.gmail.com') as mail_server:
    # authenticate
    # pw=getpass("Password?")
    pw='qydbflgcomrzoatg'    # app password for weetabix4@gmail
    # username = message.sender
    username = message["From"]
    receiver = message["To"]
    # logon to mail server
    mail_server.login(username,pw)
    print(f"attempting to login with:\nusername: {username} \npassword: {pw}")
    # send_message
    print(f"sending message to {receiver}")
    mail_server.send_message(message)
    
    #   except SMTPResponseException as e:
    #   err_code = e.smtp_code
    #   err_message = e.smtp_message
    #   print(f("Attempt to send via email produced: {err_code}, {err_message}"))