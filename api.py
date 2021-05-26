import requests

import config as Consts

class RiotAPI():

    def __init__(self, api_key, region=Consts.REGIONS['North America']):
        self.api_key = api_key
        self.region = region


    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}

        for key, value in params.items():
            if key not in args:
                args[key] = value
        
        response = requests.get(
            Consts.URL['base'].format(
                region=self.region,
                url=api_url
            ),
            params=args
        )
        
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['version'],
            names=name
        )
        return self._request(api_url)

    
