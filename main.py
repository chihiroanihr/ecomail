from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

imageForTest = "proteinsale.png"

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
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

#Authenticates the credentials using http method
http = credentials.authorize(httplib2.Http())
#run service(features)
service = discovery.build('gmail', 'v1', http=http)


import send_email
from ImageProcessor import imageProcessor
# Now, create message
sendInst = send_email.send_email(service)
# (sender, recipient, title, body, attachment)

# Decide what to send
sender = "chihiroanihr@gmail.com"
to = "rhina4649@gmail.com"
title = "Testing Email"
body = "Hi THERE"
bcc = ""

# Filter image
imageForTest = "proteinsale.png"
image_path = os.getcwd() + "\\img\\" + imageForTest
imageToSend = imageProcessor(image_path, True)

message = sendInst.create_message_with_attachment(sender,to,bcc,title,body,imageToSend)
#sendInst send instance, send message
sendInst.send_message('me',message)
# "me": user_id from def send_message(self, user_id, message) in send_email.py

import json
import get_email
getInst = get_email.get_email(service)
messages = getInst.GetMessageList(DateFrom='2020-01-01',DateTo='2020-02-01')
#output result
for message in messages:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(message, f, ensure_ascii=False, indent=4)
