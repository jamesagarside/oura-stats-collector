import yaml


default_values = {
    "log_level": "INFO",
    "poll_rate": 5,
    "oura_personal_access_token": None,
    "elasticsearch":{
        "cloud_id": None,
        "host": None,
        "ca_certs": None,
        "verify_certs": True,
        "username": None,
        "password": None,
        "api_id": None,
        "api_key": None,
        "index" : "oura-stats"
    }
}


with open("settings.yaml", "r", encoding="utf_8") as stream:
    try:
        settings = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


def setdefault_recursively(tgt, default):
    """Set default settings values"""
    for k in default:
        if isinstance(default[k], dict): # if the current item is a dict,
            # expand it recursively
            setdefault_recursively(tgt.setdefault(k, {}), default[k])
        else:
            # ... otherwise simply set a def
            tgt.setdefault(k, default[k])
    return tgt

settings = setdefault_recursively(settings, default_values)
