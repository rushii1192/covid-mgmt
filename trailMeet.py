from backend import MeetCreator
import datetime

meet = MeetCreator
d1 = datetime.datetime.strptime("2013-07-12T07:00:00Z","%Y-%m-%dT%H:%M:%SZ")
meet.createMeeting()