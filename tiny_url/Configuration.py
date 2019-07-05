from dataclasses import dataclass
import json


@dataclass()
class Configuration:
    domain_name: str
    port: int
    zookeeper_host: str
    postgres_host: str
    postgres_secrets: str

    @classmethod
    def read_from(cls, configuration_file_path):
        with open(configuration_file_path) as config:
            data = json.loads(config.read())
            return Configuration(
                domain_name=data['domain_name'],
                port=data['port'],
                zookeeper_host=data['zookeeper'],
                postgres_host=data['postgres'],
                postgres_secrets=data['postgres_secrets']
            )
