import pandas as pd
import re

trespa_base = pd.read_csv("stap2/201942818_lijst.csv", ";")

df1 = pd.DataFrame(trespa_base)
a = df1['Colorcode']
b = df1['num']

regex = r"([. -])"
subst = ""

links = []
for line in a:
    a = "".join(line.strip("\n"))
    result = re.sub(regex, subst, a, 0, re.MULTILINE)
    links.append(f'{result}-')


rechts = [str(line) for line in b]

# code = [i + j for i, j in zip(links, rechts)]

code_word = pd.DataFrame([i + j for i, j in zip(links, rechts)])

df1['code'] = code_word
print(df1)
df1.to_csv("201942818_lijst_metcode.csv", ";", encoding=' utf-8')