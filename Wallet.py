import csv
import os.path


def write_to_file(fn, mode, dictionary):
    with open(fn, mode) as file:
        default_writer = csv.writer(file)
        for k, v in dictionary.items():
            default_writer.writerow([k, v])

class Wallet:
    def __init__(self):
        self.capacity = {}
        self.currency = ""
        self.amount = 0

    def display_amount(self):
        if os.path.isfile("Wallet.csv"):
            with open(file="Wallet.csv", mode="r") as wallet_file:
                reader = csv.reader(wallet_file)
                return {row[0]: row[1] for row in reader}
        else:
            return self.capacity

    def spend_money(self, curr: str, amt: float):
        pass
        # if curr not in self.capacity:
        #     return "You don't own the currency"
        # if self.capacity[curr] >= amt:
        #     # self.amount = self.amount - amt
        #     self.capacity[curr] -= amt
        #     return f"You have spent {amt} {curr} and you have {self.amount} left"
        # else:
        #     return "Not enough amount"

    def deposit_money(self, curr: str, amt: float):
        file_name = "Wallet.csv"
        if os.path.isfile(file_name):
            with open(file_name, mode="r") as wallet_file:
                reader = csv.reader(wallet_file)
                temp_dict = {row[0]: float(row[1]) for row in reader}
                temp_dict[curr] += amt if curr in temp_dict else amt
            write_to_file(fn=file_name, mode="w", dictionary=temp_dict)

        else:
            write_to_file(fn=file_name, mode="w", dictionary=self.capacity)
            with open("Wallet.csv", mode="a") as wallet_file:
                writer = csv.writer(wallet_file)
                writer.writerow([curr, amt])


lv = Wallet()
lv.currency = "Pounds"
lv.amount = 2300
lv.capacity[lv.currency] = lv.amount

print(lv.display_amount())
lv.deposit_money(curr="Euros", amt=50)
lv.deposit_money(curr="Euros", amt=123)
lv.deposit_money(curr="Dollar", amt=340)
print(lv.display_amount())
