from PIL import Image, ImageDraw, ImageFont

class Cursor():
    # class variables
    name = None
    cursor_type = None
    index = None
    target = None
    image = None
    limit = None
    shift = None
    target_image = None
    target_list = None
    selection_layer = None
    spacing = 2
    font = None
    position = (11, 40)


    def __init__(self, name="unnamed", cursor_type="None", index=0, target_list = [], target="None") -> None:
        self.name = name
        self.cursor_type = cursor_type
        self.index = index
        self.shift = index
        self.target_list = target_list
        self.target = None
        self.limit = 6
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        
        # initialize the selection_layer to be a new transparent image. 
        # self.image = Image.new("RGBA", (320,240), (0,0,0,0))
        # self.target_image = Image.new("RGBA", (320,240), (0,0,0,0))
        # self.selection_layer = Image.new("RGBA", (320,240), (0,0,0,0))
        self.image = None
        self.target_image = None
        self.selection_layer = None
        self.draw_target_list()
        self.draw_selection_box()
        

    def cursor_up(self):
        print("cursor_up")
        self.index -= 1

        # check if we need to shift
        if (self.index < self.shift):
            self.shift_up()

        # redraw the selection box to index - shift
        self.draw_selection_box()
        
        return self.get_image()

    def cursor_dn(self):
        print("cursor_dn")
        self.index += 1

        # check if we need to shift
        if (self.index > self.shift + self.limit):
            self.shift_dn()

        # redraw the selection box to index - shift
        self.draw_selection_box()
        
        return self.get_image()
    
    def shift_up(self): # shifts the target_list upward
        self.shift -= 1
        # redraw the target_list
        self.draw_target_list()
        
    
    
    def shift_dn(self): # shifts the target_list downward
        self.shift += 1
        # redraw the target_list
        self.draw_target_list()
        

    def get_image(self):
        self.image = Image.new("RGBA", (320,240), (0,0,0,0))
        # self.image.paste(self.selection_layer, (0,0))
        # self.image.paste(self.target_image, (0,0))
        self.image = Image.alpha_composite(self.selection_layer, self.target_image)
        # self.image.show()
        return self.image

    def draw_target_list(self):
        if (self.target_list == []):
            self.target_list = ["Trackname"] * self.limit
        
        # reset the image
        self.target_image =  Image.new("RGBA", (320,240), (0,0,0,0))

        target_string = "\n".join(self.target_list)

        # draw the multiline target_list
        draw = ImageDraw.Draw(self.target_image)

        draw.text(self.position, target_string, font = self.font, spacing = self.spacing)
        
        return self.target_image
        # self.target_image.show()
        


    def draw_selection_box(self):
        self.selection_layer = Image.new("RGBA", (320,240), (0,0,0,0))
        
        # draw the multiline target_list
        draw = ImageDraw.Draw(self.selection_layer)

        slot = self.index - self.shift
        # x = (0, 320)
        
        pos = [0, (slot * 20) + 40, 320, ((slot + 1) * 20) + 40]
        print("pos: %s"%(str(pos)))
        # 
        draw.rectangle(pos, fill = (100,100,100,255), outline=(0,0,0,0), width =1)
        # self.selection_layer.show()
        
        return self.selection_layer