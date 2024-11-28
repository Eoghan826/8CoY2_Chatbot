import pandas as pd
datafile = pd.read_csv("Pokemon.csv")
count_a = 0
totala
for i, record in datafile.iterrows():
    if 0 < int(record['attack']):
        count_a += 1
        totala += 'attack'
        print(count_a)
        print(totala)
