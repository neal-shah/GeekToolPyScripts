#!/usr/local/bin/python3

from datetime import datetime, timedelta
from pytz import timezone

fmt = '%H:%M'

def get_localised_time(city):
    now_utc = datetime.now(timezone('UTC'))
    city_time = now_utc.astimezone(city)
    return city_time


def get_world_times():
    timezones = {
        "London": timezone('Europe/London'),
        "New York": timezone('America/New_York'),
        "Singapore": timezone('Asia/Singapore')
    }

    for k, v in timezones.items():
        time = get_localised_time(v)
        print('{} : {}'.format(time.strftime(fmt), k))


get_world_times()
