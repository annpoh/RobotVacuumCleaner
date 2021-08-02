import pycom
from machine import I2C
import machine
import lib.rvc as rvc
import lib.keys as keys
import lib.mpu6050 as mpu
import time
from math import sqrt

def checkCollision(acceleration, Glimit=1):
    # Calculate the length of the acceleration vector
    absAcc = sqrt(sum([i*i for i in acceleration]))
    return absAcc > Glimit

## Pybytes signals defined (fill it up as you add more!):
    # 0: 
    # 1: Collision count

# Indicate smartconfig process is finished
pycom.rgbled(0xAA1155)

# Setup starts here!
if not pybytes.is_connected():
    print("Not connected to pybytes. Updating config file:")
    pybytes.set_config('wifi', {'ssid': keys.SSID, 'password' : keys.PASSWORD})
    print("Trying to connect...")
    pybytes.connect()

# Sync Real Time Clock
rtc = machine.RTC()
rtc.ntp_sync(keys.NTP_SERVER)
print("Time is synced!")

# Create an instance of the Robot Vacuum Cleaner class
robot = rvc.RobotVacuumCleaner()

# Create I2C instance on bus 0 
# Default pins on Lopy4 are P9 (SDA) and P10 (SCL)
i2c = I2C(0, I2C.MASTER, baudrate=115200)

# Create an accelerometer object
accelerometer = mpu.accel(i2c)
accelerometer.calibrate()
print(accelerometer.offsets)

robot.moveForward()

# Indicate that initialization process is done
pycom.rgbled(0x00FF00)

while True:
    if checkCollision(accelerometer.get_acceleration()):
        robot.handleCollision()
        pybytes.send_signal(1, robot.collisionCount)
        robot.reportData()
    time.sleep(0.01)
