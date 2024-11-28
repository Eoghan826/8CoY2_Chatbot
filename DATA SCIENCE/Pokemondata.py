import pandas as pd
datafile = pd.read_csv("Pokemon.csv")
count_a = 0
totala = 0
for i, record in datafile.iterrows():
    if 'Dragon' == (record['Type 2']):
        count_a += 1
        totala += str(record['Type 2'])
        print(count_a)
import pandas as pd
datafile = pd.read_csv("Pokemon.csv")
count_a = 0
totala = 0
for i, record in datafile.iterrows():
    if record['Type 2'] == 'Dragon':
        count_a += 1
        totala += record['SomeNumericField']
        print(f"Count of Dragon Type 2: {count_a}")
        print(f"Total for SomeNumericField: {totala}")
