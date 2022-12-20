import statsapi

allSoxGames = statsapi.schedule(
    start_date='4/1/2021', end_date='10/5/2021', team='145')

allSoxHomeGames = []
for game in allSoxGames:
    if game['venue_name'] == 'Guaranteed Rate Field':
        # print(game['status'])
        allSoxHomeGames.append(statsapi.game_scoring_plays(game['game_id']))

four = 0
five = 0
six = 0


def check(g, inning):
    match inning:
        case '4':
            if 'Bottom 4' in g:
                return 1
        case '5':
            if 'Bottom 5' in g:
                return 1
        case '6':
            if 'Bottom 6' in g:
                return 1
    return 0


for game in allSoxHomeGames:
    four += check(game, '4')
    five += check(game, '5')
    six += check(game, '6')

print("The Sox scored in the 4th inning {0:.1f}% percent of the time".format(
    four / len(allSoxHomeGames) * 100))
print("The Sox scored in the 5th inning {0:.1f}% percent of the time".format(
    five / len(allSoxHomeGames) * 100))
print("The Sox scored in the 6th inning {0:.1f}% percent of the time".format(
    six / len(allSoxHomeGames) * 100))

# status postponed
