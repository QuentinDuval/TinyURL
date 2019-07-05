from tiny_url.AccessCache import AccessCache
from tiny_url.IdentifierStream import IdentifierStream
from tiny_url.Storage import Storage
from kazoo.client import KazooClient


class TinyURL:
    def __init__(self, url_prefix):
        self.url_prefix = url_prefix + "/"
        self.storage = Storage()
        self.zk = KazooClient(hosts='127.0.0.1:2181')  # TODO - inject zookeeper information
        self.zk.start()
        self.zk.add_listener(lambda zk_state: print(zk_state))
        self.identifiers = IdentifierStream(zk=self.zk, reservation_size=10)
        self.cache = AccessCache()

    def add_link(self, full_url):
        identifier = next(self.identifiers)
        identifier = str(identifier)
        self.storage.add_link(identifier, full_url)
        return self.url_prefix + identifier

    def get_link(self, tiny_url):
        # TODO - search cache first
        return self.storage.get_full(tiny_url)
