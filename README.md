
example crons

45 23 * * * python /home/jcarver/code/quantified-self/gmail/record.py 2>&1 >> /var/log/qs-gmail-local.cron.log
1-59/15 * * * * python /home/jcarver/code/quantified-self/gmail/sen.se.py 2>&1 >> /var/log/qs-gmail-sense.cron.log
