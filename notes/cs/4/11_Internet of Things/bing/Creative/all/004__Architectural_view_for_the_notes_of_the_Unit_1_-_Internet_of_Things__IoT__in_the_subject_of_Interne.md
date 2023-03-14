### Architectural view for the notes of the Unit 1 - Internet of Things (IoT) in the subject of Internet of Things

The architectural view of IoT is a way of describing the structure and behavior of an IoT system from different perspectives. It helps to understand the components, relationships, and functionalities of an IoT system, and to design and implement it according to the requirements and constraints. There are different types of architectural views, such as functional, logical, physical, deployment, and security views, that focus on different aspects of an IoT system. However, a common and fundamental architectural view of IoT is the four-stage IoT architecture, which describes the basic process flow of data from devices to applications. The four stages are:

- Sensing layer: This layer consists of sensors and actuators that are attached to physical objects or environments, and that collect and transmit data about various parameters, such as temperature, humidity, light, sound, motion, etc. The sensors and actuators can be passive or active, wired or wireless, and can use different communication protocols, such as WiFi, Bluetooth, Zigbee, or cellular networks. The sensing layer is also known as the perception layer or the edge layer.
- Network layer: This layer provides the connectivity and communication between the sensing layer and the data processing layer. It includes gateways, routers, and other network devices that enable data transmission and routing over the internet or other networks. The network layer can use different network technologies, such as Ethernet, IP, TCP, UDP, MQTT, CoAP, etc. The network layer is also known as the transport layer or the access layer.
- Data processing layer: This layer handles the collection, storage, analysis, and processing of data from the network layer. It includes various software and hardware components, such as databases, data lakes, data warehouses, analytics platforms, machine learning algorithms, cloud services, etc. The data processing layer performs various functions, such as data filtering, aggregation, transformation, normalization, compression, encryption, etc. The data processing layer is also known as the service layer or the platform layer.
- Application layer: This layer provides the user interface and functionality that enable users to access and control the IoT system. It includes various software and applications, such as mobile apps, web portals, dashboards, etc. The application layer delivers various services and solutions based on the data and insights from the data processing layer, such as smart home, smart city, smart health, smart agriculture, etc. The application layer is also known as the presentation layer or the business layer.

The following diagram illustrates the four-stage IoT architecture:

```
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  Application    |     |  Data processing|     |  Network        |     |  Sensing        |
|  layer          |     |  layer          |     |  layer          |     |  layer          |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  Mobile apps    |     |  Data lake      |     |  Gateway        |     |  Sensor         |
|  Web portals    |     |  Analytics      |     |  Router         |     |  Actuator       |
|  Dashboards     |     |  Machine learning|    |  WiFi           |     |  RFID           |
|  Smart services |     |  Cloud services |     |  Bluetooth      |     |  NFC            |
|                 |     |                 |     |  Zigbee         |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  User           |<--->|  Data           |<--->|  Data           |<--->|  Data           |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
```

Some mnemonics and learning tricks for the architectural view of IoT are:

- Remember the four stages as **S**ensing, **N**etwork, **D**ata processing, and **A**pplication, or **SNDA** for short.
- Remember the functions of each stage as **C**ollect, **C**onnect, **A**