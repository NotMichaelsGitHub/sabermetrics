import statsapi

# sched = statsapi.schedule(start_date='07/01/2018',
#                           end_date='07/31/2018', team=143, opponent=121)

# print(sched)

print(statsapi.linescore(565997))

# rookie_hr_headers = statsapi.league_leaders(
#     'homeRuns', season=2021, playerPool='rookies', limit=5)
# print(rookie_hr_headers)

# print('White Sox 40-man roster on opening day of the 2021 season:\n%s' % statsapi.roster(143, '40Man',
#       date=statsapi.get('season', {'seasonId': 2021, 'sportId': 1})['seasons'][0]['regularSeasonStartDate']))

# http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1

# allSoxGames = statsapi.schedule(
#     start_date='4/1/2021', end_date='10/5/2021', team='145')

# for game in allSoxGames:
#     print(game['game_id'])

# soxHomeGames = []

# soxHomeGames.append(allSoxGames[170]['game_id'])
# print(soxHomeGames)

# print(statsapi.linescore(finalGame))
