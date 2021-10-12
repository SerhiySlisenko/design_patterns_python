from __future__ import annotations

from .singleton import Singleton


class Connection(metaclass=Singleton):
    """
    Connection is Singleton class
    """
    def __init__(self, login: str = 'admin', password: str = '12345'):
        self.__login = login
        self.__password = password

    def connect(self):
        print(f"{self.__login} connected successfully")

    def __str__(self):
        return f"Login: {self.__login}, Password: <secured>"


