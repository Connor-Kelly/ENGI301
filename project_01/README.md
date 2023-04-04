# Music Box
## Repo: 
This reposistory is fairly simple, the vast majority of files pertaining to the project are contained within the project_01 directory, including docs in /project_01/docs and source code in /project_01/src. There is also some royalty free music contained within the /project_01/sample_music directory, being used solely for testing purposes. In addition to the project directory, there is a /ipynb_testing_files directory which contains a variety of jupyter notebook files which can be used for easily testing and iterating through code.

## Story:
For my ENGI 301 project, I wanted to produce a self-contained music player box. Why would you want a self-contained music player? Why? When you have services like spotify and apple music, would you want something so dumb that you could develop it on your own?\
Well, I got a record player for Christmas, along with a collection of my grandparent's record collection. It's a cheaper one, definitely with worse sound quality than my JBL bluetooth speaker. However, when I played music on the record player, I found out how much I fiddle with my spotify playlist. I'm constantly changing the order, adding things to the queue, or just moving the volume. This is significantly more difficult on the record player, yet, it was nice to not be so worried about my music. With this project, I wanted to replicate this feeling, by making a player which is capable of playing premade playlists on a usb, rather than tracks on a record. Doing so, would allow for more playtime and customizability on the music to play further outside of what is pressed on a given record.\

My plan was to create an initial product which is as simple as this: Turn on, Select a playlist and songs, Play Music. 
In order to do this, I would need to create a navigable GUI which interacts with the hardware correctly, and is capable of calling music commands from button presses. 

## Environment:
In working on this project, I had to test different modules in 3 different environments. This was due to the lack of parts at the initial outset, and lack of portability of the pocketBeagle board.

First, on my personal laptop. My laptop is a Windows machine, and from here, I mainly did research, and outline/initial python code in VSCode. This is where I built the diagram for System, Software, Power, and GUI, which was done in Affinity Designer, a cheaper alternative to Illustrator.

Second, on my VM. On my laptop, using VirtualBox, I set up an Ubuntu VM. This offered a simple, reliable way to test things which had to occur in a linux environment, such as terminal commands, MOC, and python scripts.

Third, on the PocketBeagle board. This was by far the worst experience. The PocketBeagle, in my experience, was unreliable, inconvienient, and overall a pain in the rear. One major struggle is that the board is not really portable. You can stick it in your bag, but there's a pretty good chance that any wires on the breadboard are going to be messed up. Another issue is that the board is unreliable. As in, at this stage, I am on my third board (through no fault of my own). One board refused to read my SD card, while the other couldn't seem to read the data lines on the usb port. While this is part of embedded development, it's still a little frustrating, leading me to seek alternative environments, until hardware is strictly necessary.

## Music Software:
The plan for software was originally to use MPD (music player daemon). On initial testing, it quickly became apparent that this was a horrible idea. For me, it was far too complex, and it was nearly impossible to get a workable solution. Instead, I opted to use MOC (music on console), which is far less complex.\
I built a simple moc.py library which can be called as a python class, and encapsulates all the pieces needed to run mocp, as well as python aliases of the mocp terminal commands. While I got this working very well in my VM, I discovered later that the PocketBeagle doesn't like to play well with other devices, and it requires further testing to get working on the PocketBeagle.
## Visual Software:
For this project, I decided I would need to develop a GUI, and corresponding Hardware to run the GUI. For my screen, I used a LCD SPI screen from adafruit, and I used Pillow to build the GUI image files, and adafuit's drivers to run the screen.
The GUI library is segmented into 3 portions, a driver for the cursor / list selection, a modified spi_display driver, and a GUI driver, to coordinate the two, as well as set up buttons, underlays, and to call out to the moc driver.

## Hardware Drivers:
For driving the hardware. I first focused focused on the buttons. For some reason, I couldn't get threading to work, like we did in class, so, I instead wrote a simple event driven button that produces a callback:

```python
class EventButton():
    pin     = None
    edge    = None
    
    def __init__(self, pin, edge, callback):
        self.pin = pin
        self.edge = edge
        self.setup(callback)
    def setup(self, callback):
        # setup the pin
        GPIO.setup(self.pin, GPIO.IN)
        # setup the event handler
        GPIO.add_event_detect(gpio=self.pin, edge=self.edge, callback=callback)
```
From here, we can simply produce a callback to any class function via the prototype:
```python
class C():
    def func(args);

    btn = EventButton(gpio_pin, GPIO_action, lambda x: C.func(self, args))

# where gpio_pin is like "P1_18" for GPIO pin 18 in header P1, and 
# GPIO_action is one of the following: {GPIO.FALLING, GPIO.RISING, GPIO.BOTH}
```
With this basic functionality, I wrote handlers for each buttons within the GUI class.
## Working with the Rotary Encoder:
I wanted to get a rotary encoder working in order to be able to scroll through the cursor list.  For all the libraries I found, none of them worked, however, I found a raspberrypi rotary repo which I could convert to using BBIO.GPIO instead of the RPI.GPIO. While this appeared to work in software, the hardware did not seem to be cooperating; when looking at the sys/dev/gpio values in the PocketBeagle filesystem, no value bits seemed to be changing when moving the hardware. After struggling with it for some time, I gave up on this hardware portion, though the software driver is likely working.

## What I learned: 
 I am very familiar with software and thus familiar with Murphy's Law, but I think it should be extended for embedded systems to something to the affect: Anything that can go wrong, will go wrong, at the least convenient time, and it will be impossible to debug. 
I learned that debugging hardware and the os is a multilayered approach. For example, when setting up my USB on my second board, I found that the USB port had power, so I assumed that the data lines would be working. However, when running a `lsusb` command, I found that it didn't recognize my speaker. Where would one start debugging this issue? Honestly, my answer was to take it to my professor, and ask for help, but the answer was actually to get another board. 
I also learned that some things are just going to be magic. For example, the library which handles the rotary encoder is a piece of straight up bit magic. It uses the 4 low bits of a class integer to maintain the previous state of the encoder, pushes the new state bits onto the integer, and then uses states from 1 to 15 to determine the rotation direction which caused that state update. From looking at the algorithm, I just assumed that it was magic, and asked my professor why my encoder wasn't working. After he explained the algorithm, I think I understood how it worked, but we still could not get the encoder to work. 
I also learned that most things just aren't going to just work. When a port doesn't work, the first step is to perturb all the things associated with it. It should be re-plugged, any config files should be checked, the state should be reset, and any and all wire connections should be checked.

## What's left:
The cursor library still needs to be completed when it is given a correct target_list, this target_list would be a playlist or directory, which needs to be scrolled through. This has not been implemented, as I ran out of time working to get moc to work on the PocketBeagle, however, there exists a cursor.Cursor.cursor_select(), which should return a <str> target, which will then get called in moc like so moc.Moc.play_target(target), and direct the player to the target song.