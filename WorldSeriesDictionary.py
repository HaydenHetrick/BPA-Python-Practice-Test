BASE_YEAR = 1903

def main():
    year_dict = {}
    count_dict = {}

    input_file = open('WorldSeriesDictionary.txt', 'r')
    winners = input_file.readlines()

    for i in range(len(winners)):
        team = winners[i].rstrip('\n')
        year = BASE_YEAR + i
        if year == 1904 or year == 1994:
            year_dict[str(year)] = "No World Series"
        else:
            if year > 1994:
                year += 1

            year_dict[str(year)] = team

        if team in count_dict:
            count_dict[team] += 1
        else:
            count_dict[team] = 1

    year = input('Enter a year between 1903-2022 to find out who won that year\'s World Series: ')

    if year == '1904' or year == '1994':
        print("The World Series Wasn't Played In", year)
    elif int(year) < 1903 or int(year) > 2022:
        print('There is no data for the year', year)
    else:
        winner = year_dict[year]
        wins = count_dict.get(winner, 0)
        print('The team that won the World Series in that year are the', winner + '.')
        print('They have won the World Series', wins, 'times.')

main()
