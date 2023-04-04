import Adafruit_BBIO.GPIO as GPIO

class EventButton():
    pin             = None
    edge = None
    # callback   = None

    
    def __init__(self, pin, edge, callback):
        self.pin = pin
        self.edge = edge
        # self.callback = 
        self.setup(callback)
        
    def setup(self, callback):
        # setup the pin
        GPIO.setup(self.pin, GPIO.IN)
        # setup the event handler
        GPIO.add_event_detect(gpio=self.pin, edge=self.edge, callback=callback)
        