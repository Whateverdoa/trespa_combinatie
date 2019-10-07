import pandas as pd
import os
import re

# maak een tmp folder
# lees aantal files in folder
# count lengte files if file==file==file dan concat

file_in = pd.read_csv("201953122_met_code.csv", delimiter=";")

aantal_banen = 3  # int(input("aantal_banen: >")) ##tijdelijk
totaal = file_in.aantal.sum()
row = len(file_in)
opb = ongeveer_per_baan = (totaal // aantal_banen)
print(f'aantal rollen= {row}')
afwijking = -50

print(f'totaal van lijst is {totaal} en het gemiddelde over {aantal_banen} banen is {opb}')

benamingen = [f'tmp{naam}.csv' for naam in range(1, aantal_banen + 1)]
print(benamingen)

a = 0

begin_eind_lijst = []
be_LIJST = []

for num in range(len(file_in)):
    b = file_in.aantal.iloc[a:num].sum()
    # print(a, num)

    if num == (len(file_in) - 1):
        c = file_in.aantal.iloc[a:num].sum()
        begin_eind_lijst.append([c, a, num + 1])
        be_LIJST.append([a, num + 1])

        csv_naam = f'tmp/tmp{a}.csv'
        print(csv_naam)
        file_in.iloc[a:(num + 1)].to_csv(csv_naam)
        print("einde")



    elif b >= opb + afwijking:

        csv_naam = f'tmp/tmp{a}.csv'
        print(csv_naam)
        file_in.iloc[a:(num + 1)].to_csv(csv_naam)

        begin_eind_lijst.append([b, a, num])
        be_LIJST.append([a, num + 1])
        be_LIJST.append(f'[{a}:{num}]')
        a = num + 1

    continue

print(begin_eind_lijst)
print(be_LIJST)
print(be_LIJST[0])
print(be_LIJST[0][1:])
print(be_LIJST[0][:1])

begin = be_LIJST[0][1:]
eind = be_LIJST[0][:1]
print(len(begin_eind_lijst))

split_csv = [x for x in os.listdir("tmp") if x.endswith(".csv")]
print(split_csv)
lijst_lengte = len(split_csv)
aantal_per_lijst = 3
use = lijst_lengte // aantal_per_lijst
print(use)
# ------------------------------------------------

regex = r"([.])"
subst = ""
links = []

count = 0
for line in split_csv:
    file_Naam_In = f"tmp/{line}"

    a = "".join(line.strip("\n"))
    result = re.sub(regex, subst, a, 0, re.MULTILINE)
    links.append(f'{result}_')

    # file_Naam_In = f"{naam}_inschiet.csv"
    filenaam_uit = f"vdps/vdp{count}_bewerkt.csv"
    print(file_Naam_In)
    print(filenaam_uit)
    count += 1

    trespa_lijst = pd.read_csv(file_Naam_In, ",", encoding="utf-8")
    print(trespa_lijst[0:1])

    oap = overaantalpercentage = 1  # 1.02 = 2% overlevering
    ee = 4  # = etiketten overlevering handmatig


    # ___________________________________________________________________________________________
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


    df = trespa_lijst[["Colorcode", "beeld", "aantal"]]
    df.to_csv("lijst_in.csv", index=0)

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

# _______________________________________________________________________________________________

vdp_csv = [x for x in os.listdir("vdps") if x.endswith(".csv")]
print(vdp_csv)
