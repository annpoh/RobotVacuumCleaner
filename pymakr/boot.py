from network import WLAN
import lib.keys as keys
import pycom
import time

pycom.heartbeat(False)
pycom.rgbled(0xFFFF00)

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid=keys.SSID, auth=(WLAN.WPA2, keys.PASSWORD))
print('Hello there!')
print("Initialising connection attempt...")

waitingTime = 5
while not wlan.isconnected():
    pycom.rgbled(0x00FF00)
    wlan.connect(ssid=keys.SSID, auth=(WLAN.WPA2, keys.PASSWORD))
    if wlan.isconnected():
        break
    else:
        print("Failed connecting to network. Next attempt in {} seconds.".format(waitingTime))
    pycom.rgbled(0xFF0000)
    time.sleep(waitingTime)


print("WiFi connected succesfully")
print(wlan.ifconfig())
