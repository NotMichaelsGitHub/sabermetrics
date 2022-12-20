import statsapi
import json


allSoxGames = statsapi.schedule(
    start_date='4/1/2021', end_date='10/5/2021', team='145')

with open('data.txt', 'w') as outfile:
    json.dump(allSoxGames, outfile)
