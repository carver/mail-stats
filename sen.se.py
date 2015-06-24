from datetime import datetime
import json

import gmail
import requests

import config

g = gmail.login(config.gmail.user, config.gmail.password)

#all unarchived, unread messages marked as priority
msgs = g.important().mail(unread=True, label="INBOX")

def sense_post(dat):
    poststr = json.dumps(postdat)
    requests.post(
            'http://api.sen.se/events',
            params={'sense_key': config.sense.key},
            data=poststr)

# high-res unread inbox count
postdat = {'feed_id': 56134, 'value': len(msgs)}
sense_post(postdat)

# low-res unread inbox count
now = datetime.now()
if now.minute < 3 and now.hour % 4 == 0:
    postdat = {'feed_id': 56356, 'value': len(msgs)}
    sense_post(postdat)
