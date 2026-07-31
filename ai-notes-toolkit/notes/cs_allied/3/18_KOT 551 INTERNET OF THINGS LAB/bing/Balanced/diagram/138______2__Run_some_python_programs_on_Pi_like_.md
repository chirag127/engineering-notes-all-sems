#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- You also need to have a text editor or an IDE (Integrated Development Environment) to write and edit your python code. You can use the default text editor on Pi, which is called `nano`, or you can install other editors like `Thonny` or `Mu`. To install Thonny, type `sudo apt install thonny`. To install Mu, type `pip3 install mu-editor`.
- To write a python program, you need to create a file with the `.py` extension, such as `hello.py`. You can use any text editor to create and save the file in your Pi directory. To open the file with nano, type `nano hello.py` in the terminal. To open the file with Thonny or Mu, launch the editor from the menu or the terminal and then open the file from the editor.
- To run a python program, you need to use the `python3` command followed by the name of the file, such as `python3 hello.py`. This will execute the code in the file and display the output in the terminal. If you are using Thonny or Mu, you can also run the program from the editor by clicking the run button.
- Some examples of python programs that you can run on Pi are:

  - A program that prints "Hello, world!" to the terminal. The code is:

    ```python
    print("Hello, world!")
    ```

  - A program that asks the user for their name and then greets them. The code is:

    ```python
    name = input("What is your name? ")
    print("Hello, " + name + "!")
    ```

  - A program that blinks an LED connected to the Pi's GPIO pin. The code is:

    ```python
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM) # use BCM numbering scheme for the pins
    GPIO.setup(18, GPIO.OUT) # set pin 18 as output

    while True: # loop forever
      GPIO.output(18, GPIO.HIGH) # turn on the LED
      time.sleep(1) # wait for 1 second
      GPIO.output(18, GPIO.LOW) # turn off the LED
      time.sleep(1) # wait for 1 second
    ```