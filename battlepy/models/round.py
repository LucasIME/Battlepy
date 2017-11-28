from .basebrobject import BaseBRObject
from .participant import Participant

class Round(BaseBRObject):
    def __init__(self, data):
        super().__init__(data)
        self.duration = data['attributes']['duration']
        self.ordinal = data['attributes']['ordinal']
        self.winning_team = data['attributes']['stats']['winningTeam']

        self.participants = []
        for participant in data['relationships']['participants']['data']:
            self.participants.append(Participant(participant)) 
