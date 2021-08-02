import pycom

# Indicate startup (boot file runs before smartconfig)
pycom.heartbeat(False)
pycom.rgbled(0xFFFF00)
print('Hello there!')


