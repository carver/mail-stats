
example crons

```
45 23 * * * python /home/jcarver/code/quantified-self/gmail/record.py 2>&1 >> /var/log/qs-gmail-local.cron.log
1-59/15 * * * * cd /home/jcarver/code/mail-stats && . venv/bin/activate && python sen.se.py >>/tmp/qs-gmail-sense.cron.log 2>&1
```
