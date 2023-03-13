## Unit 1 - Internet of Things (IoT)

The Internet of Things (IoT) is a network of physical devices (so-called “things”) that collect and exchange data with other devices and systems over the internet. IoT architecture is the structure enabling internet-connected devices to communicate with other devices. There is no single standard reference architecture for IoT as it encompasses a variety of technologies, but a common way to describe IoT architecture is by using four layers: device, gateway, cloud, and application    .

The following diagram illustrates the basic architecture of an IoT system using ASCII art:

```
+----------------+      +----------------+      +----------------+      +----------------+
|                |      |                |      |                |      |                |
|  Application   |<---->|     Cloud      |<---->|    Gateway     |<---->|     Device     |
|                |      |                |      |                |      |                |
+----------------+      +----------------+      +----------------+      +----------------+
|                |      |                |      |                |      |                |
| - User         |      | - Data storage |      | - Data         |      | - Sensor       |
| - Interface    |      | - Data analysis|      |   processing   |      | - Actuator     |
| - Logic        |      | - Data security|      | - Data security|      | - Controller   |
|                |      |                |      |                |      |                |
+----------------+      +----------------+      +----------------+      +----------------+
```

The device layer is the layer closest to the physical world and consists of the sensors, actuators, and other devices that collect data and perform actions. The devices can communicate with the gateway layer using various protocols, such as Bluetooth, Wi-Fi, ZigBee, etc.

The gateway layer is the layer that connects the device layer with the cloud layer. It is responsible for data processing, data security, and data transmission. The gateway can be a dedicated device, such as a router, or a software component, such as a smartphone app. The gateway can communicate with the cloud layer using protocols, such as MQTT, HTTP, CoAP, etc.

The cloud layer is the layer that provides data storage, data analysis, and data security for the IoT system. It can also enable remote access and control of the devices. The cloud can be a public cloud, such as AWS, Azure, or Google Cloud, or a private cloud, such as a local server.

The application layer is the layer that provides the user interface, the logic, and the functionality of the IoT system. It can be a web app, a mobile app, a desktop app, or any other software that interacts with the user and the devices. The application can communicate with the cloud layer using protocols, such as REST, WebSocket, etc.