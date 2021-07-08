import pycom
import time
import machine
import lib.rvc as rvc

pycom.heartbeat(False)
pycom.rgbled(0x00FFFF)
# Init routines
# setState('parked')
# initUART
# notifyStarted()
rtc = machine.RTC()
rtc.init()
rtctime, timetime, localtime = [rtc.now(), time.time(), time.localtime()]
print("Before RTC sync:")
print(rtctime)
print(timetime)
print(localtime)

rtc.ntp_sync("ntp.se")
rtctime, timetime, localtime = [rtc.now(), time.time(), time.localtime()]
isSynced = rtc.synced()
print("Synced: {}".format(isSynced))

print(rtctime)
print(timetime)
print(localtime)

time.sleep(5)

while True: #Forever loop
    pycom.rgbled(0xFFFF00)  # Red
    time.sleep(1) #sleep for 1 second

    pycom.rgbled(0xFF3300)  # Orange
    time.sleep_ms(1000) #sleep for 1000 ms

    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)

    rtctime = rtc.now()
    print("RTC time says: {}.".format(rtctime))
    #print(f"Time library says: {time.time()} or {time.localtime()}")