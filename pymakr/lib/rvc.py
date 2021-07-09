import time
PARKED = 0
MANUAL = 1
AUTO = 2

class RobotVacuumCleaner():
    def __init__(self) -> None:
        self.timeStarted = time.time()
        print("Started at {}".format(self.timeStarted))
        self.state = PARKED
    
    def runTime():
        timestamp = time.time()
        return int(timestamp - self.timeStarted)

