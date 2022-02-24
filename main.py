import logging, sys
import elasticsearch_client, oura_client
from config import settings
from time import sleep


# Configure Logger
logger = logging.getLogger('root')
logger.setLevel(settings['log_level'])
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(settings['log_level'])
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



def job():
    """Main job"""
    elasticsearch_client.bulk_index_data_elasticsearch(oura_client.get_heartrate())
    elasticsearch_client.bulk_index_data_elasticsearch(oura_client.get_daily_activity())
    elasticsearch_client.bulk_index_data_elasticsearch(oura_client.get_tags())


while True:
    job()
    sleep(settings['poll_rate']*60)
    