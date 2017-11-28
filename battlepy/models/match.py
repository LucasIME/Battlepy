from .basebrobject import BaseBRObject
from .roster import Roster
from .round import Round
from .participant import Participant

class Match(BaseBRObject):
    def __init__(self, data):
        super().__init__(data)
        self.created_at = data['attributes']['createdAt']
        self.duration = data['attributes']['duration']
        self.game_mode = data['attributes']['gameMode']
        self.patch = data['attributes']['patchVersion']
        self.shard_id = data['attributes']['shardId']
        self.map_id = data['attributes']['stats']['mapID']
        self.type = data['attributes']['stats']['type']
        self.rosters = []
        for roster in data['relationships']['rosters']['data']:
            self.rosters.append(Roster(roster))
        self.rounds = []
        for round in data['relationships']['rounds']['data']:
            self.rounds.append(Round(round))
        self.spectators = [] 
        for participant in data['relationships']['spectators']['data']:
            self.spectators.append(Participant(participant))
        self.telemetry_url = data['relationships']['assets']['data'][0]['attributes']['URL']

