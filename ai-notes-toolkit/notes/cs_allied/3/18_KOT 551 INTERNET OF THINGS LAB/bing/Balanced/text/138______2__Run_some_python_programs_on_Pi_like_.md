#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your device. Python is a high-level, interpreted, and general-purpose programming language that can run on various platforms, including Pi.
- Pi comes with two versions of python pre-installed: python 2 and python 3. You can check the version of python by typing `python --version` or `python3 --version` in the terminal. You can also use the `which` command to find the location of the python executable, such as `which python` or `which python3`.
- To write a python program, you can use any text editor of your choice, such as nano, vim, or IDLE. You can also use an integrated development environment (IDE) such as Thonny, which is designed for beginners and comes with Pi. To launch Thonny, go to the main menu and select Programming > Thonny Python IDE.
- To save a python program, you need to give it a name with the `.py` extension, such as `hello.py`. You can save the program in any directory of your choice, but it is recommended to create a separate folder for your python projects, such as `~/python_projects`.
- To run a python program, you can use the terminal or the IDE. If you use the terminal, you need to navigate to the directory where your program is saved, and then type `python` or `python3` followed by the name of your program, such as `python hello.py` or `python3 hello.py`. If you use the IDE, you can open your program and click the Run button or press F5.
- A simple python program that prints "Hello, world!" to the screen is:

```python
# This is a comment
print("Hello, world!") # This is another comment
```

- Some examples of python programs that you can run on Pi are:

  - A program that blinks an LED connected to a GPIO pin:

```python
# Import the GPIO library
import RPi.GPIO as GPIO
# Import the time library
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Set the GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT)

# Loop forever
while True:
  # Turn on the LED
  GPIO.output(18, GPIO.HIGH)
  # Wait for one second
  time.sleep(1)
  # Turn off the LED
  GPIO.output(18, GPIO.LOW)
  # Wait for one second
  time.sleep(1)
```

  - A program that reads the temperature and humidity from a DHT11 sensor connected to a GPIO pin:

```python
# Import the DHT library
import Adafruit_DHT
# Import the time library
import time

# Set the sensor type to DHT11
sensor = Adafruit_DHT.DHT11
# Set the GPIO pin 4 as input
pin = 4

# Loop forever
while True:
  # Read the temperature and humidity from the sensor
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  # Check if the readings are valid
  if humidity is not None and temperature is not None:
    # Print the readings to the screen
    print(f"Temperature: {temperature} C, Humidity: {humidity} %")
  else:
    # Print an error message
    print("Failed to read from the sensor")
  # Wait for two seconds
  time.sleep(2)
```

  - A program that plays a sound file using the pygame library:

```python
# Import the pygame library
import pygame
# Import the time library
import time

# Initialize the pygame mixer
pygame.mixer.init()
# Load a sound file
sound = pygame.mixer.Sound("sound.wav")
# Play the sound
sound.play()
# Wait for the sound to finish
time.sleep(sound.get_length())
# Quit the pygame mixer
pygame.mixer.quit()
```