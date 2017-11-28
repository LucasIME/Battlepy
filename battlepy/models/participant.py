from .basebrobject import BaseBRObject
from .player import Player

class Participant(BaseBRObject):
    def __init__(self, data):
        super().__init__(data)
        self.actor = data['attributes']['actor']
        self.shard_id = data['attributes']['shardId']
        self.attachment = data['attributes']['stats']['attachment']
        self.emote = data['attributes']['stats']['emote']
        self.mount = data['attributes']['stats']['mount']
        self.outfit = data['attributes']['stats']['outfit']

        if 'relationships' in data:
            self.player = Player(data['relationships']['player']['data'])
