# python-geofs
This package is an abstraction layer for the GeoFS API, allowing for Python 3+ integration.

## Quick Install
1. Install the package via pip with ```pip install python-geofs``` in the terminal.
2. Create a Python (v3.0+) file and add ```import geofs```
3. Utilize below guide for use instructions.

## Using the package
GeoFS has two different backend APIs, one which powers the Map, and presents the basic information of every user (callsign, location, etc), called the MapAPI, and the MultiplayerAPI, which allows you to spawn in as a user, send and receive chat messages, and more (coming soon).

### MapAPI
You utilize the MapAPI to get basic information on every users. The following is a list of all data presented by the API for usage:
**1.** Location (latitude and longitude)
**2.** Altitude
**3.** Vertical Speed
**4.** Airspeed
**5.** User Info (callsign & GeoFS internal identifier)
**6.** Aircraft Type

To begin utilizing the MapAPI, you must initialize the ``MapAPI`` class. You may then utilize the ``getUsers()`` function to get a list of users.

#### ``MapAPI`` Class
The ``MapAPI`` class does not take in any variables.
##### Example
```python
from geofs import MapAPI
api = MapAPI()
```
With the API Class defined, you can then utilize any of the below functions & variables.

##### Functions List
``getUsers(foos:bool/NoneType)``: Returns a list of users in the form of a list of ``Player`` classes. Pass in ``False`` to ``foos`` to have no foos, ``True`` to have only foos, and ``None`` to be indescriminate of type.
``returnResponseList(reset:bool)``: Returns a list of the previous responses (if reset is ``True``, then clear the response list).
``disableResponseList()``: Disables the saving of previous responses for use in ``returnResponseList``. Do note that the list is on by default.
``enableResponseList()``: Enables the saving of previosu responses for use in ``returnResponseList``. Do note that the list is on by default.
``getUser(acid:int)``: (Coming in next version), will provide a ``Player`` class for the user who's acid is provided, if found.
##### Variables List
The ``MapAPI`` Class has no externally used variables.

#### ``Player`` Class
The ``Player`` class is an internally initialized  class which provides all information about one specific player.
##### Functions List
``findUser()``: (Coming in next version), will provide a circularly initialized ``Player`` class with updated information on the player.
##### Variables List
``Player.airspeed``: (``int``) Player's airspeed in knots.
``Player.userInfo``: (``dict``) Player's callsign and internal ID (acid).
``Player.coordinates``: (``tuple``) Player's latitude [0] and longitude [1].
``Player.altitude``: (``int`` or ``float``) Player's altitude in feet (type ``float`` will be a result of conversion from meters, which GeoFS uses internally, to feet, which is offered by this module).
``Player.verticalSpeed``: (``int`` or ``float``) Player's vertical speed in feet (type ``float`` will be a result of conversion from meters, which GeoFS uses internally, to feet, which is offered by this module).
``Player.aircraft``: (``dict``) Player's aircraft type and that aircraft's GeoFS Internal ID.
``Player.grounded``: (``bool``) Coming in next update, tells if a player is grounded or not.

### MapAPI Example
The below example gets a list of all non-foo users, and prints all of their callsigns followed by their altitudes
#### Code
```python
from geofs import MapAPI

data = MapAPI().getUsers(foos=False)
for player in data:
    print (player.userInfo['callsign']+': '+str(player.altitude))
```
#### Output
```BVW-00: 1971.08
Venom583: 26.37
davidpietro: 23414.06
WN-1529: 17493.09
SomebodyaddtheF35: 526.4
NICARAGUAN-2[FAN][ACIR][626]: 34000.2
fiumba: 2005.44
DXA212: 69.0
TCHALA[M4AF][FIGHTER][AIRSHOW]: 156.2
Eagle-7[18][3UM][USAF]: 4582.4
N999UA: 1155.33
BJ-120: 4425.64
626076: 474.72
SubtoBrianisawesome2927: 8.19
```
#### Output
## Getting Session and Account IDs
### Account IDs
The account ID identifies the account that you are using to connect to the server.
This is found on the account page on the website: https://www.geo-fs.com/pages/account.php?action=edit

This is refered to as your "user ID" on the website.

## MultiplayerAPI
The MultiplayerAPI exists in the code, but is currently being redone.
