#Database Connection
import mysql.connector as mysql
import smtplib
import jwt
import requests
import json
from time import time


#class for data connectivity with MySql
class DatabaseConnection(object):
    def __new__(cls, *args, **kwargs):
        conn = mysql.connect(
            host='db4free.net',
            database='covid_mgmt',
            user='sql6468008',
            password='eqHRn7SbqA'
        )
        # print("connected")
        # print(type(conn))
        return conn

# email sender class
class EmailSender(object):
    def __init__(self):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com")
        self.server.login("rushikeshborakhede@student.sfit.ac.in", "password")

    def sendEmail(self,receiver,content):
        self.server.sendmail('rushikeshborakhede@student.sfit.ac.in',receiver,content)

        
    
#Exception Handling

# meets Create
class MeetCreator(object):
    # Enter your API key and your API secret
    __API_KEY = 'ns8woTgrQlCJmZrDt15sDg'
    __API_SEC = 'U1p3KndKvYmUcKfP3T6yeVco67JDqK0coPdn'

    # create a function to generate a token
    # using the pyjwt library


    def generateToken(self):
        token = jwt.encode(

            # Create a payload of the token containing
            # API Key & expiration time
            {'iss': self.__API_KEY, 'exp': time() + 5000},

            # Secret used to generate token signature
            self.__API_SEC,

            # Specify the hashing alg
            algorithm='HS256'
        )
        return token
    
    # send a request with headers including
    # a token and meeting details


    def createMeeting(self,datetime):
        # create json data for post requests
        meetingdetails = {"topic": "The title of your zoom meeting",
                    "type": 2,
                    "start_time": datetime,
                    "duration": "45",
                    "timezone": "Asia/Kolkata",
                    "agenda": "test",

                    "recurrence": {"type": 1,
                                    "repeat_interval": 1
                                    },
                    "settings": {"host_video": "true",
                                "participant_video": "true",
                                "join_before_host": "true",
                                "mute_upon_entry": "False",
                                "watermark": "true",
                                "audio": "voip",
                                "auto_recording": "cloud"
                                }
                    }

        headers = {'authorization': 'Bearer ' + self.generateToken(),
                'content-type': 'application/json'}
        r = requests.post(
            f'https://api.zoom.us/v2/users/me/meetings',
            headers=headers, data=json.dumps(meetingdetails))

        print("\n creating zoom meeting ... \n")
        # print(r.text)
        # converting the output into json and extracting the details
        y = json.loads(r.text)
        join_URL = y["join_url"]
        meetingPassword = y["password"]

        return join_URL

