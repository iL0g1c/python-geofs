from geofs import multiplayerAPI
import time

instance = multiplayerAPI("4llobv5bulth98j889cerspua0", "400813")
instance.handshake()
while True:
    print(instance.getMessages())
    time.sleep(.5)
