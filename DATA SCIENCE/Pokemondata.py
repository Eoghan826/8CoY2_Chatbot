import pandas as pd
datafile = pd.read_csv("Pokemon.csv")
count_a = 0
for i, record in datafile.iterrows():
    if "a" in record['name'] or "a" in record['name']:
        count_a += 1
        print(f"This pokemons name is {record['name']}")
        print(count_a)
