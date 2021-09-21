import datetime


class Character:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.date_of_birth: datetime = datetime.datetime.now()
        self.networth: float = 0
        self.family_members = []
        self.superpowers = None
        self.wallet = {}


superman = Character()
superman.name = "Clark"
superman.age = 36
superman.date_of_birth = datetime.date(year=1986, month=3, day=15)
# print(type(ironman.date_of_birth))
# print(type(datetime.datetime.now()))
age = (datetime.datetime.now().date() - superman.date_of_birth)
superman.networth = 20.5
superman.family_members = [50, "Natasha", "Nick Fury"]
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

power_check = input("Enter a superpower: ").lower()
if superman.superpowers[power_check] >= 80:
    print("SUPER COOL")
elif superman.superpowers[power_check] > 50:
    print("COOL")
else:
    print("YEAAAH AVERAGE")

wallet = {"dollars": 170, "pounds": 50, "euros": 100}
superman.wallet.update(wallet)
print(superman.wallet)
