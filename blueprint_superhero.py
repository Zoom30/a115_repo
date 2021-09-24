import datetime
from typing import Dict, Union, Any


def evaluate_money(wallet_dict: dict, currency: str, num: int) -> dict:
    amount_spent = {}
    for key, value in wallet_dict.items():
        if currency == key and value >= num:
            amount_spent[key] = num
            break
        elif currency == key and value < num:
            amount_spent[key] = value
            break
        else:
            amount_spent[currency] = 0
    return amount_spent


def evaluate_superpower(dict_of_sp: dict, value: int) -> list:
    list_of_sp = [(key, _value) for key, _value in dict_of_sp.items() if _value >= value]
    return list_of_sp


class Character:
    def __init__(self):
        self.name: str = ""
        self.age: float = 0
        self.date_of_birth: datetime = datetime.datetime.now()
        self.net_worth: float = 0
        self.family_members: list[str] = []
        self.superpowers: Dict[str, Any] = None
        self.wallet: Dict[Any, Any] = {}

