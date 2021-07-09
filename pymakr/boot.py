from network import WLAN
import lib.keys as keys
import pycom
import time

pycom.heartbeat(False)
pycom.rgbled(0xFFFF00)
print('Hello there!')
print('Connected while running this file: {}'.format(WLAN(mode=WLAN.STA).isconnected()))
