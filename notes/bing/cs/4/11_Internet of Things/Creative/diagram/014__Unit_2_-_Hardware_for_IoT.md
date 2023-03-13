## Unit 2 - Hardware for IoT

The following diagram illustrates the basic architecture of a hardware device for IoT applications. It consists of three main components: sensors, microcontrollers, and communication modules. Sensors are used to collect data from the environment, such as temperature, humidity, motion, etc. Microcontrollers are used to process the data and execute the logic of the application. Communication modules are used to transmit and receive data over wireless networks, such as Wi-Fi, Bluetooth, ZigBee, etc.

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Sensors      |       |  Microcontrollers      |  Communication  |
|                 |       |                 |       |    Modules      |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  - Temperature  |       |  - Arduino      |       |  - Wi-Fi        |
|  - Humidity     |       |  - Raspberry Pi |       |  - Bluetooth    |
|  - Motion       |       |  - ESP32        |       |  - ZigBee       |
|  - ...          |       |  - ...          |       |  - ...          |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```