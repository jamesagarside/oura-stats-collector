import common
import requests, logging
from config import settings
from datetime import date, timedelta

logger = logging.getLogger('root')

# Generates timeframe based on current date.
start_date =  date.today().strftime("%Y-%m-%d")
end_date = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
period = {'start_date': start_date, 'end_date': end_date}


def call_api(url, time_frame):
    """Call Oura API and returns JSON data"""
    params=time_frame
    headers = {'Authorization': 'Bearer %s' % settings['oura_personal_access_token']}
    response = requests.request('GET', url, headers=headers, params=params)
    data = common.rename_field(response.json()['data'], "timestamp", "@timestamp")
    return data


def get_heartrate():
    """Get heartrate for specified time period"""
    url = 'https://api.ouraring.com/v2/usercollection/heartrate'
    logger.info("Getting Heartrate data from: %s", url)
    response = call_api(url, period)
    data = common.add_field(response, "event.dataset", "heartrate")
    return data


def get_daily_activity():
    """Get heartrate for specified time period"""
    url = 'https://api.ouraring.com/v2/usercollection/daily_activity'
    logger.info("Getting Daily Activity data from: %s", url)
    response = call_api(url, period)
    data = common.add_field(response, "event.dataset", "activity")
    return data


def get_tags():
    """Get heartrate for specified time period"""
    url = 'https://api.ouraring.com/v2/usercollection/tag'
    logger.info("Getting tag data from: %s", url)
    response = call_api(url, period)
    data = common.add_field(response, "event.dataset", "tags")
    return data
