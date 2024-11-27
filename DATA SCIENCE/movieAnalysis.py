import pandas as pd
datafile = pd.read_csv("Top Rated 9000 Movies TMDB.csv")
count_a = 0
for i, record in datafile.iterrows():
    if  not "a" in record['title'] or not "a" in record['title'] or not "E" in record['title'] or not "e" in record['title']or not "I" in record['title']or not "i" in record['title']or not "O" in record['title']or not "o" in record['title'] or not "U" in record['title'] or not "u" in record['title']:
        count_a += 1
        print(f"Title is {record['title']}")
        print(count_a)
