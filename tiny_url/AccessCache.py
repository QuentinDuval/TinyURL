import redis


class AccessCache:
    def __init__(self):
        self.redis_connection = redis.Redis()

    def put(self, identifier, full_url):
        self.redis_connection.set(identifier, full_url)

    def get(self, identifier):
        return self.redis_connection.get(identifier)
