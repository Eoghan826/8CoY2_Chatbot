import pandas as pd
datafile = pd.read_csv("Top Rated 9000 Movies")

for i, record in dataFile.iterrows():
    if  "m" in record['title'] or "n" in record['title']:
        print(f"Title is {record['title']}")
