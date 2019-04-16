from ggapi import *
import csv
import datetime

# returns a "row" (array) with the date, entrants, name, and url
def tourney_row_parser(tourney):

    # easy
    name = tourney['name']
    url = "https://smash.gg" + tourney['url'] + "/events/melee-singles/overview"

    # medium
    date = datetime.date.fromtimestamp(tourney['startAt'])
    isodate = date.isoformat()

    # hard
    entrants = 0
    for event in tourney['events']:
        if event['name'] == "Melee Singles":
            entrants = event['numEntrants']

    return [isodate, entrants, name, url]

# Parses the tournament data and writes to a csv file
def tournament_data_parser(tournament_data):
    with open('tournies.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for tourney in tournament_data:
            tourneyrow = tourney_row_parser(tourney)
            if "Weds Night Fights" in tourneyrow[2]:
                continue
            spamwriter.writerow(tourneyrow)

def main():

    # Hardcoded timestamps
    afterDate = 1545033600
    beforeDate = 1555398000

    # Preparing to do some date math
    dateMarkerEnd = datetime.datetime.fromtimestamp(beforeDate)
    firstDate = datetime.datetime.fromtimestamp(afterDate)
    one_month = datetime.timedelta(days=30)
    dateMarkerBeg = dateMarkerEnd - one_month


    # Start the .csv file
    with open('tournies.csv', 'w+') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['Date', 'Entrants', 'Name', 'URL'])

    # Getting the values

    while dateMarkerBeg > firstDate:
        gg_runner = GGApi(int(dateMarkerBeg.timestamp()), int(dateMarkerEnd.timestamp()))
        results = gg_runner.send_query()
        tournament_data = results.json()['data']['tournaments']['nodes']

        # Parse data and write to csv!
        tournament_data_parser(tournament_data)
        dateMarkerBeg -= one_month
        dateMarkerEnd -= one_month

    # last iteration
    gg_runner = GGApi(afterDate, int(dateMarkerEnd.timestamp()))
    results = gg_runner.send_query()
    tournament_data = results.json()['data']['tournaments']['nodes']
    tournament_data_parser(tournament_data)

if __name__ == '__main__':
    main()