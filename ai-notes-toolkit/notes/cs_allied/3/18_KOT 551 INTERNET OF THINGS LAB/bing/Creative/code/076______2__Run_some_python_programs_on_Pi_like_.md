#### 2. Run some python programs on Pi like:

- To run python programs on Pi, you need to have a Raspberry Pi device, a microSD card with an operating system installed, a power supply, a keyboard, a mouse, and a monitor.
- You also need to install python on your Pi, which you can do by opening a terminal and typing `sudo apt install python3`.
- You can write python programs using any text editor, such as nano, vim, or IDLE. To create a new file, type `nano program.py` in the terminal, where `program.py` is the name of your file.
- You can write python code using the same syntax and rules as on any other platform. For example, to print "Hello, world!" on the screen, you can write:

```python
print("Hello, world!")
```

- To save and exit the file, press Ctrl+X, then Y, then Enter.
- To run the program, type `python3 program.py` in the terminal. You should see the output on the screen.
- You can run any python program on Pi, as long as you have the required libraries and modules installed. For example, to use the GPIO pins on the Pi, you need to install the RPi.GPIO module by typing `sudo apt install python3-rpi.gpio`.
- You can then import the module in your program and use it to control the pins. For example, to blink an LED connected to pin 18, you can write:

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use BCM numbering scheme
GPIO.setup(18, GPIO.OUT) # set pin 18 as output

while True: # loop forever
    GPIO.output(18, GPIO.HIGH) # turn on LED
    time.sleep(1) # wait for 1 second
    GPIO.output(18, GPIO.LOW) # turn off LED
    time.sleep(1) # wait for 1 second
```

- To stop the program, press Ctrl+C in the terminal. To clean up the GPIO pins, type `GPIO.cleanup()` in the terminal.