### Mobiles for the notes of the Unit 7 - IoT Applications in the subject of Internet of Things

The following diagram illustrates the basic architecture of a mobile IoT application, based on the information from the search results     :

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Mobile App    |     |   IoT Devices   |     |   Cloud Server  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  User Interface |     |  Sensors/Actors |     |  Data Storage   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Business Logic |     |  Device Logic   |     |  Application    |
|                 |     |                 |     |  Logic/Services |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Data Access    |     |  Data Access    |     |  Data Access    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Network Layer  |     |  Network Layer  |     |  Network Layer  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        |                     |                         |
        +---------------------+-------------------------+
                            Network
```

The mobile app is the interface that the user interacts with to control and monitor the IoT devices. It contains the user interface, the business logic, the data access and the network layer components.

The IoT devices are the sensors, actuators, gadgets and other physical components that are connected to the network and the cloud server. They contain the device logic, the data access and the network layer components.

The cloud server is the central platform that provides data storage, application logic and services for the mobile app and the IoT devices. It contains the data storage, the application logic, the data access and the network layer components.

The network is the communication channel that connects the mobile app, the IoT devices and the cloud server. It can use various protocols and technologies, such as Wi-Fi, Bluetooth, cellular, LoRaWAN, etc.