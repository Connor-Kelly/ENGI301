import encoder



# ---

from event_button import EventButton
import Adafruit_BBIO.GPIO as GPIO
from cursor import Cursor
from spi_screen import SPI_Display as Display


def go_up(self):
    print("go up")
    d.display_image(c.cursor_up())



def go_dn(self):
    print("go down")
    d.display_image(c.cursor_dn())



pinBtnUp = "P2_22"
pinBtnDn = "P2_24"

c = Cursor()
d = Display()

BtnUp = EventButton(pinBtnUp, GPIO.FALLING, go_up)
BtnDn = EventButton(pinBtnDn, GPIO.FALLING, go_dn)

