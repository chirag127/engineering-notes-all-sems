The following diagram illustrates the basic architecture of communicating data with H/W units for the notes of the Unit 7 - IoT Applications in the subject of Internet of Things.

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   IoT Device    |       |   IoT Gateway   |       |   IoT Platform  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Sensors/       |       |  Protocol       |       |  Data Storage   |
|  Actuators      |       |  Translation    |       |                 |
|                 |       |                 |       |                 |
|  Embedded       |       |  Data           |       |  Data Analysis  |
|  System         |       |  Processing     |       |                 |
|                 |       |                 |       |                 |
|  Connectivity   |       |  Connectivity   |       |  Connectivity   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Data           |       |  Data           |       |  Data           |
|  Transmission   |       |  Transmission   |       |  Transmission   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  IoT Protocols  |       |  IoT Protocols  |       |  IoT Protocols  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Radio Signal   |       |  Radio Signal   |       |  Internet       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows the three main components of an IoT system: the device, the gateway, and the platform. The device is the hardware unit that collects data from sensors or performs actions with actuators. The device has an embedded system that controls its functions and a connectivity module that allows it to communicate with other devices or the gateway. The device uses IoT protocols such as Wi-Fi, Bluetooth, or Satellite to transmit data wirelessly over radio signal .

The gateway is the intermediary between the device and the platform. The gateway can perform protocol translation, data processing, security, and device management functions. The gateway can also communicate with other devices or gateways using IoT protocols. The gateway uses radio signal or internet to transmit data to the platform .

The platform is the cloud-based service that stores, analyzes, and presents the data collected from the devices. The platform can also provide device management, security, and application integration functions. The platform uses IoT protocols such as HTTP, MQTT, or CoAP to communicate with the gateway or other platforms. The platform uses internet to transmit data to the user or other applications .

The diagram also shows the data transmission flow from the device to the platform and vice versa. The device sends data to the gateway using IoT protocols and radio signal. The gateway receives the data and translates it to a different protocol if needed. The gateway also processes the data and sends it to the platform using IoT protocols and internet. The platform receives the data and stores it in a data storage system. The platform also analyzes the data and presents it to the user or other applications using IoT protocols and internet. The user or other applications can also send commands or requests to the platform using IoT protocols and internet. The platform forwards the commands or requests to the gateway using IoT protocols and internet. The gateway receives the commands or requests and translates them to a different protocol if needed. The gateway also processes the commands or requests and sends them to the device using IoT protocols and radio signal. The device receives the commands or requests and performs the actions or sends the responses using IoT protocols and radio signal   .