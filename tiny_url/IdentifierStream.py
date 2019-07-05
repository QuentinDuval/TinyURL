from kazoo.client import KazooClient


class IdentifierStream:
    def __init__(self, zk: KazooClient, reservation_size: int):
        self.zk = zk
        self.reservation_size = reservation_size
        self.current_id = None
        self.last_id = None
        self.counter = zk.Counter("/id", default=1)

    def __next__(self):
        # TODO - race condition here if we use counter.value? how does it work in behind?
        if self.current_id is None or self.current_id >= self.last_id:
            self.counter += self.reservation_size
            self.current_id = self.counter.pre_value + 1
            self.last_id = self.counter.post_value
        else:
            self.current_id += 1
        return self.current_id
