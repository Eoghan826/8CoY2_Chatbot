import pandas as pd
datafile = pd.read_csv("Top Rated 9000 Movies TMDB.csv")

for i, record in datafile.iterrows():
    if  "A" in record['title'][0] or "a" in record['title'][0]:
        print(f"Title is {record['title']}")
