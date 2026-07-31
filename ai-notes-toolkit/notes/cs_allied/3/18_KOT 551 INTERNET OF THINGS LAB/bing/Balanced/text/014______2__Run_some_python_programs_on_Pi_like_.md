#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your device. Python is a high-level, interpreted, and general-purpose programming language that can run on various platforms, including Pi.
- You can check if you have python installed by typing `python --version` or `python3 --version` in the terminal. If you see a version number, such as 3.9.2, then you have python installed. If not, you can install it by typing `sudo apt install python3` or `sudo apt install python` depending on the version you want.
- To write a python program, you can use any text editor, such as nano, vim, or idle. You can also use an integrated development environment (IDE), such as Thonny, which is pre-installed on Pi. To launch Thonny, type `thonny` in the terminal or click on the Raspberry Pi icon on the top left corner of the screen and select Programming > Thonny Python IDE.
- To create a new python file, click on File > New or press Ctrl+N. To save the file, click on File > Save or press Ctrl+S. To run the file, click on Run > Run current script or press F5. You can also run the file from the terminal by typing `python filename.py` or `python3 filename.py` where filename is the name of your file.
- Here are some examples of python programs that you can run on Pi:

  - Hello world: This is the simplest program that prints "Hello, world!" on the screen. To write this program, type the following code in your editor and save it as hello.py:

    ```python
    print("Hello, world!")
    ```

  - Blink an LED: This is a program that uses the GPIO pins on Pi to control an LED. To write this program, you need to connect an LED to a resistor and then to pin 11 (GPIO 17) and pin 6 (ground) on Pi. You also need to import the GPIO library and the time library in your code. Type the following code in your editor and save it as blink.py:

    ```python
    import RPi.GPIO as GPIO # Import the GPIO library
    import time # Import the time library

    GPIO.setmode(GPIO.BOARD) # Set the numbering mode to board
    GPIO.setup(11, GPIO.OUT) # Set pin 11 as output

    while True: # Loop forever
      GPIO.output(11, True) # Turn on the LED
      time.sleep(1) # Wait for 1 second
      GPIO.output(11, False) # Turn off the LED
      time.sleep(1) # Wait for 1 second
    ```

  - Read a button: This is a program that uses the GPIO pins on Pi to read the state of a button. To write this program, you need to connect a button to pin 12 (GPIO 18) and pin 6 (ground) on Pi. You also need to import the GPIO library in your code. Type the following code in your editor and save it as button.py:

    ```python
    import RPi.GPIO as GPIO # Import the GPIO library

    GPIO.setmode(GPIO.BOARD) # Set the numbering mode to board
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 12 as input with a pull-up resistor

    while True: # Loop forever
      if GPIO.input(12) == False: # If the button is pressed
        print("Button pressed") # Print a message
      else: # If the button is not pressed
        print("Button released") # Print a message
    ```