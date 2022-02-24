import asyncio
from elasticsearch import AsyncElasticsearch, Elasticsearch
from elasticsearch.helpers import async_bulk
from config import settings
import common


elasticsearch_api_key=(settings["elasticsearch"]["api_id"], settings['elasticsearch']['api_key'])


es = AsyncElasticsearch(
                    settings['elasticsearch']['host'],
                    api_key=elasticsearch_api_key,
                    ca_certs=settings['elasticsearch']['ca_certs'],
                    verify_certs=settings['elasticsearch']['verify_certs'])


async def gendata(data):
    """Create genertor of bulk data"""
    for doc in data:
        yield doc


async def bulk_index(data):
    """Create generator of data and use Elasticsearch bulk index helper to index docs."""
    await async_bulk(es, gendata(data))
    await es.close()


def bulk_index_data_elasticsearch(data):
    """Call async bulk index function"""
    common.add_doc_id_and_index(data)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bulk_index(data))
    
