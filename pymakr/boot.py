from network import WLAN
import lib.keys as keys
import machine
import utime

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid=keys.SSID, auth=(WLAN.WPA2, keys.PASSWORD))

print("Initialising connection attempt...")

waitingTime = 5
while not wlan.isconnected():
    wlan.connect(ssid=keys.SSID, auth=(WLAN.WPA2, keys.PASSWORD))
    if wlan.isconnected():
        break
    else:
        print(f"Failed connecting to {keys.SSID}. Next attempt in {waitingTime} seconds.")

print("WiFi connected succesfully")
print(wlan.ifconfig())