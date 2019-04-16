import requests

class GGApi:
    def __init__(self, afterDate, beforeDate):
        self.afterDate = afterDate
        self.beforeDate = beforeDate

    def send_query(self):
        headers = {"Authorization": "Bearer 108f713093eebd8a3153f295565ae22f", "content-type": "application/json"}
        perPage = 100
        coordinates = "33.7454725,-117.86765300000002"
        radius = "80mi"
        vgID = 1
        query = "query SocalTournaments" \
                "($perPage: Int, $coordinates: String!, $radius: String!, $videogameId: ID!, $beforeDate: Timestamp!, $afterDate: Timestamp!) " \
                "{ tournaments(query: { perPage: $perPage filter: " \
                "{ location: { distanceFrom: $coordinates, distance: $radius }, " \
                "videogameIds: [ $videogameId ], " \
                "beforeDate: $beforeDate, afterDate: $afterDate } }) " \
                "{ nodes { id name city } } }"
        variables = "{ \"perPage\": "+str(perPage)+", \"coordinates\": \""+coordinates+"\", " \
                "\"radius\": \""+radius+"\", \"videogameId\": "+str(vgID)+", \"afterDate\": 1545033600, \"beforeDate\": 1555920000 }"
        url = "https://api.smash.gg/gql/alpha"
        data = {
            "query": query,
            "variables": variables
        }
        print(url)
        print(headers)
        print(data)
        r = requests.post(url=url, headers=headers, data=data)
        return r