import pandas as pd
datafile = pd.read_csv("Top Rated 9000 Movies TMDB.csv")
count_a = 0
for i, record in datafile.iterrows():
    if  "m" in record['title'] or "M" in record['title']or "N" in record['title']or "n" in record['title']:
        count_a += 1
        print(f"Title is {record['title']}")
        print(count_a)
