import pycom
import time
from machine import Pin
import machine
import lib.rvc as rvc
import lib.keys as keys

pycom.heartbeat(False)
pycom.rgbled(0x00FFFF)
"""
if not pybytes.is_connected():
    print("Not connected to pybytes. Updating config file:")
    pybytes.set_config('wifi', {'ssid': keys.SSID, 'password' : keys.PASSWORD})
    print("Trying to connect...")
    pybytes.connect()
    
# Sync Real Time Clock
rtc = machine.RTC()
rtc.ntp_sync(keys.NTP_SERVER)

"""
time.sleep(5)

en12 = Pin('P19', mode=Pin.OUT)
pinA1 = Pin('P20', mode=Pin.OUT)
pinA2 = Pin('P21', mode=Pin.OUT)

en12(0)
pinA1(1)
pinA2(0)


while True: #Forever loop
    # Send current runtime to pybytes
    pycom.rgbled(0xFFFF00)  # Lime
    time.sleep(1) #sleep for 1 second

    pycom.rgbled(0xFF3300)  # Orange
    time.sleep_ms(1000) #sleep for 1000 ms

    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
