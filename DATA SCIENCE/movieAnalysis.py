import pandas as pd
datafile = pd.read_csv("Top Rated 9000 Movies TMDB.csv")
count_a = 0
for i, record in datafile.iterrows():
    if "a" in record['title'] or "a" in record['title'] or "E" in record['title'] or "e" in record['title']or "I" in record['title']or "i" in record['title']or "O" in record['title']or "o" in record['title'] or "U" in record['title'] or "u" in record['title']:
        count_a += 1
        print(f"Title is {record['title']}")
        print(count_a)
        print(9000 - count_a)
