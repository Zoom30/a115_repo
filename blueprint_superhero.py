import datetime
from typing import Dict, Union, Any, Optional
from decimal import Decimal
from Wallet import Wallet


# def evaluate_money(wallet_dict: dict, currency: str, num: int) -> dict:
#     if type(currency) != str or type(num) != int:
#         raise TypeError
#     amount_spent = {}
#     for key, value in wallet_dict.items():
#         if currency == key and value >= num:
#             amount_spent[key] = num
#             break
#         elif currency == key and value < num:
#             amount_spent[key] = value
#             break
#         else:
#             amount_spent[currency] = 0
#     return amount_spent


class Character:
    def __init__(self, name, age=0):
        self.name: str = name
        self.age: float = 0
        self.date_of_birth: datetime = datetime.datetime.now()
        self.net_worth: Decimal = Decimal("0")
        self.family_members: list[str] = []
        self.superpowers: Optional[Dict[str, Any]] = None
        self.wallet = Wallet()

    def evaluate_superpower(self, dict_of_sp: dict, value: int) -> list:
        if type(dict_of_sp) != dict:
            raise AttributeError
        else:
            list_of_sp = [(key, _value) for key, _value in dict_of_sp.items() if _value >= value]
            return list_of_sp

    def transfer_money(self, char, curr: str, amt: float):
        if curr in self.wallet.capacity and self.wallet.capacity[curr] >= amt:
            self.wallet.spend_money(curr=curr, amt=amt)
            char.wallet.deposit_money()
        else:
            if not self.wallet.capacity[curr] in self.wallet:
                return f"You don't own {curr} yet"
            else:
                return "You don't' have enough amount"
