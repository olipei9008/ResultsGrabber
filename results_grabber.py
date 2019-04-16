from ggapi import *

def main():
    afterDate = 1545033600
    beforeDate = 1555920000
    gg_runner = GGApi(afterDate, beforeDate)
    results = gg_runner.send_query()
    print(results.content)

if __name__ == '__main__':
    main()