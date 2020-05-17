from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


import auth
def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'credentials_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

#Authenticates the credentials using http method
http = credentials.authorize(httplib2.Http())
#run service(features)
service = discovery.build('gmail', 'v1', http=http)

# get_labels() 

import send_email
from ImageProcessor import imageProcessor
# Now, create message
sendInst = send_email.send_email(service)
# (sender, recipient, title, body, attachment)

# Decide what to send
text = "Hi there"
sender = "chihiroanihr@gmail.com"
to = "rhina4649@gmail.com"
title = "Testing Email"
body = "Hi THERE"
image_path = os.getcwd() + "\\img\\image.jpg"

# Filter image
filterRequested = True
imageToSend = imageProcessor(image_path, filterRequested)

message = sendInst.create_message_with_attachment(sender,to,title,body,imageToSend)
#sendInst send instance, send message
sendInst.send_message('me',message)
    # "me": user_id from def send_message(self, user_id, message) in send_email.py
