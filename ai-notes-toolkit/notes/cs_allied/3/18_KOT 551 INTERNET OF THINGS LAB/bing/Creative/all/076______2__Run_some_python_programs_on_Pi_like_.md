#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python --version` or `python3 --version` in the terminal. If you don't have one, you can install it by typing `sudo apt install python3` or `sudo apt install python` depending on the version you want.
- You also need to have a text editor or an IDE (Integrated Development Environment) to write and edit your python code. You can use the default text editor on Pi, which is called `nano`, or you can install other editors like `vim`, `emacs`, `geany`, `thonny`, etc. by typing `sudo apt install <editor-name>` in the terminal.
- To write a python program, you need to create a file with the `.py` extension, such as `hello.py`. You can do this by typing `nano hello.py` in the terminal, which will open the `nano` editor with a blank file named `hello.py`. You can then type your python code in the editor, such as `print("Hello, world!")`, and save the file by pressing `Ctrl+O` and then `Enter`. You can exit the editor by pressing `Ctrl+X`.
- To run a python program, you need to type `python hello.py` or `python3 hello.py` in the terminal, depending on the version of python you are using. This will execute the code in the file and display the output on the screen, such as `Hello, world!`.
- You can also run a python program interactively, without saving it to a file, by typing `python` or `python3` in the terminal. This will open the python shell, where you can type and execute python commands one by one, such as `print("Hello, world!")`. You can exit the python shell by typing `exit()` or pressing `Ctrl+D`.
- Some examples of python programs that you can run on Pi are:

  - A program that prints the current date and time:

    ```python
    import datetime
    now = datetime.datetime.now()
    print("The current date and time is:", now)
    ```

  - A program that blinks an LED connected to a GPIO pin:

    ```python
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    while True:
      GPIO.output(18, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(18, GPIO.LOW)
      time.sleep(1)
    ```

  - A program that reads the temperature and humidity from a DHT11 sensor connected to a GPIO pin:

    ```python
    import Adafruit_DHT
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4
    while True:
      humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
      if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
      else:
        print("Sensor failure. Check wiring.")
      time.sleep(3)
    ```