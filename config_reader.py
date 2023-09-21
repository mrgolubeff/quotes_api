import configparser
from dataclasses import dataclass


@dataclass
class DBConnect:
    user: str
    password: str
    ip: str
    port: str


@dataclass
class Config:
    db_connect: DBConnect


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    db_connect = config['db_connect']

    return Config(
        db_connect=DBConnect(
            user=db_connect['user'],
            password=db_connect['password'],
            ip=db_connect['ip'],
            port=db_connect['port'],
        )
    )
