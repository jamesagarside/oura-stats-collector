# Oura Stats Collector

A program to collect Oura Ring stats from Oura cloud and Export them to Elasticsearch.

The script will pull the following datasets from Oura at the specified poll rate (default = 5 minutes):
* Heartrate
* Daily Activity
* Tags

## Prerequisites
* Git
* Python 3.7+
* Docker (If doploying using Docker)


## Usage
### Getting ready
1. Clone the repo `git clone git@github.com:jamesagarside/oura-stats-collector.git`
2. Change directory `cd oura-stats-collector`
3. Copy example settings file and update with your values `cp settings.example.yaml settings.yaml`. Reference [settings](##Settings) for possible settings. 

### Deploy with Docker (Recommended)
1. Build and deploy using Docker Compose `docker-compose up -d`  

### Run with Python
1. Install requirements `pip -r requirements.txt`
2. Run script with `python3 main.py` 

## Settings             
| Setting                       | Description                                       | Default       | Type      |
| ----------------------------  | ------------------------------------------------- | :---------:   | -------   |
| log_level                     | Log level (DEBUG, INFO, WARN, ERROR, CRITICAL)    | INFO          |           |
| poll_rate                     | The rate at which to pull Oura Cloud stats        | 5             |           |
| oura_personal_access_token    | Personal access token generated within cloud app  | None          |           |
| elasticsearch.cloud_id        | Elastic Cloud cloud_id string                     | None          |           |
| elasticsearch.host            | Elasticsearch host URL                            | None          |           |
| elasticsearch.ca_certs        | CA Certificate chain for Elasticsearch cluster    | None          |           |
| elasticsearch.verify_certs    | Verify certificate from Elasticsearch cluster     | None          |           |
| elasticsearch.username        | Username for Elasticsearch user                   | None          |           |
| elasticsearch.password        | Password for Elasticsearch user                   | None          |           |
| elasticsearch.api_id          | API key ID for Elasticsearch cluster              | None          |           |
| elasticsearch.api_key         | API key for Elasticsearch cluster                 | None          |           |
| elasticsearch.index           | Index of which to store Oura data                 | oura-stats    |           |

## TODO
* Add support for settings from Environment Variables
* Optimise schema
* Add local file export
* Add support for Oura API V1

