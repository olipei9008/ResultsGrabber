import requests

# Class to interact with the smash.gg API
class GGApi:

    # For now, only take in dates for getting tournaments in SoCal within the period.
    def __init__(self, authToken, afterDate, beforeDate):
        self.authToken = authToken
        self.afterDate = afterDate
        self.beforeDate = beforeDate


    # Making a query and sending it to smash gg
    def send_query(self):

        bearer = "Bearer " + self.authToken
        # need to edit in auth token before running
        headers = {"Authorization": bearer}

        # Hardcoded values to find tournaments for SoCal Melee
        perPage = 100
        coordinates = "33.7454725,-117.86765300000002"
        radius = "150mi"
        vgID = 1 # SSBM

        # Using very inelegant string concatenation to create the query + variables
        query = "query SocalTournaments" \
                "($perPage: Int, $coordinates: String!, $radius: String!, $videogameId: ID!, $beforeDate: Timestamp!, $afterDate: Timestamp!) " \
                "{ tournaments(query: { perPage: $perPage filter: " \
                "{ location: { distanceFrom: $coordinates, distance: $radius }, " \
                "videogameIds: [ $videogameId ], " \
                "beforeDate: $beforeDate, afterDate: $afterDate } }) " \
                "{ nodes { id name city url startAt events { id name numEntrants }} } }"
        variables = "{ \"perPage\": "+str(perPage)+", \"coordinates\": \""+coordinates+"\", " \
                "\"radius\": \""+radius+"\", \"videogameId\": "+str(vgID)+", \"afterDate\":" \
                " "+str(self.afterDate)+", \"beforeDate\": "+str(self.beforeDate)+" }"

        # Finishing up setting up the variables
        url = "https://api.smash.gg/gql/alpha"
        data = {
            "query": query,
            "variables": variables
        }

        # Send!
        r = requests.post(url=url, headers=headers, json=data)
        print(self.afterDate)
        print(self.beforeDate)
        print(r.content)
        return r