import requests
import json
import config
import pytz
from datetime import datetime, timedelta

def postToServer(url, payload):
    """ Post data to a SensorThings API server """
    headers = {'content-type': 'application/json'}
    r = requests.post(url,
                      data=json.dumps(payload), headers=headers, auth=config.STA_AUTH)
    return r


def getTime(seconds):
    """ This will convert n seconds into d days, h hours, m minutes, and s seconds """
    sec = timedelta(seconds=int(seconds))
    d = datetime(1, 1, 1) + sec

    print("DAYS:HOURS:MIN:SEC")
    print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))


def localToUTC(local, timezone, format):
    """ Convert loacl time to the UTC time """
    local_tz = pytz.timezone(timezone)
    date = datetime.strptime(local, format)
    local_dt = local_tz.localize(date, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt
