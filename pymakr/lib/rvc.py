import time
import random
from machine import PWM, Pin
from pybytes import Pybytes
from pycom import rgbled

FORWARD = (1,0)
BACKWARD = (0,1)
STOP = (0,0)

class DCmotor():
    def __init__(self, enable_pin, pin1, pin2, pwm_channel) -> None:
        # Standing still, (0,0), for starters (1,0) means forward, (0,1) backwards
        self.pin1 = Pin(pin1, mode=Pin.OUT) 
        self.pin1(0) 
        self.pin2 = Pin(pin2, mode=Pin.OUT)
        self.pin2(0)

        pwm = PWM(pwm_channel, frequency=5000) # Set the frequency of the chosen channel (0-15)
        self.enablePin = pwm.channel(pwm_channel, pin=enable_pin, duty_cycle=1.0)
        self.speed = 1.0
        self.defaultSpeed = 1.0

        self.collisionCount = 0

    def setSpeed(self, dutycycle):
        self.enablePin.duty_cycle(dutycycle)
        self.speed = dutycycle

    def getDirection(self):
        dir = (self.pin1(), self.pin2())
        return dir

    def setDirection(self, dir): # dir is a tuple
        self.pin1(dir[0])
        self.pin2(dir[1])

class RobotVacuumCleaner():
    def __init__(self) -> None:
        self.timeStarted = time.time()

        self.leftMotor = DCmotor('P3', 'P4', 'P8', pwm_channel=0)
        self.rightMotor = DCmotor('P19', 'P20', 'P21', pwm_channel=1)

        self.collisionCount = 0
        #self.sensorTimer = Timer.Alarm(handler=self.collectSensorData, ms=1000, arg=None, periodic=True)

    def runTime(self):
        timestamp = time.time()
        return int(timestamp - self.timeStarted)

    def turnRight(self):
        self.leftMotor.setDirection(FORWARD)
        self.rightMotor.setDirection(BACKWARD)
        rgbled(0x00EEFF)

    def turnLeft(self):
        self.leftMotor.setDirection(BACKWARD)
        self.rightMotor.setDirection(FORWARD)
        rgbled(0xEE3366)

    def moveForward(self):
        self.leftMotor.setDirection(FORWARD)
        self.rightMotor.setDirection(FORWARD)
        rgbled(0xFFFFFF)

    def moveBackward(self):
        self.leftMotor.setDirection(BACKWARD)
        self.rightMotor.setDirection(BACKWARD)
        rgbled(0x050505)

    def setSpeed(self, newSpeed):
        speed = max(0, min(newSpeed, 1)) # Making sure value is between 0 and 1
        self.rightMotor.setSpeed(speed)
        self.leftMotor.setSpeed(speed)

    def stop(self):
        self.leftMotor.setDirection(STOP)
        self.rightMotor.setDirection(STOP)

    def handleCollision(self):
        self.stop()
        # Collect the randomness<3
        turnright = random.choice(True, False) # Generate turn direction
        turntime = random.uniform(2.0, 5.0) # Generate turn duration

        time.sleep(2)
        
        # Back up before turning
        self.moveBackward()
        time.sleep(3)
        
        if turnright:
            self.turnRight()
        else:
            self.turnLeft()
        time.sleep(turntime)
        
        self.stop()
        time.sleep(2)
        
        # Keep going
        self.moveForward()
        
        self.collisionCount +=1

    # Currently not used! Fan goes on full speed if no signal is given, which is used atm.
    def startFan(self, pin, dutyCycle = 1.0):
        pwm = PWM(0, frequency=25000) # Fan PWM on 25 kHz for inaudibility
        self.fanPWM = pwm.channel(0, pin=pin, duty_cycle=dutyCycle)

    def setFanSpeed(self, dutyCycle=0.5):
        self.fanPWM.duty_cycle(dutyCycle)

    def reportData(self):
        # Can be extended with further data, like fan speed, acceleration etc
        #Pybytes.send_signal(1, self.collisionCount)
        print("Remember to implement this!")
    


    
    
        


