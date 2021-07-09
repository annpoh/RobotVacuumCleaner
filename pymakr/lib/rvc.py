import time
from machine import PWM, UART
PARKED = 0
MANUAL = 1
AUTO = 2

class RobotVacuumCleaner():
    def __init__(self) -> None:
        self.timeStarted = time.time()
        print("Started at {}".format(self.timeStarted))
        self.state = PARKED
        self.uart_connected = False
    
    def runTime(self):
        timestamp = time.time()
        return int(timestamp - self.timeStarted)

    def startFan(self, pin = 'P12', dutyCycle):
        pwm = PWM(0, frequency=25000) # Fan wants 25 kHz for inaudibility
        self.fanPWM = pwm.channel(0, pin=pin, duty_cycle=dutyCycle)

    def setFanSpeed(self, dutyCycle=0.5):
        self.fanPWM.duty_cycle(dutyCycle)
    
    def initUART(self, baudrate):
        uart = UART(1) # Construct UART object on bus1
        uart.init(baudrate=baudrate)

    #TODO
    def handleCollision(self):
        print('Collided!')
        #save traveled distance and stuff?

    def reportData(self):
        print("Report data not implemented yet")
        


