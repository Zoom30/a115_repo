from blueprint_superhero import *
import datetime

superman = Character()
superman.name = "Clark"
superman.age = 36
superman.date_of_birth = datetime.date(month=3, day=29, year=1985)
# print(type(ironman.date_of_birth))
# print(type(datetime.datetime.now()))
age = (datetime.datetime.now().date() - superman.date_of_birth)
superman.net_worth = 20.5
superman.family_members = ["50", "Natasha", "Nick Fury"]
superman.superpowers = dict(
    {"flying": 100, "heat vision": 75, "super strength": 45, "super speed": 89, "invincibility": 40})
print(f"""
Superman has the following powers:
{superman.superpowers}
""")

# favourite_power = input("What is your fav superpower?\n")
# if favourite_power in superman.superpowers:
#     print("power already acquired")
# else:
#     superman.superpowers.add(favourite_power)
# print(superman.superpowers)

# power_check = input("Enter a superpower: ").lower()
# if superman.superpowers[power_check] >= 80:
#     print("SUPER COOL")
# elif superman.superpowers[power_check] > 50:
#     print("COOL")
# else:
#     print("YEAAAH AVERAGE")

wallet: dict = {"dollars": 170, "pounds": 50, "euros": 100}
superman.wallet.update(wallet)
print(superman.wallet)

currency_input = input("specify the currency type: ")
amount = int(input("How much do you want to spend: "))
print(evaluate_money(wallet_dict=superman.wallet, currency=currency_input, num=amount))
print(evaluate_superpower(superman.superpowers, 45))
