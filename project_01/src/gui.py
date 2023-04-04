from event_button import EventButton
import Adafruit_BBIO.GPIO as GPIO
from cursor import Cursor
from spi_screen import SPI_Display as Display
from PIL import Image, ImageDraw, ImageFont

class GUI():
    # class vars
    cursor = None
    display = None
    pin_button_up = "P2_24"
    pin_button_down = "P2_22"
    pin_button_select = "P2_17"
    button_up = None
    button_down = None
    button_select = None
    background = None
    foreground = None
    dimensions = (320, 240)

    def __init__(self):
        self.cursor = Cursor()
        self.display = Display()

        # assumes that all buttons are momentary and are active-low
        self.button_up = EventButton(self.pin_button_up, GPIO.FALLING, lambda a : GUI.gui_up(self))
        self.button_down = EventButton(self.pin_button_down, GPIO.FALLING, lambda a : GUI.gui_dn(self))
        self.button_select = EventButton(self.pin_button_select, GPIO.FALLING, lambda a : GUI.gui_select(self))
        
        # load in background_gui, and display it
        self.background = self.open_image("slice1.png")
        self.display.display_image(self.background)
        
        # load in the cursor data
        self.foreground = self.cursor.get_image()
        self.display.display_image(Image.alpha_composite(self.background, self.foreground))
        
        pass

    def _setup(self):
        pass
    
    def gui_up(self):
        print("self: %s"%str(self))
        print("gui up")
        self.foreground = self.cursor.cursor_up()
        self.display.display_image(Image.alpha_composite(self.background, self.foreground))

    def gui_dn(self):
        print("self: %s"%str(self))
        print("gui down")
        self.foreground = self.cursor.cursor_dn()
        self.display.display_image(Image.alpha_composite(self.background, self.foreground))
        
    
    def gui_select(self):
        print("gui select")
        # selection = c.cursor_select()
        selection = "smthn"
        print("selection: %s"%str(selection))
        
    def open_image(self, filename):
        # Create image with file name
        image = Image.open(filename)
        # image = convertImage(image)

        # Get screen dimensions
        width, height = self.dimensions

        # Scale the image to the smaller screen dimension
        image_ratio  = image.width / image.height
        screen_ratio = width / height
        if screen_ratio < image_ratio:
            scaled_width  = image.width * height // image.height
            scaled_height = height
        else:
            scaled_width  = width
            scaled_height = image.height * width // image.width
        
        image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

        # Crop and center the image
        x = scaled_width  // 2 - width  // 2
        y = scaled_height // 2 - height // 2
        image = image.crop((x, y, x + width, y + height))
        
        return image