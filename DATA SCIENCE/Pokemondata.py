import pandas as pd
datafile = pd.read_csv("Pokemon.csv")
count_a = 0
totala = 0
for i, record in datafile.iterrows():
    if 0 < int(record['Attack']):
        count_a += 1
        totala += int(record['Attack'])
        print(count_a)
        print(totala)
