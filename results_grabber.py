from ggapi import *
import csv

def main():

    # Hardcoded timestamps
    afterDate = 1545033600
    beforeDate = 1555397935

    # Getting the values
    gg_runner = GGApi(afterDate, beforeDate)
    results = gg_runner.send_query()
    tournament_data = results.json()['data']['tournaments']['nodes']

    # For each entry, do stuff
    for tourney in tournament_data:
        print(tourney['url'] + str(tourney['startAt']))

if __name__ == '__main__':
    main()