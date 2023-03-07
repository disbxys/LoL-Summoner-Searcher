from typing import Any, Dict, List, Optional

import requests

import config as Consts

class MissingAPIKeyException(Exception):
    pass

class RiotAPI():

    def __init__(
            self,
            api_key: str,
            region: Consts.Region = Consts.Region.NORTH_AMERICA):
        if api_key is None: raise MissingAPIKeyException

        self.api_key = api_key
        self.region = region

    def _request(
            self,
            api_url: str,
            params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
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

    def get_summoner_by_name(self, name: str) -> Dict[str, Any]:
        """Return a dict of player data."""
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['version'],
            names=name
        )
        return self._request(api_url)
    
    def get_league_queue(
            self,
            queue: Consts.LEAGUE_QUEUE,
            tier: Consts.LEAUGE_TIER,
            div: Optional[Consts.LEAGUE_DIVISION] = None) -> List[Dict[str, Any]]:
        """
        Return a sorted list of players depending on the ranked queue, division,
        and tier.
        """

        # Master, Grandmaster, and Challenger tiers are special tiers that are
        # not split into divisions.
        if tier.lower() in ["challenger", "grandmaster", "master"]:
            api_url = Consts.URL["master_plus_ladder_by_queue"].format(
                version=Consts.API_VERSIONS["version"],
                tier=f"{tier}leagues",
                queue=queue
            )
        else:
            api_url = Consts.URL["ladder_by_queue"].format(
                version=Consts.API_VERSIONS["version"],
                queue=queue,
                tier=tier,
                division=div
            )
        return self._request(api_url)