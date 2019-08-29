"""
Combination printfiles csv builder
"""
import os
import pandas as pd
from pathlib import Path

pad_in = Path("M:/ESKO/Products/R/RIJVERS/21000000-21000999/898121000371/VDP/csv/")

print(os.listdir(pad_in))

trespa_lijst = pd.read_csv("201911447.csv", ";")
trespa_lijst[0:1]

oap = overaantalpercentage = 1.02  # 1.05 = 5% overlevering


def print_trespa_rolls(colorcode, beeld, aantal):
    """
    Take line from list and build csv for that line
    """

    with open("trespa_combinatie.csv", "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f"Colorcode {colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)

        print(f";{beeld}\n" * int(aantal * oap), end="", file=fn)
        # print(f"{colorcode}, {int(aantal * oap)};leeg.pdf\n", end="", file=fn)

        print(f"Colorcode {colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)
        print(f";stans.pdf\n", end="", file=fn)


df1 = trespa_lijst[["Colorcode", "beeld", "aantal"]]
df1.to_csv("lijst_in.csv", index=0)

new_input_list = []

with open("lijst_in.csv") as input:
    num = 0
    for line in input:
        line_split = line.split(",")

        new_input_list.append(line_split)
        num += 1

list_length = len(new_input_list)

beg = 1
eind = 2


with open("trespa_combinatie.csv", "w", encoding="utf-8") as fn:

    print("beeld1;pdf", file=fn)

with open("trespa_combinatie.csv", "a", encoding="utf-8") as fn:
    for _ in range(list_length - 1):
        a = str(new_input_list[beg:eind][0][0])
        b = str(new_input_list[beg:eind][0][1])
        c = int(new_input_list[beg:eind][0][2])
        print_trespa_rolls(a, b, c)

        beg += 1
        eind += 1
