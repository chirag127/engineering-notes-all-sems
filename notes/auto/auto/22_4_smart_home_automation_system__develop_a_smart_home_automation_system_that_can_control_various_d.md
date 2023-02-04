4. Smart Home Automation System: Develop a smart home automation system that can control various devices and appliances in a user's home. Utilize IoT technologies and protocols such as MQTT and Bluetooth Low Energy to connect devices and transmit data. Tools such as Raspberry Pi, Node-RED, and Home Assistant can be used to build the system.

Sure, here's a sample code in Python using Raspberry Pi and Node-RED to build a smart home automation system:

```
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("home/light")

def on_message(client, userdata, msg):
    if msg.payload.decode() == "on":
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
```

This code uses the Paho MQTT library to connect to a MQTT broker and subscribe to a topic `home/light`. The `on_connect` and `on_message` functions are used to handle the connection and incoming messages, respectively. When a message is received with payload `"on"`, the code sets the state of GPIO pin 17 to high, which can be used to control a light or other device. When the message payload is `"off`, the GPIO pin is set to low.

This is just a basic sample code, you can extend it to add more devices and improve the overall functionality of the smart home automation system. Additionally, you can use Node-RED to create a graphical user interface for controlling the devices and visualize the data from the sensors.
