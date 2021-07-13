import pycom
import time
import machine
import lib.rvc as rvc
import lib.keys as keys

pycom.heartbeat(False)
pycom.rgbled(0x00FFFF)

if not pybytes.is_connected():
    print("Not connected to pybytes. Updating config file:")
    pybytes.set_config('wifi', {'ssid': keys.SSID, 'password' : keys.PASSWORD})
    print("Trying to connect...")
    pybytes.connect()

wlan = WLAN(mode=WLAN.STA)
while not wlan.isconnected():
    pycom.rgbled(0xFF0000)
    print('Initializing connection attempt...')
    wlan.connect(ssid=keys.SSID, auth=(WLAN.WPA2, keys.PASSWORD))
    if wlan.isconnected():
        print("Connected!")
        pycom.rgbled(0x00FFFF)
        break
    else:
        print("Failed connecting to network. Next attempt in 5 seconds.")
    pycom.rgbled(0xFF0000)
    time.sleep(5)
    
# Sync Real Time Clock
rtc = machine.RTC()
rtc.ntp_sync(keys.NTP_SERVER)

# Init routines
# setState('parked')
# initUART
# notifyStarted()
#robot = rvc.RobotVacuumCleaner()
time.sleep(5)

#alarm = machine.Timer.Alarm(handler=self.collectSensorData, ms=5000, arg=None, periodic=True)
sreg = (1,0,0,0)

temp = (0,0,0,0)
while True:
    time.sleep(5)
    step()


while True: #Forever loop
    # Send current runtime to pybytes
    pycom.rgbled(0xFFFF00)  # Lime
    time.sleep(1) #sleep for 1 second

    pycom.rgbled(0xFF3300)  # Orange
    time.sleep_ms(1000) #sleep for 1000 ms

    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)

    #print(f"Time library says: {time.time()} or {time.localtime()}")