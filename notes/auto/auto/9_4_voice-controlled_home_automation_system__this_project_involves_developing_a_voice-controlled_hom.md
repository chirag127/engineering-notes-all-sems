4. Voice-controlled Home Automation System: This project involves developing a voice-controlled home automation system that can control various devices in a home using voice commands. Tools such as Amazon Alexa, Google Home, and Raspberry Pi can be used to implement this project.

Here's a sample code in Python to get you started with the Voice-controlled Home Automation System using Raspberry Pi and Google Assistant:

```
import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
    subprocess.call("google-assistant-demo", shell=True)

GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback, bouncetime=300)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
```

This code uses the Raspberry Pi's GPIO pins to detect a button press. When the button is pressed, it triggers the Google Assistant demo, which allows the user to issue voice commands. The code is set up to run continuously, so the user can issue multiple commands without having to press the button each time.

Note: This is just a sample code to get you started and you can further customize and add additional functionalities as per your requirements.
