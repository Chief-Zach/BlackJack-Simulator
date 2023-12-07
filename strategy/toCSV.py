import csv
import re

with open("BasicStrategy.csv", "r") as file:
    strat = re.sub(";", ",", file.read())
    print(strat)

with open("BasicStrategy1.csv", "w") as file:
    file.write(strat)