import time
from machine import PWM, UART, Timer
PARKED = 0
MANUAL = 1
AUTO = 2

class RobotVacuumCleaner():
    def __init__(self) -> None:
        self.timeStarted = time.time()
        print("Started at {}".format(self.timeStarted))
        self.state = PARKED
        self.uartConnected = False

        # Motor values setup
        self.LWR = 0 # Left wheel tick rate
        self.RWR = 0 # Right wheel tick rate
        self.leftDSC = 0.0 # Distance since last collision
        self.rightDSC = 0.0
        self.leftTicksSinceUpdate = 0 
        self.rightTicksSinceUpdate = 0
        self.LWS = (0,)

        #self.sensorTimer = Timer.Alarm(handler=self.collectSensorData, ms=1000, arg=None, periodic=True)
        self.testTicks = 0
        self.leftWheelTimer = None
        self.rightWheelTimer = None
        self.actionTimer = None # Handle when 

    def runTime(self):
        timestamp = time.time()
        return int(timestamp - self.timeStarted)

    def setState(self, newState):
        if newState == PARKED: 
            self.stop()
            pycom.rgbled(0x0000FF) # Blue
        elif newState == MANUAL:
            print("Manual mode isn't implemented")
        elif newState == AUTO:
            print("duuh, implement this please")
            pycom.rgbled(0xFFFF00) # Lime
            self.leftWheelTimer

    def startFan(self, pin = 'P12', dutyCycle = 0.5):
        pwm = PWM(0, frequency=25000) # Fan wants 25 kHz for inaudibility
        self.fanPWM = pwm.channel(0, pin=pin, duty_cycle=dutyCycle)

    def setFanSpeed(self, dutyCycle=0.5):
        self.fanPWM.duty_cycle(dutyCycle)
    
    def initUART(self, baudrate):
        uart = UART(1) # Construct UART object on bus1
        uart.init(baudrate=baudrate)

    def stop(self):
        if self.leftWheelTimer or self.rightWheelTimer:
            self.leftWheelTimer.cancel()
            self.rightWheelTimer.cancel()

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
    
        


