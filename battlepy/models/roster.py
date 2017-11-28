from .basebrobject import BaseBRObject
from .participant import Participant

class Roster(BaseBRObject):
    def __init__(self, data):
        super().__init__(data)
        self.shard_id = data['attributes']['shard_id']
        self.score = data['attributes']['score']
        self.side = data['attributes']['side']
        self.won = data['won']

        self.participants = []
        for participant in data['relationships']['participants']['data']:
            self.participants.append(Participant(participant))

        if 'team' in data['relationships']:
            self.team = Team(data['relationships']['team'])

