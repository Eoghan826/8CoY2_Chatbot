import pandas as pd
import json
datafile = pd.read_json("spotifyy.json")
count_a = 0
totala = 0
RED = '\033[31m'
RESET = '\033[0m'
for i, record in datafile.iterrows():
    trackName = record['master_metadata_track_name']
    if trackName:
        word = 'red'
        if word in trackName:
            print(f"{trackName[:trackName.find(word)]}{RED}red{RESET}{trackName:}")
