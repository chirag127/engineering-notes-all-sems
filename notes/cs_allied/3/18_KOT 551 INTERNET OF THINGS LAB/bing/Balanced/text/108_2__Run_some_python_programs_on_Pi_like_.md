# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on the Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on the Pi, you need to have a python interpreter installed on your system. The Pi comes with two versions of python pre-installed: python 2 and python 3. You can check which version you have by typing `python --version` or `python3 --version` in the terminal.
- To write a python program, you can use any text editor of your choice, such as nano, vim, or IDLE. You can also use an integrated development environment (IDE) such as Thonny, which provides a graphical user interface (GUI) for editing and running python code.
- To run a python program, you need to save it with a `.py` extension and execute it with the python interpreter. For example, if you have a file called `hello.py` that contains the following code:

```python
print("Hello, world!")
```

You can run it by typing `python hello.py` or `python3 hello.py` in the terminal, depending on which version of python you want to use. You should see the output `Hello, world!` on the screen.

- There are many python programs that you can run on the Pi to explore its features and capabilities. Some examples are:

  - Blinking an LED: You can use the GPIO (general-purpose input/output) pins on the Pi to control external devices, such as LEDs, buttons, sensors, etc. You can use the `gpiozero` library to simplify the process of working with GPIO pins. For example, the following code will blink an LED connected to pin 17:

  ```python
  from gpiozero import LED
  from time import sleep

  led = LED(17)

  while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
  ```

  - Taking a photo: You can use the Pi camera module to capture images and videos with the Pi. You can use the `picamera` library to control the camera settings and functions. For example, the following code will take a photo and save it as `image.jpg`:

  ```python
  from picamera import PiCamera
  from time import sleep

  camera = PiCamera()

  camera.start_preview()
  sleep(5)
  camera.capture('image.jpg')
  camera.stop_preview()
  ```

  - Playing a sound: You can use the `pygame` library to play sounds and music on the Pi. You can use the `mixer` module to load and play sound files. For example, the following code will play a sound file called `sound.wav`:

  ```python
  import pygame
  from pygame.locals import *

  pygame.init()
  pygame.mixer.init()

  sound = pygame.mixer.Sound('sound.wav')
  sound.play()

  while pygame.mixer.get_busy():
    pygame.time.wait(100)
  ```

- These are just some examples of python programs that you can run on the Pi. You can find more examples and tutorials on the official Raspberry Pi website or other online resources. You can also create your own python programs and experiment with different features and functions of the Pi. Have fun!