import pandas as pd
datafile = pd.read_csv("Pokemon.csv")
count_a = 0
totala = 0
for i, record in datafile.iterrows():
    if 'Dragon' == int(record['Total']):
        count_a += 1
        totala += int(record['Total'])
        print(count_a)
