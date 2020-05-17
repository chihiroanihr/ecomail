from __future__ import print_function
import httplib2
from datetime import datetime
from email.utils import formatdate
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import base64  # For encoding emails
# Allow you to process the data that you upload in a different way
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import mimetypes
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

class send_email:
    def __init__(self,service): 
        #service: the variable that allows you to run all the commands you sent to the GMAIL api
        self.service = service

    def create_message(self,sender, to, bcc, subject, message_text):
      message = MIMEText(message_text)  # message_text: body of the message
      message['to'] = to  # recipient
      message['from'] = sender  # sender
      message['subject'] = subject  # subject
      message['Bcc'] = bcc
      message['Date'] = formatdate(localtime=True)
      return {'raw': base64.urlsafe_b64encode(message.as_bytes())} # change from string to bytes

    def create_message_with_attachment(self, sender, to, bcc, subject, message_text, file):
      message = MIMEMultipart() # using attachment requires Multipart()
      # one part email: have body
      # two part email: have body and an attachment
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject
      message['Bcc'] = bcc
      message['Date'] = formatdate(localtime=True)

      msg = MIMEText(message_text)
      message.attach(msg)

      content_type, encoding = mimetypes.guess_type(file)
      # identify what file we are going to be attaching (MIME)
      if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
      main_type, sub_type = content_type.split('/', 1)
      if main_type == 'text':
        fp = open(file, 'rb')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
      elif main_type == 'image':
        fp = open(file, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
      elif main_type == 'audio':
        fp = open(file, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
      else:
        fp = open(file, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
      filename = os.path.basename(file)
      # adds header: attachment name
      msg.add_header('Content-Disposition', 'attachment', filename=filename)
      message.attach(msg) # attaches the attachment to the main body

      return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
      #.decode() to convert byte back to base 64 in basic plain text

    def send_message(self, user_id, message):
      """Send an email message.
      Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.
      Returns:
        Sent Message.
      """
      try:
        message = (self.service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
      except errors.HttpError as error:
        print('An error occurred: %s' % error)