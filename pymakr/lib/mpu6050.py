from struct import unpack
import time
# MPU6050 library created by Adam Jezek: https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython
# Modified to fit this project

class accel():
    def __init__(self, i2c, addr=0x68, offsets=None, sensitivity_factor=2):
        # Set default offset values if not provided
        if offsets is None:
            offsets = [0,0,0,0,0,0,0]

        self.iic = i2c
        self.addr = addr
        # Writes to the power management 1 register (107). Selects gyro-X (1)
        # as the clock source according to recommendations in the data sheet
        self.iic.writeto(self.addr, bytearray([107, 1]))
        # Sensitivity is set to 2G as default, check data sheet if you want to change it
        self.sensitivity = sensitivity_factor
        self.offsets = offsets

    def calibrate(self, numreadings=10, timebetween=0.1):
        new_offsets = self.find_offsets(numreadings, timebetween)
        self.offsets = new_offsets

    def get_acceleration(self):
        data = self.iic.readfrom_mem(self.addr, 0x3B, 6)
        asInts = unpack('>hhh', data)
        calibrated = [i-j for i,j in zip(asInts, self.offsets[0:3])]
        gValues = [val*self.sensitivity/32767 for val in calibrated]
        return gValues

    def get_all_as_ints(self):
        raw = self.get_raw_values(bytes=14)
        # Unpack as big endian short (2 byte) signed ints
        asInts = unpack('>7h', raw)
        # Making a list since tuples are immutable)
        result = [i for i in asInts]
        return result

    # Finding the offsets (as integers)
    def find_offsets(self, numreadings=10, timebetween=0.1):
        print("Make sure the MPU6050 is still! Beginning calibration.")
        aX, aY, aZ, gX, gY, gZ = [], [], [], [], [], []
        for i in range(numreadings): # Makes ten measurements spaced about 0.1 sec apart (default)
            reading = self.get_all_as_ints()
            aX.append(reading[0])
            aY.append(reading[1])
            aZ.append(reading[2])
            # skipping temp
            gX.append(reading[4])
            gY.append(reading[5])
            gZ.append(reading[6])
            print("Reading {} out of {} done: {}".format(i+1, numreadings, reading))
            time.sleep(timebetween)
        collection = [aX, aY, aZ, gX, gY, gZ]
        result = []
        for entry in collection:
            result.append(sum(entry) // numreadings) # Sum and floor division
        print("The offsets are {}.".format(result))
        return [result[0], result[1], result[2], 0, result[3], result[4], result[5]]

### Functions from the original library
    def get_raw_values(self, bytes=14):
        a = self.iic.readfrom_mem(self.addr, 0x3B, bytes)
        return a

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["AcX"] = self.bytes_toint(raw_ints[0], raw_ints[1])*2*9.82/32767
        vals["AcY"] = self.bytes_toint(raw_ints[2], raw_ints[3])*2*9.82/32767
        vals["AcZ"] = self.bytes_toint(raw_ints[4], raw_ints[5])*2*9.82/32767
        vals["Tmp"] = self.bytes_toint(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        vals["GyX"] = self.bytes_toint(raw_ints[8], raw_ints[9])*2*9.82/32767
        vals["GyY"] = self.bytes_toint(raw_ints[10], raw_ints[11])*2*9.82/32767
        vals["GyZ"] = self.bytes_toint(raw_ints[12], raw_ints[13])*2*9.82/32767
        return vals  # returned in range of Int16
        # -32768 to 32767

    def val_test(self):  # ONLY FOR TESTING! Also, fast reading sometimes crashes IIC
        from time import sleep
        while 1:
            print(self.get_values())
            sleep(0.05)