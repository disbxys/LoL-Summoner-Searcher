# from dotenv import load_dotenv
from enum import Enum, EnumMeta
import os
# from typing_extensions import Literal


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True    


class BaseEnum(Enum, metaclass=MetaEnum):
    pass

# load_dotenv()       # load env file

API_KEY = os.getenv("API_KEY", "")

API_VERSIONS = {
    'version': '4'
}

class Region(str, BaseEnum):
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

# LEAGUE_DIVISION = Literal["I", "II", "III", "IV"]
class Division(str, BaseEnum):
    I = "I"
    II = "II"
    III = "III"
    IV = "IV"

# LEAUGE_TIER = Literal[
#     "CHALLENGER", "GRANDMASTER", "MASTER",
#     "DIAMOND", "EMERALD", "PLATINUM", "GOLD", "SILVER", "BRONZE"
# ]
class Tier(str, BaseEnum):
    CHALLENGER = "CHALLENGER"
    GRANDMASTER = "GRANDMASTER"
    MASTER = "MASTER"
    DIAMOND = "DIAMOND"
    EMERALD = "EMERALD"
    PLATINUM = "PLATINUM"
    GOLD = "GOLD"
    SILVER = "SILVER"
    BRONZE = "BRONZE"

# LEAGUE_QUEUE = Literal["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]
class Queue(str, BaseEnum):
    SOLO_5V5 = "RANKED_SOLO_5x5"
    FLEX_SR = "RANKED_FLEX_SR"
    FLEX_TT = "RANKED_FLEX_TT"

URL = {
    'base': 'https://{region}.api.riotgames.com/{url}',
    'summoner_by_name': 'lol/summoner/v{version}/summoners/by-name/{names}',
    'ladder_by_queue': 'lol/league/v{version}/entries/{queue}/{tier}/{division}',
    'master_plus_ladder_by_queue': 'lol/league/v{version}/{tier}/by-queue/{queue}',
    'grandmasters_ladder_by_queue': 'lol/league/v{version}/grandmasterleagues/by-queue/{queue}',
    'challengers_ladder_by_queue': 'lol/league/v{version}/challengerleagues/by-queue/{queue}',
}