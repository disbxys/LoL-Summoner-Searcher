from typing_extensions import Literal

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

LEAGUE_DIVISION = Literal["I", "II", "III", "IV"]
LEAUGE_TIER = Literal[
    "CHALLENGER", "GRANDMASTER", "MASTER",
    "DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE"
]
LEAGUE_QUEUE = Literal["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]

URL = {
    'base': 'https://{region}.api.riotgames.com/{url}',
    'summoner_by_name': 'lol/summoner/v{version}/summoners/by-name/{names}',
    'ladder_by_queue': 'lol/league/v{version}/entries/{queue}/{tier}/{division}',
    'master_plus_ladder_by_queue': 'lol/league/v{version}/{tier}/by-queue/{queue}',
    'grandmasters_ladder_by_queue': 'lol/league/v{version}/grandmasterleagues/by-queue/{queue}',
    'challengers_ladder_by_queue': 'lol/league/v{version}/challengerleagues/by-queue/{queue}',
}