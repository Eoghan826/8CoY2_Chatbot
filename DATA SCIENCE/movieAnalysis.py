import pandas as pd
datafile = pd.read_csv("Top Rated 9000 Movies TMDB.csv")
count_a = 0
for i, record in datafile.iterrows():
    if  "A" in record['title'][0] or "a" in record['title'][0]:
        count_a += 1
        print(f"Title is {record['title']}")
        print(count_a)
