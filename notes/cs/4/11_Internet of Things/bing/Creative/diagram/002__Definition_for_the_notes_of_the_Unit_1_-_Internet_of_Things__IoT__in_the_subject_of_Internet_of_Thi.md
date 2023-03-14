The Internet of Things (IoT) is the concept of connecting any device (so long as it has an on/off switch) to the Internet and to other connected devices. The IoT is a giant network of connected things and people – all of which collect and share data about the way they are used and about the environment around them .

The following diagram illustrates the basic architecture of a typical IoT system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   IoT Devices   |     |   IoT Gateway   |     |   IoT Platform  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| - Sensors       |     | - Data filtering|     | - Data storage  |
| - Actuators     |     | - Data analysis |     | - Data analysis |
| - Connectivity  |     | - Connectivity  |     | - Connectivity  |
|                 |     |                 |     | - Applications  |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Data and      |     |   Data and      |     |   Data and      |
|   commands      |     |   commands      |     |   commands      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Physical      |     |   Physical      |     |   Cloud         |
|   world         |     |   world         |     |   computing     |
|                 |     |                 |     |   environment   |
+-----------------+     +-----------------+     +-----------------+
```

The IoT devices are the physical objects that have sensors, actuators and connectivity capabilities. They can collect data from the environment, perform actions, and communicate with other devices or systems. Examples of IoT devices are smart thermostats, wearable fitness trackers, connected cars, etc.

The IoT gateway is a device or software that acts as a bridge between the IoT devices and the IoT platform. It can filter, analyze, and aggregate the data from the IoT devices before sending it to the IoT platform. It can also receive commands from the IoT platform and relay them to the IoT devices. Examples of IoT gateways are Raspberry Pi, Arduino, etc.

The IoT platform is a cloud-based service that provides the infrastructure and tools for storing, processing, and analyzing the data from the IoT devices. It can also enable the development and deployment of applications that use the IoT data to provide value-added services. Examples of IoT platforms are IBM Watson IoT, Microsoft Azure IoT, etc.