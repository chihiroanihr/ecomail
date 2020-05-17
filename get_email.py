from __future__ import print_function
import base64
import email
from email.utils import formatdate

class get_email:
    def __init__(self,service):
        #service: the variable that allows you to run all the commands you sent to the GMAIL api
        self.service = service

    def GetMessageList(self,DateFrom,DateTo):
        MessageList = []

        query = ''
        # Search query
        if DateFrom != None and DateFrom !="":
            query += 'after:' + DateFrom + ' '
        if DateTo != None  and DateTo !="":
            query += 'before:' + DateTo + ' '
        #if MessageFrom != None and MessageFrom !="":
            #query += 'From:' + MessageFrom + ' '

        # get the list of Mail ID (max 100 mails)
        messageIDlist = self.service.users().messages().list(userId='me',maxResults=100,q=query).execute()
        #If no mail: message no found
        if messageIDlist['resultSizeEstimate'] == 0:
            print("Message is not found")
            return MessageList
        #get the details of message based on messageID
        for message in messageIDlist['messages']:
            row = {}
            row['ID'] = message['id']
            MessageDetail = self.service.users().messages().get(userId='me',id=message['id']).execute()
            for header in MessageDetail['payload']['headers']:
                #get name, date, subject of an email
                if header['name'] == 'Date':
                    row['Date'] = header['value']
                elif header['name'] == 'From':
                    row['From'] = header['value']
                elif header['name'] == 'Subject':
                    row['Subject'] = header['value']
            MessageList.append(row)
        return MessageList

    def get_mime_message(service, user_id, msg_id):
        try:
            message = self.service.users().messages().get(userId=user_id, id=msg_id,
                                                     format='raw').execute()
            print('Message snippet: %s' % message['snippet'])
            msg_str = base64.urlsafe_b64decode(message['raw'].encode("utf-8")).decode("utf-8")
            mime_msg = email.message_from_string(msg_str)

            return mime_msg
        except Exception as error:
            print('An error occurred: %s' % error)


    def get_attachments(service, user_id, msg_id, store_dir):
        try:
            message = self.service.users().messages().get(userId=user_id, id=msg_id).execute()

            for part in message['payload']['parts']:
                if(part['filename'] and part['body'] and part['body']['attachmentId']):
                    attachment = service.users().messages().attachments().get(id=part['body']['attachmentId'], userId=user_id, messageId=msg_id).execute()

                    file_data = base64.urlsafe_b64decode(attachment['data'].encode('utf-8'))
                    path = ''.join([store_dir, part['filename']])

                    f = open(path, 'wb')
                    f.write(file_data)
                    f.close()
        except Exception as error:
            print('An error occurred: %s' % error)
