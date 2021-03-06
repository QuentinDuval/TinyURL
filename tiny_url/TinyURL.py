from colorama import Fore
from kazoo.client import KazooClient

from tiny_url.AccessCache import AccessCache
from tiny_url.Configuration import Configuration
from tiny_url.IdentifierStream import IdentifierStream
from tiny_url.Storage import Storage


class TinyURL:
    def __init__(self, configuration: Configuration):
        self.url_prefix = configuration.domain_name + ":" + str(configuration.port) + "/"
        self.storage = Storage(configuration=configuration)
        self.zk = KazooClient(hosts=configuration.zookeeper_host)
        self.zk.start()
        self.zk.add_listener(lambda zk_state: print(zk_state))
        self.identifiers = IdentifierStream(zk=self.zk, reservation_size=10)
        self.cache = AccessCache()

    def add_link(self, full_url):
        identifier = next(self.identifiers)
        identifier = str(identifier)
        self.storage.add_link(identifier, full_url)
        self.cache.put(identifier, full_url)
        return self.url_prefix + identifier

    def get_link(self, identifier):
        result = self.cache.get(identifier)
        if result is not None:
            return result

        print(Fore.BLUE + "Cache miss for " + identifier + Fore.RESET)
        result = self.storage.get_full(identifier)
        self.cache.put(identifier, result)
        return result
