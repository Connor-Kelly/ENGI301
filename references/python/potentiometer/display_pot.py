import time

import Adafruit_BBIO.GPIO as GPIO

import ht16k33 as HT16K33


print("Potentiometer Test")

# Create instantiation of the potentiometer
pot = Potentiometer("P1_19")
display    = HT16K33.HT16K33(i2c_bus=1, i2c_address=0x70)

display.clear()

# Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
print("Use Ctrl-C to Exit")

try:
    while(1):
        # Print potentiometer value
        value = pot.get_value(value)
        print("Value   = {0}".format())
        print("Voltage = {0} V".format(pot.get_voltage()))
        self.display.update(value)
        time.sleep(1)
    
except KeyboardInterrupt:
    pass

print("Test Complete")