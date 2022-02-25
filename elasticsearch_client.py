import asyncio
from asyncio.log import logger
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from config import settings
import common


if settings["elasticsearch"]["username"] and settings['elasticsearch']['password'] is not None:
    http_auth = (settings["elasticsearch"]["username"], settings['elasticsearch']['password'])
else:
    http_auth = None


if settings["elasticsearch"]["api_id"] and settings['elasticsearch']['api_key'] is not None:
    api_key = (settings["elasticsearch"]["api_id"], settings['elasticsearch']['api_key'])
else:
    api_key = None


es = AsyncElasticsearch(
        settings['elasticsearch']['host'],
        cloud_id=settings['elasticsearch']['cloud_id'],
        http_auth=http_auth,
        api_key=api_key,
        ca_certs=settings['elasticsearch']['ca_certs'],
        verify_certs=settings['elasticsearch']['verify_certs']
    )


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
    logger.info("Indexing to Elasticsearch")
