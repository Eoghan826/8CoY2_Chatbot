import pandas as pd
datafile = pd.read_csv("Top Rated 9000 Movies TMDB.csv")
count_a = 0
for i, record in datafile.iterrows():
    if  not "Love" in record['overview'] or not "love" in record['overview']:
        count_a += 1
        print(f"Title is {record['overview']}")
        print(count_a)
