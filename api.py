from typing import Any, Dict, Optional

import requests

import config as Consts

class MissingAPIKeyException(Exception):
    pass

class RiotAPI():

    def __init__(
            self,
            api_key: Optional[str] = None,
            region: Consts.Region = Consts.Region.NORTH_AMERICA):
        
        # If an api key is not passed in, try to grab the api key
        # from the consts file.
        if (api_key is None) and (Consts.API_KEY is None):
            raise MissingAPIKeyException
        else:
            self.api_key = api_key or Consts.API_KEY or ""

        if isinstance(region, Consts.Region):
            self.region = region.value

    def _request(
            self,
            api_url: str,
            params: Optional[Dict[str, str]] = None
    ) -> Any:
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
            queue: Consts.Queue,
            tier: Consts.Tier,
            div: Optional[Consts.Division] = None
    ) -> Any:
        """
        Return a sorted list of players depending on the ranked queue, division,
        and tier.
        """

        # Master, Grandmaster, and Challenger tiers are special tiers that are
        # not split into divisions.
        if tier.upper() in Consts.Tier:
            api_url = Consts.URL["master_plus_ladder_by_queue"].format(
                version=Consts.API_VERSIONS["version"],
                tier=f"{tier.lower()}leagues",
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