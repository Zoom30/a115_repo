import datetime


class Character:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.date_of_birth: datetime = datetime.datetime.now()
        self.networth: float = 0
        self.family_members = []


ironman = Character()
ironman.name = "Tony"
ironman.age = 36
ironman.date_of_birth = datetime.date(year=1986, month=3, day=15)
# print(type(ironman.date_of_birth))
# print(type(datetime.datetime.now()))
age = (datetime.datetime.now().date() - ironman.date_of_birth)

ironman.networth = 20.5
ironman.family_members = [50, "Natasha", "Nick Fury"]

haris = ironman
haris.name = "haris"
print(ironman.name)
print(haris.name)