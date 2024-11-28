import pandas as pd
datafile = pd.read_csv("Pokemon.csv")
count_a = 0
for i, record in datafile.iterrows():
    if 80 == int(record['HP']):
        count_a += 1
        print(f"This pokemons HP is {record['HP']}")
        print(count_a)
