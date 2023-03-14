## Unit 2 - Hardware for IoT

The hardware for IoT consists of devices that can sense, process, and communicate data over a network. The basic components of IoT hardware are sensors, microcontrollers, and communication modules. The following diagram illustrates the basic architecture of an IoT device using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Sensor       |    |  Microcontroller|    | Communication   |
|                 |    |                 |    | Module          |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Analog signal  |----| Analog to       |----| Digital signal  |
|                 |    | Digital         |    |                 |
|                 |    | Converter       |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

A sensor is a device that measures a physical quantity and converts it into an electrical signal. Sensors can detect various parameters such as temperature, humidity, pressure, light, sound, motion, etc. Sensors are the most critical hardware in IoT applications and are used to gather information from the surroundings .

A microcontroller is a small computer on a single chip that can execute instructions and perform calculations. Microcontrollers are used to process the data from the sensors and control the device's behavior. Microcontrollers can also have built-in memory, timers, and input/output ports .

A communication module is a device that enables data transmission and reception over a network. Communication modules can use different protocols and technologies such as Wi-Fi, Bluetooth, ZigBee, cellular, LoRa, etc. Communication modules are responsible for connecting the IoT device to the cloud or other devices .