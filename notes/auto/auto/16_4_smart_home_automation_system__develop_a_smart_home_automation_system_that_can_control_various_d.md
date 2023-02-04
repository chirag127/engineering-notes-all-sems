4. Smart Home Automation System: Develop a smart home automation system that can control various devices and appliances in a user's home. Utilize IoT technologies and protocols such as MQTT and Bluetooth Low Energy to connect devices and transmit data. Tools such as Raspberry Pi, Node-RED, and Home Assistant can be used to build the system.

Sure, here is a sample code for the development of a smart home automation system using Raspberry Pi, Node-RED, and Home Assistant.

```
# Import necessary libraries
import paho.mqtt.client as mqtt
import bluetooth

# Define MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("home/devices")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# Initialize MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect("localhost", 1883, 60)

# Start MQTT client loop
client.loop_start()

# Scan for available Bluetooth devices
nearby_devices = bluetooth.discover_devices()

# Loop through each device and connect
for bdaddr in nearby_devices:
    print(bluetooth.lookup_name(bdaddr))
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bdaddr, 1))
    sock.send("Hello World!")
    sock.close()

# Stop MQTT client loop
client.loop_stop()
```

This code uses the Paho MQTT library to connect to an MQTT broker and subscribe to the "home/devices" topic. It also uses the Bluetooth library to scan for nearby Bluetooth devices and connect to them. The code sends a message "Hello World!" to each device after connecting.

Note: This code is just a sample and may need to be customized and expanded based on the specific requirements of your project.
