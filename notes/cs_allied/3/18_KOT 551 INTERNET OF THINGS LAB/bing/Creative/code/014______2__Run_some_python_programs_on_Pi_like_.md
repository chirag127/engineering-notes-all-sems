#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- You also need to have a text editor or an IDE (Integrated Development Environment) to write and edit your python code. You can use the default text editor on Pi, which is called `nano`, or you can install other editors like `Thonny` or `Mu`. To install Thonny, type `sudo apt install thonny`. To install Mu, type `pip3 install mu-editor`.
- To write a python program, you need to create a file with the `.py` extension, such as `hello.py`. You can use any text editor to create and save the file in your preferred location. To run the program, you need to navigate to the folder where the file is located, and type `python3 hello.py` in the terminal. This will execute the code in the file and display the output in the terminal.
- Some examples of python programs that you can run on Pi are:

  - A program that prints "Hello, world!" to the terminal. The code for this program is:

    ```python
    print("Hello, world!")
    ```

  - A program that blinks an LED connected to the Pi's GPIO (General Purpose Input/Output) pins. The code for this program is:

    ```python
    import RPi.GPIO as GPIO # Import the GPIO library
    import time # Import the time library

    GPIO.setmode(GPIO.BCM) # Set the GPIO mode to BCM
    GPIO.setup(18, GPIO.OUT) # Set pin 18 as an output pin

    try:
      while True: # Loop forever
        GPIO.output(18, GPIO.HIGH) # Turn on the LED
        time.sleep(1) # Wait for 1 second
        GPIO.output(18, GPIO.LOW) # Turn off the LED
        time.sleep(1) # Wait for 1 second
    except KeyboardInterrupt: # If the user presses Ctrl+C
      GPIO.cleanup() # Clean up the GPIO pins
    ```

  - A program that reads the temperature and humidity from a DHT11 sensor connected to the Pi's GPIO pins. The code for this program is:

    ```python
    import Adafruit_DHT # Import the Adafruit_DHT library
    import time # Import the time library

    DHT_SENSOR = Adafruit_DHT.DHT11 # Set the sensor type to DHT11
    DHT_PIN = 4 # Set the pin number to 4

    while True: # Loop forever
      humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN) # Read the humidity and temperature from the sensor
      if humidity is not None and temperature is not None: # If the readings are valid
        print(f"Temp={temperature:.1f}C Humidity={humidity:.1f}%") # Print the readings to the terminal
      else: # If the readings are invalid
        print("Sensor failure. Check wiring.") # Print an error message to the terminal
      time.sleep(3) # Wait for 3 seconds
    ```