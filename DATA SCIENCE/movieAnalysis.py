import pandas as pd
datafile = pd.read_csv("Top Rated 9000 Movies TMDB.csv")

for i, record in datafile.iterrows():
    if  "Sigma" in record['a'] in record['title']:
        print(f"Title is {record['title']}")
