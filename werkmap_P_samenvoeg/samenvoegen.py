import pandas as pd

# maak een tmp folder
# lees aantal files in folder
# count lengte files if file==file==file dan concat

file_in = pd.read_csv("201947742_naVV.csv", delimiter=";")

aantal_banen = 24   # int(input("aantal_banen: >")) ##tijdelijk
totaal = file_in.aantal.sum()
row = len(file_in)
opb = ongeveer_per_baan = (totaal // aantal_banen)
print(f'aantal rollen= {row}')
afwijking = -100

print(f'totaal van lijst is {totaal} en het gemiddelde over {aantal_banen} banen is {opb}')

benamingen= [ f'tmp{naam}.csv' for naam in range(1, aantal_banen + 1)]
print(benamingen)

a = 0

begin_eind_lijst = []
be_LIJST=[]

for num in range(len(file_in)):
    b = file_in.aantal.iloc[a:num].sum()
    # print(a, num)

    if num == (len(file_in)-1):
        c=file_in.aantal.iloc[a:num].sum()
        begin_eind_lijst.append([c, a, num+1])
        be_LIJST.append([a, num+1])
        print(f'{c}, {a}:{num+1}')
        print(f'aaar{a} = file_in.iloc[{a}:{num + 1}]')
        print(f'aaar{a}.to_csv("e{a}.csv", ";")')
        print("einde")

    elif b >= opb + afwijking:
        # print(f'{b}, {a}:{num+1}')
        print(f'aaar{a} = file_in.iloc[{a}:{num+1}]')
        print(f'aaar{a}.to_csv("e{a}.csv", ";")')
        begin_eind_lijst.append([b, a, num])
        be_LIJST.append([a, num+1])
        # be_LIJST.append(f'[{a}:{num}]')
        a = num+1

    continue

print(begin_eind_lijst)
print(be_LIJST)
print(be_LIJST[0])
print(be_LIJST[0][1:])
print(be_LIJST[0][:1])

begin=be_LIJST[0][1:]
eind=be_LIJST[0][:1]


aaar = file_in.iloc[164:176]

# aaar.to_csv("ddd.csv", ";")

aaar0 = file_in.iloc[0:14]
aaar0.to_csv("e0.csv", ";")
aaar14 = file_in.iloc[14:31]
aaar14.to_csv("e14.csv", ";")
aaar31 = file_in.iloc[31:42]
aaar31.to_csv("e31.csv", ";")
aaar42 = file_in.iloc[42:60]
aaar42.to_csv("e42.csv", ";")
aaar60 = file_in.iloc[60:77]
aaar60.to_csv("e60.csv", ";")
aaar77 = file_in.iloc[77:103]
aaar77.to_csv("e77.csv", ";")
aaar103 = file_in.iloc[103:115]
aaar103.to_csv("e103.csv", ";")
aaar115 = file_in.iloc[115:121]
aaar115.to_csv("e115.csv", ";")
aaar121 = file_in.iloc[121:131]
aaar121.to_csv("e121.csv", ";")
aaar131 = file_in.iloc[131:141]
aaar131.to_csv("e131.csv", ";")
aaar141 = file_in.iloc[141:164]
aaar141.to_csv("e141.csv", ";")
aaar164 = file_in.iloc[164:176]
aaar164.to_csv("e164.csv", ";")
aaar176 = file_in.iloc[176:202]
aaar176.to_csv("e176.csv", ";")
aaar202 = file_in.iloc[202:209]
aaar202.to_csv("e202.csv", ";")
aaar209 = file_in.iloc[209:217]
aaar209.to_csv("e209.csv", ";")
aaar217 = file_in.iloc[217:226]
aaar217.to_csv("e217.csv", ";")
aaar226 = file_in.iloc[226:254]
aaar226.to_csv("e226.csv", ";")
aaar254 = file_in.iloc[254:268]
aaar254.to_csv("e254.csv", ";")
aaar268 = file_in.iloc[268:277]
aaar268.to_csv("e268.csv", ";")
aaar277 = file_in.iloc[277:300]
aaar277.to_csv("e277.csv", ";")
aaar300 = file_in.iloc[300:303]
aaar300.to_csv("e300.csv", ";")