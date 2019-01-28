#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

from twilio.rest import Client

accountSID = 'ACff5a0ca4da421e2bfa1e29be66563f3c'
authToken = 'd69e018ddf1ad64454d9a52b364edffa'

myTwilioNumber = '+48799449202'
myCellPhone = '+48791497598'


def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)
    print('Sent notification via SMS')

# import textmyself
# textmyself.textmyself('message you want to text')

