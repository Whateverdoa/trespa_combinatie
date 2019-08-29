"""
Step 2
use pandas and or numpy / csv

to split the file in three columns

readlines than check for blanco to split file

make new csv files

concat them


i want to add all the numbers in a specific column "aantal
"""

import csv
import pandas as pd
import numpy as np

# dir(csv)
# help(csv)

with open('trespa_combinatie.csv', encoding="utf-8") as file:
    new = ["".join(line.strip("\n")) for line in file]

trespa_dataframe = pd.read_csv("201917453Inschiet.csv", ";")

aantal = trespa_dataframe['aantal']
print(aantal)

print(aantal.sum(axis=0, skipna=True))
