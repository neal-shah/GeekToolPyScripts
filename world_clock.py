import pytz
from pytz import timezone
from datetime import datetime, timedelta

fmt = '%H:%M'

timezones = {
    "London": timezone('Europe/London'),
    "New York": timezone('America/New_York'),
    "Singapore": timezone('Asia/Singapore')
}

def get_localised_time(city):
    now_utc = datetime.now(timezone('UTC'))
    city_time = now_utc.astimezone(city)
    return city_time

for k, v in timezones.items():
    time = get_localised_time(v)
    print('{} : {}'.format(time.strftime(fmt), k))