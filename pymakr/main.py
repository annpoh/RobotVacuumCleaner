import pycom # "pycom" will be an error in your
# IDE because it's not on your computer, but on 
# the device
import time

pycom.heartbeat(False)

while True: #Forever loop
    pycom.rgbled(0xFFFF00)  # Red
    time.sleep(1) #sleep for 1 second

    pycom.rgbled(0xFF3300)  # Orange
    time.sleep_ms(1000) #sleep for 1000 ms

    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)