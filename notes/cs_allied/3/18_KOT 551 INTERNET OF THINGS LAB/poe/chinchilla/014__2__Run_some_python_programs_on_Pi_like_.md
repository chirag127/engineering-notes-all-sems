#### 2. Run some python programs on Pi like:

Raspberry Pi is a small, affordable, and versatile computer that can be used for a wide range of projects, including running Python programs. Python is a popular programming language that is easy to learn and has a wide range of libraries and tools available for use. In this section, we will look at how to run Python programs on Raspberry Pi.

Here are some steps to follow to run Python programs on Raspberry Pi:

1. Install Python on Raspberry Pi: Before you can run Python programs on Raspberry Pi, you need to make sure that Python is installed on your Pi. Most versions of Raspberry Pi come with Python pre-installed, but you can check by running the following command in the terminal:

   ```
   python --version
   ```

   If Python is not installed, you can install it by running the following command:

   ```
   sudo apt-get install python3
   ```

2. Write a Python program: Once Python is installed on your Raspberry Pi, you can start writing Python programs. You can use any text editor to write your program, such as nano, vi, or emacs. For example, you can create a file called "hello.py" and add the following code:

   ```
   print("Hello, World!")
   ```

3. Run the Python program: To run the Python program, you need to navigate to the directory where the program is saved and run the following command in the terminal:

   ```
   python3 hello.py
   ```

   This will execute the "hello.py" program and print the output "Hello, World!" in the terminal.

4. Use Python libraries: Python has many libraries and modules available that can be used to perform specific tasks. To use a library, you need to install it first. For example, to install the "numpy" library, you can run the following command:

   ```
   sudo apt-get install python3-numpy
   ```

   Once the library is installed, you can import it into your Python program and use its functions. For example, you can create a file called "numpy_test.py" and add the following code:

   ```
   import numpy as np

   x = np.array([1, 2, 3])
   print(x)
   ```

   This program will import the "numpy" library and create a one-dimensional array. It will then print the array to the terminal.

5. Use GPIO pins: Raspberry Pi has GPIO (General-Purpose Input/Output) pins that can be used to interact with the physical world. You can use Python to control these pins and perform tasks such as turning on a LED or reading a sensor. To use GPIO pins in Python, you need to install the "RPi.GPIO" library. You can install it by running the following command:

   ```
   sudo apt-get install python3-rpi.gpio
   ```

   Once the library is installed, you can import it into your Python program and use its functions. For example, you can create a file called "gpio_test.py" and add the following code:

   ```
   import RPi.GPIO as GPIO
   import time

   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(11, GPIO.OUT)

   while True:
       GPIO.output(11, GPIO.HIGH)
       time.sleep(1)
       GPIO.output(11, GPIO.LOW)
       time.sleep(1)
   ```

   This program will use the GPIO pin 11 to turn on and off a LED in a loop with a time delay of 1 second. 

In conclusion, Raspberry Pi is a great platform for running Python programs, and it provides a lot of flexibility and options for developers. By following the above steps, you can start running your own Python programs on Raspberry Pi and explore the possibilities of this powerful combination.