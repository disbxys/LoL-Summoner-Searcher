from dotenv import load_dotenv
from enum import Enum
import os
from typing_extensions import Literal

load_dotenv()       # load env file

API_KEY = os.getenv("API_KEY", "")

API_VERSIONS = {
    'version': '4'
}

class Region(str, Enum):
    BRAZIL = "br1"
    EUROPE_NE = "eun1"
    EUROPE_WEST = "enw1"
    JAPAN = "jp1"
    KOREA = "kr"
    LATIN_AMERICA_NORTH = "la1"
    LATIN_AMERICA_SOUTH = "la2"
    NORTH_AMERICA = "na1"
    OCEANIA = "oc1"
    PBE = "pbe1"
    PHILLIPPINES = "ph2"
    RUSSIA = "ru"
    SINGAPORE = "sg2"
    THAILAND = "th2"
    TURKEY = "tr1"
    VIETNAM = "vn2"

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