import requests
import json
import time

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
            self.aircraft = {'type':json.loads(open(r'geofs\data\aircraftcodes.json').read())[str(userobj['ac'])],'id':userobj['ac']}
        except KeyError:
            self.aircraft = {'type':"Unknown",'id':userobj['ac']}
## MAIN CLASS ##
class MapAPI:
    def __init__(self):
        self._responseList = []
        self._utilizeResponseList = True
    def getUsers(self,foos):
        while True:
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
                print("Unable to connect to GeoFS. Check your connection and restart the application.")
                print(f"Error message: {e}")
                time.sleep(5)

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