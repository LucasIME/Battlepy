from .basebrobject import BaseBRObject

class Team(BaseBRObject):
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.shard_id = data['shard_id']

