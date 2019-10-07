"""
Combination printfiles csv builder
generalize this please
# make it TDD
watch out for floats!!!
let op input file met kommas uitzoeken of het misschien niet beter is om excel file in te voeren
"""
import pandas as pd


file_Naam_In = "201951348_inschiet.csv"
filenaam_uit = "201951348_inschiet_bewerkt.csv"

trespa_lijst = pd.read_csv(file_Naam_In, ";", encoding="utf-8")
trespa_lijst[0:1]

oap = overaantalpercentage = 1   # 1.02 = 2% overlevering
ee = 4                           #  = etiketten overlevering handmatig


def print_trespa_rolls(colorcode, beeld, aantal):
    """
    Take line from list and build csv for that line
    """

    with open(filenaam_uit, "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f"{colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)

        print(f";{beeld}\n" * int(aantal * oap + ee), end="", file=fn)
        # print(f"{colorcode}, {int(aantal * oap)};leeg.pdf\n", end="", file=fn)

        print(f"{colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)
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


with open(filenaam_uit, "w", encoding="utf-8") as fn:

    print("beeld1;pdf1", file=fn)

with open(filenaam_uit, "a", encoding="utf-8") as fn:
    for _ in range(list_length - 1):
        a = str(new_input_list[beg:eind][0][0])
        b = str(new_input_list[beg:eind][0][1])
        c = int(new_input_list[beg:eind][0][2])
        print_trespa_rolls(a, b, c)

        beg += 1
        eind += 1
