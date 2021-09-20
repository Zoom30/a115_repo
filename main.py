import datetime


class Character:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.date_of_birth: datetime = datetime.datetime.now()
        self.networth: float = 0
        self.family_members = []
        self.superpowers = None


superman = Character()
superman.name = "Tony"
superman.age = 36
superman.date_of_birth = datetime.date(year=1986, month=3, day=15)
# print(type(ironman.date_of_birth))
# print(type(datetime.datetime.now()))
age = (datetime.datetime.now().date() - superman.date_of_birth)
superman.networth = 20.5
superman.family_members = [50, "Natasha", "Nick Fury"]
superman.superpowers = {"flying", "heat vision", "super strength", "super speed", "invincibility"}
print(f"""
Superman has the following powers:
{superman.superpowers}
""")

favourite_power = input("What is your fav superpower?\n")
if favourite_power in superman.superpowers:
    print("power already aquired")
else:
    superman.superpowers.add(favourite_power)
print(superman.superpowers)

