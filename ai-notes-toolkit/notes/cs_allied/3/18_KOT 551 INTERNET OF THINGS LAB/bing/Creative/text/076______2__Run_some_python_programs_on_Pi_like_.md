#### 2. Run some python programs on Pi like:

- To run python programs on Pi, you need to have a Raspberry Pi device, a microSD card with an operating system installed, a power supply, a keyboard, a mouse, and a monitor. You also need to install python on your Pi if it is not already included in your operating system.
- To install python on your Pi, you can use the following command in the terminal: `sudo apt install python3`
- To write python programs on your Pi, you can use any text editor or IDE (Integrated Development Environment) that supports python syntax. Some examples are Thonny, IDLE, PyCharm, or Visual Studio Code. You can also use the nano editor in the terminal to create and edit python files.
- To run python programs on your Pi, you can use the following command in the terminal: `python3 filename.py`, where filename.py is the name of your python file. You can also run python programs directly from your text editor or IDE if they have a run or execute option.
- Some examples of python programs that you can run on your Pi are:

  - A program that prints "Hello, world!" to the screen: `print("Hello, world!")`
  - A program that blinks an LED connected to the Pi's GPIO (General Purpose Input Output) pins: `import RPi.GPIO as GPIO # Import the GPIO library
GPIO.setmode(GPIO.BCM) # Set the GPIO numbering mode
GPIO.setup(18, GPIO.OUT) # Set pin 18 as an output
while True: # Loop forever
  GPIO.output(18, GPIO.HIGH) # Turn on the LED
  time.sleep(1) # Wait for one second
  GPIO.output(18, GPIO.LOW) # Turn off the LED
  time.sleep(1) # Wait for one second`
  - A program that takes user input and prints it back: `user_input = input("Enter something: ") # Ask the user for input
print("You entered: " + user_input) # Print the user input`