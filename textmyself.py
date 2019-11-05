#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

from twilio.rest import Client

accountSID = 'accountSID'
authToken = 'authToken'

myTwilioNumber = 'myTwilioNumber'
myCellPhone = 'myCellPhone'


def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)
    print('Sent notification via SMS')

# import textmyself
# textmyself.textmyself('message you want to text')

