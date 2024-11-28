import pandas as pd
datafile = pd.read_csv("Pokemon.csv")
count_a = 0
totala = 0
for i, record in datafile.iterrows():
    if 80 < int(record['Sp. Atk']):
        count_a += 1
        totala += int(record['Sp. Atk'])
        print(count_a)
        print(totala)
