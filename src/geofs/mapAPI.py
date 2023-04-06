import requests
import json
import time
import pkg_resources

## EXCEPTIONS ##
class BackendError(Exception):
    pass

## USER CLASSES ##

class Player:
    def __init__ (self,userobj):
        #add grounded
        self.airspeed = userobj['st']['as']
        self.userInfo = {'id':userobj['acid'],'callsign':userobj['cs']}
        self.coordinates = (userobj['co'][0],userobj['co'][1])
        self.altitude = round(userobj['co'][2]*3.28084,2) # meters to feet
        self.verticalSpeed = round(userobj['co'][3]*3.28084,2) # meters to feet
        try:
            with pkg_resources.resource_stream("geofs", "data/aircraftcodes.json") as reader:
                aircrafCodes = json.load(reader)
            self.aircraft = {
                'type':aircrafCodes[str(userobj['ac'])],
                'id':userobj['ac']
            }
        except KeyError:
            self.aircraft = {
                'type':"Unknown",
                'id':userobj['ac']
            }
## MAIN CLASS ##
class MapAPI:
    def __init__(self):
        self._responseList = []
        self._utilizeResponseList = True
        self.error = False
    def getUsers(self,foos):
        self.error = False
        try:
            response = requests.post(
                "https://mps.geo-fs.com/map",
                json = {
                    "id":"",
                    "gid": None
                }
            )
            response_body = json.loads(response.text)
            userList = []
            if foos == False:
                for user in response_body['users']:
                    if user['cs'] == "Foo" or user['cs'] == '':
                        pass
                    else:
                        userList.append(Player(user))
            elif foos == True:
                for user in response_body['users']:
                    if user['cs'] != "Foo":
                        pass
                    else:
                        userList.append(Player(user))
            elif foos == None:
                userList.append(Player(user))
            
            
            else:
                raise AttributeError('"Foos" attribute must be boolean or NoneType.')
            if self._utilizeResponseList == True:
                self._responseList.append(userList)
            return userList
        except Exception as e:
            self.error = True
            print("Unable to connect to GeoFS. Check your connection and restart the application.")
            print(f"Error Code 1: {e}")
            return None

    def returnResponseList(self,reset:bool):
        if reset == True:
            before = self._responseList
            self._responseList = []
            return before
        return self._responseList
    def disableResponseList(self):
        self._utilizeResponseList = False
    def enableResponseList(self):
        self._utilizeResponseList = True


'''
st gr -- grounded
st as -- airspeed
ac -- aircraft number [refr aircraftcodes.json]
acid -- user id
cs -- callsign
co 0 latitude
co 1 longitude
co 2 altitude in meters
co 3 vertical speed in meters
'''