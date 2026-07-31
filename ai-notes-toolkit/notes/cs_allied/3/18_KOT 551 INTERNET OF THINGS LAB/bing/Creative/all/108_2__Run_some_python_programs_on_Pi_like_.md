# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on the Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on the Pi, you need to have a python interpreter installed on the Pi. The Pi comes with two versions of python: python 2 and python 3. You can check which version you have by typing `python --version` or `python3 --version` in the terminal.
- You also need to have a text editor or an IDE (Integrated Development Environment) to write and edit your python code. The Pi comes with some pre-installed editors, such as Thonny, IDLE, Geany, etc. You can also install other editors, such as VS Code, PyCharm, etc.
- To run a python program on the Pi, you can either use the terminal or the editor. In the terminal, you can type `python filename.py` or `python3 filename.py` to execute the python file. In the editor, you can use the run or debug option to run the python file.
- Here are some examples of python programs that you can run on the Pi:

  - Hello World: This is the simplest python program that prints "Hello World" on the screen. To write this program, you need to create a file named `hello.py` and write the following code:

    ```python
    print("Hello World")
    ```

    To run this program, you can type `python hello.py` or `python3 hello.py` in the terminal, or use the run option in the editor. You should see the output "Hello World" on the screen.

  - Blink LED: This is a python program that uses the GPIO (General Purpose Input Output) pins on the Pi to control an LED. To write this program, you need to have an LED, a resistor, some jumper wires, and a breadboard. You also need to install the `gpiozero` library on the Pi, which is a python module that simplifies the interaction with the GPIO pins. You can install it by typing `sudo apt install python3-gpiozero` in the terminal. To write this program, you need to create a file named `blink.py` and write the following code:

    ```python
    from gpiozero import LED
    from time import sleep

    led = LED(17) # create an LED object connected to pin 17
    while True: # loop forever
      led.on() # turn on the LED
      sleep(1) # wait for 1 second
      led.off() # turn off the LED
      sleep(1) # wait for 1 second
    ```

    To run this program, you can type `python blink.py` or `python3 blink.py` in the terminal, or use the run option in the editor. You should see the LED blinking on and off every second.

  - Web Server: This is a python program that uses the `flask` library to create a simple web server on the Pi. To write this program, you need to install the `flask` library on the Pi, which is a python framework that allows you to create web applications. You can install it by typing `sudo pip install flask` or `sudo pip3 install flask` in the terminal. To write this program, you need to create a file named `app.py` and write the following code:

    ```python
    from flask import Flask
    app = Flask(__name__) # create a Flask object

    @app.route('/') # define the route for the home page
    def index():
      return "Hello from Raspberry Pi" # return a string as the response

    if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80) # run the app on port 80
    ```

    To run this program, you can type `python app.py` or `python3 app.py` in the terminal, or use the run option in the editor. You should see a message saying "Running on http://0.0.0.0:80/" on the terminal. You can then open a web browser on any device connected to the same network as the Pi, and type the Pi's IP address in the address bar. You should see the message "Hello from Raspberry Pi" on the web page.