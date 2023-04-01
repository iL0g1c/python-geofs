# python-geofs
This package allows the use of an abstraction layer for the geoFS api.

## Quick Setup
1. Install the package with ```pip install python-geofs```
2. Create a python file and add ```import geofs```
3. Your good to go.

## Using the package
GeoFS has two different APIs.
One of them is used in game, and the other is for the map.
### Multiplayer API
```from geofs import multiplayerAPI```

Before you use the API you first have to give your account ID and session ID. (More on that later)

```myAPI = multiplayerAPI(sessionID, accountID)```

Next, you need to make a handshake with the server.

```myAPI.handshake()```

Finally, you are setup and can use the API freely.
multiplayerAPI currently allows you to send a recieve messages to the GeoFS chat.

```myAPI.sendMsg(msg)``` Sends a message to GeoFS chat.

```myAPI.getMessages(msg)``` allows you to pull the most recent messages from the server.
It will only pull messages that occured, since the last time you used this command.

### Map API
```from geofs import mapAPI```

This API is used for pulling user data from the server.

First initialize the class:

```myAPI = mapAPI()```

Now you can pull users.

```userData = myAPI.getUsers()```

## Getting Session and Account IDs
### Account IDs
The account ID identifies the account that you are using to connect to the server.
This is found on the account page on the website: https://www.geo-fs.com/pages/account.php?action=edit

This is refered to as your "user ID" on the website.

### Session ID
The session ID is stored on your computer in the cookies.
1. Sign into your account and log into the server.
2. Open Chrome Console with ctrl+shift+j
3. Paste this code into the console, and it will return the session ID
```
const cookies = document.cookie.split(';');
const sessionIdCookie = cookies.find(cookie => cookie.trim().startsWith('PHPSESSID='));
const sessionId = sessionIdCookie ? sessionIdCookie.split('=')[1] : null;
console.log(sessionId);
```
4. If you are having trouble connecting to the server, it may be that your session ID has expired, so be sure to check that.
