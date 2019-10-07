import pandas as pd
import os

# maak een tmp folder
# lees aantal files in folder
# count lengte files if file==file==file dan concat

file_in = pd.read_csv("201953122_met_code.csv", delimiter=";")

aantal_banen = 3 # int(input("aantal_banen: >")) ##tijdelijk
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
use = lijst_lengte//aantal_per_lijst
print(use)



