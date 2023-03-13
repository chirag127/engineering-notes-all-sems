## Unit 7 - IoT Applications

An IoT application is a software system that uses data from connected devices and sensors to provide value to the end users. IoT applications can be deployed in various domains, such as smart home, smart city, smart agriculture, smart healthcare, smart industry, and so on.

A basic IoT architecture consists of three layers:

- Perception layer: This layer consists of the sensors, gadgets, and other devices that collect data from the physical world and convert it into digital signals. The devices can be embedded, wearable, or mobile, and can have different capabilities and protocols. The perception layer is also responsible for device management, security, and authentication.
- Network layer: This layer consists of the connectivity between devices and the cloud or edge computing platforms. The network layer can use various technologies, such as Wi-Fi, Bluetooth, cellular, LoRaWAN, Zigbee, etc. The network layer is also responsible for data transmission, routing, aggregation, and filtering.
- Application layer: This layer consists of the software applications that interact with the end users and provide value-added services based on the data from the devices. The application layer can use various technologies, such as web, mobile, or desktop apps, dashboards, analytics, machine learning, etc. The application layer is also responsible for data storage, processing, visualization, and decision making.

The following diagram illustrates the basic architecture of an IoT application using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Perception     |     |   Network       |     |  Application    |
|  Layer          |     |   Layer         |     |  Layer          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Devices        |     |  Connectivity   |     |  Applications   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Sensors        |     |  Wi-Fi          |     |  Web App        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Gadgets        |     |  Bluetooth      |     |  Mobile App     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Other Devices  |     |  Cellular       |     |  Desktop App    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Device         |     |  LoRaWAN        |     |  Dashboard      |
|  Management     |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Security       |     |  Zigbee         |     |  Analytics      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Authentication |     |  Other          |     |  Machine        |
|                 |     |  Technologies   |     |  Learning       |
+-----------------+     +-----------------+     +-----------------+
```