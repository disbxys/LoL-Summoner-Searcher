API_KEY = 'Insert your api key here'


API_VERSIONS = {
    'version': '4'
    }


# Dictionary of all regions with key
# as full name of region and value
# as regional endpoint marker
REGIONS = {
    'Brazil': 'br',
    'Europe NE': 'eun1',
    'Europe West': 'euw1',
    'Japan': 'jp1',
    'Korea': 'kr',
    'Latin America North': 'la1',
    'Latin America South': 'la2',
    'North America': 'na1',
    'Oceania': 'oc1',
    'Turkey': 'tr1',
    'Russia': 'ru',
    'PBE': 'pbe1'
    }



URL = {
    'base': 'https://{region}.api.riotgames.com/{url}',
    'summoner_by_name': 'lol/summoner/v{version}/summoners/by-name/{names}',
    'ladder_by_queue': 'lol/league/v4/entries/{queue}/{tier}/{division}'
    }

HEADER = {
    'API-KEY': API_KEY
    }
