import gmail
import requests
from datetime import date
import json
import os.path

g = gmail.login(config.gmail.user, config.gmail.password)

#only unarchived, unread messages marked as priority up until midnight pacific
today = date.today()
msgs = g.important().mail(unread=True, label="INBOX", before=today)

num_msgs = len(msgs)

datfile = '/home/jcarver/code/quantified-self/dat/mail-priority-count/%s' % today.strftime('%Y%m%d')
if not os.path.isfile(datfile):
    with open(datfile, 'w') as f:
        f.write('%s\n' % num_msgs)
