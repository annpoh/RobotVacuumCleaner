import time
from machine import PWM, Pin
PARKED = 0
MANUAL = 1
AUTO = 2
FORWARD = (1,0)
BACKWARD = (0,1)
STOP = (0,0)

class DCmotor():
    def __init__(self, enable_pin, pin1, pin2, pwm_channel) -> None:
        # Standing still for starters (1,0) is forward, (0,1) backwards
        self.pin1 = Pin(pin1, mode=Pin.OUT) 
        pin1(0) 
        self.pin2 = Pin(pin2, mode=Pin.OUT)
        pin2(0)

        PWM(pwm_channel, frequency=1000) # Set the frequency of the chosen channel (0-15)
        self.enablePin = PWM.channel(pwm_channel, pin=enable_pin, duty_cycle=0.8)
        self.speed = 0.8
        self.defaultSpeed = 0.8

    def setSpeed(self, dutycycle):
        self.enablePin.duty_cycle(dutycycle)

    def setDirection(self, dir): # dir is a tuple
        self.pin1(dir[0])
        self.pin2(dir[1])

class RobotVacuumCleaner():
    def __init__(self) -> None:
        self.timeStarted = time.time()
        print("Started at {}".format(self.timeStarted))
        self.state = PARKED

        self.leftMotor = DCmotor('P8', 'P9', 'P10', pwm_channel=0)
        self.rightMotor = DCmotor('P19', 'P20', 'P21', pwm_channel=1)

        self.collisionCount = 0
        self.averageCollisionTime = None
        self.lastCollision = None
        #self.sensorTimer = Timer.Alarm(handler=self.collectSensorData, ms=1000, arg=None, periodic=True)

    def start(self):
        self.lastCollision = time.time()
        self.setState(AUTO)

    def runTime(self):
        timestamp = time.time()
        return int(timestamp - self.timeStarted)

    def setState(self, newState):
        if newState == PARKED: 
            self.stop()
            pycom.rgbled(0x0000FF) # Blue
        elif newState == MANUAL:
            print("Manual mode isn't implemented")
            pycom.rgbled(0xFF6611)
            self.stop()
            newState = PARKED
        elif newState == AUTO:
            print("duuh, implement this please")
            pycom.rgbled(0xFFFF00) # Lime
        self.state = newState


    # Don't use P12!
    #def startFan(self, pin = 'P12', dutyCycle = 0.5):
    #    pwm = PWM(0, frequency=25000) # Fan wants 25 kHz for inaudibility
    #    self.fanPWM = pwm.channel(0, pin=pin, duty_cycle=dutyCycle)

    #def setFanSpeed(self, dutyCycle=0.5):
    #    self.fanPWM.duty_cycle(dutyCycle)
    
    def turnRight(self):
        self.leftMotor.setDirection(FORWARD)
        self.rightMotor.setDirection(BACKWARD)

    def turnLeft(self):
        self.leftMotor.setDirection(BACKWARD)
        self.rightMotor.setDirection(FORWARD)

    def moveForward(self):
        self.leftMotor.setDirection(FORWARD)
        self.rightMotor.setDirection(FORWARD)

    def moveBackward(self):
        self.leftMotor.setDirection(BACKWARD)
        self.rightMotor.setDirection(BACKWARD)


    def stop(self):
        print('STAAAHP')
        self.leftMotor.setDirection(STOP)
        self.rightMotor.setDirection(STOP)

    #TODO
    def handleCollision(self):
        print('Collided!')
        #save traveled distance and stuff?
        #reset distance since collision

    def reportData(self):
        print("Report data not implemented yet")

        # Timer for updating distance
    

    def collectSensorData(self, alarm):
        self.testTicks += 1
        print(self.testTicks)
        if self.testTicks > 9:
            alarm.cancel()
        # s = t*v
    
        


