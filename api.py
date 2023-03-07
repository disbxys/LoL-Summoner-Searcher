import requests

import config as Consts

class MissingAPIKeyException(Exception):
    pass

class RiotAPI():

    def __init__(self, api_key, region=Consts.REGIONS['North America']):
        if api_key is None: raise MissingAPIKeyException

        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params=None):
        params = dict() if params == None else params
        headers = {'X-Riot-Token': self.api_key}
        
        response = requests.get(
            Consts.URL['base'].format(
                region=self.region,
                url=api_url
            ),
            params=params,
            headers=headers
        )
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['version'],
            names=name
        )
        return self._request(api_url)
    
    def get_league_queue(
            self,
            queue:Consts.LEAGUE_QUEUE,
            tier:Consts.LEAUGE_TIER,
            div:Consts.LEAGUE_DIVISION):
        
        api_url = Consts.URL["ladder_by_queue"].format(
            version=Consts.API_VERSIONS["version"],
            queue=queue,
            tier=tier,
            division=div
        )
        return self._request(api_url)