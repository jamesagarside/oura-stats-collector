import hashlib, json
from config import settings


def add_field(data: list, key: str, value):
    """Add a field to each dictionary"""
    updated_data = []
    for doc in data:
        doc.update({key: value})
        updated_data.append(doc)
    return updated_data


def rename_field(data: list, source_field, desitination_field):
    """Rename a field for each dictionary"""
    updated_data = []
    for doc in data:
        doc[desitination_field] = doc.pop(source_field)
        updated_data.append(doc)
    return updated_data


def hash_dict(d):
    """Returns the hash of a supplied dictionary"""
    return hashlib.md5(json.dumps(d, sort_keys=True).encode('utf-8')).hexdigest()


def add_doc_id_and_index(data):
    """Adds index and id to documets. ID is a hash of the original document"""
    updated_data = []
    for doc in data:
        doc.update({"_id": hash_dict(doc), "_index": settings['elasticsearch']['index']})
        updated_data.append(doc)
    return updated_data