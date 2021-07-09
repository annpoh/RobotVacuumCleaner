import pycom
import time
import machine
import lib.rvc as rvc
import lib.keys as keys

pycom.heartbeat(False)
pycom.rgbled(0x00FFFF)

wlan = WLAN(mode=WLAN.STA)
while not wlan.isconnected():
    pycom.rgbled(0xFF0000)
    print('Initializing connection attempt...')
    wlan.connect(ssid=keys.SSID, auth=(WLAN.WPA2, keys.PASSWORD))
    if wlan.isconnected():
        break
    else:
        print("Failed connecting to network. Next attempt in {} seconds.".format(waitingTime))
    pycom.rgbled(0xFF0000)
    time.sleep(waitingTime)
    
# Sync Real Time Clock
rtc = machine.RTC()
rtc.ntp_sync(keys.NTP_SERVER)

# Init routines
# setState('parked')
# initUART
# notifyStarted()
robot = rvc.RobotVacuumCleaner()
time.sleep(5)

while True: #Forever loop
    # Send current runtime to pybytes
    pycom.rgbled(0xFFFF00)  # Red
    time.sleep(1) #sleep for 1 second

    pycom.rgbled(0xFF3300)  # Orange
    time.sleep_ms(1000) #sleep for 1000 ms

    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)

    #print(f"Time library says: {time.time()} or {time.localtime()}")