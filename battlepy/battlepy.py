import requests

class Battlepy():
    MATCH_URL = "https://api.dc01.gamelockerapp.com/shards/global/matches"
    PLAYER_URL = "https://api.dc01.gamelockerapp.com/shards/global/players"

    def __init__(self, key):
        self.header = {
	    "Authorization": key, 
	    "Accept": "application/vnd.api+json"
	}

    def get_matches(self, page_offset=None, page_limit=None, with_player_names=None, with_player_ids=None, with_team_names=None):
        query = {}

        if isinstance(page_offset, int):
            query['page[offset]'] = page_offset

        if isinstance(page_limit, int):
            query['page[limit]'] = page_limit

        if isinstance(with_player_names, list):
            query['filter[playerNames]'] = ','.join(with_player_names)

        if isinstance(with_player_ids, list):
            query['filter[playerIds]'] = ','.join(with_player_ids)

        if isinstance(with_team_names, list):
            query['filter[teamNames]'] = ','.join(with_team_names)

        return requests.get(self.MATCH_URL, headers=self.header, params=query).json()

    def get_match_with_id(self, id):
        return requests.get(self.MATCH_URL + "/" + str(id), headers=self.header).json()
    
    def get_players(self, player_names=None, player_ids=None):
        query = {}
        
        if isinstance(player_names, list):
            query['filter[playerNames]'] = ','.join(player_names)

        if isinstance(player_ids, list):
            query['filter[playerIds'] = ','.join(player_ids)

        return requests.get(self.PLAYER_URL, headers=self.header, params=query).json()

    def get_player_with_id(self, id):
        return requests.get(self.PLAYER_URL + "/" + str(id), headers=self.header).json()

