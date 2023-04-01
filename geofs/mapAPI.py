import requests
import json

class mapAPI:
    def __init__(self):
        pass
    def getUsers(self):
        try:
            response = requests.post(
                "https://mps.geo-fs.com/map",
                json = {
                    "id":"",
                    "gid": None
                }
            )
            response_body = json.loads(response.text)
            return None, response_body["users"]
        except:
            raise("Unable to connect to GeoFS. Check your connection and restart the application.")