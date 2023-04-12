### Conceptual Framework for the notes of the Unit 1 - Internet of Things (IoT): Vision, Definition, Conceptual Framework, Architectural view, technology behind IoT, Sources of the IoT, M2M Communication, IoT Examples. Design Principles for Connected Devices: IoT/M2M systems layers and design standardization, communication technologies, data enrichment and consolidation, ease of designing and affordability in the subject of INTRODUCTION TO INTERNET OF THINGS

- Internet of Things (IoT) is a network of physical objects or things that are embedded with sensors, actuators, controllers, and communication devices that enable them to exchange data and interact with other devices or systems via the internet .
- The vision of IoT is to create a smart, connected, and ubiquitous world where physical objects can be monitored, controlled, and automated remotely, and where data can be collected, processed, and analyzed to generate insights and value for various applications and domains.
- A conceptual framework for IoT is a way of describing the main components, functions, and relationships of an IoT system. It can help to understand the challenges, opportunities, and requirements of IoT, and to design and implement IoT solutions.
- A simple conceptual framework for IoT can be represented as follows:

```
Physical object + Controller, Sensor and Actuators + Internet = Internet of Things
```

- This framework shows that an IoT system consists of three main elements:
  - Physical object: the thing that is being connected and monitored, such as a car, a fridge, a lamp, etc.
  - Controller, Sensor and Actuators: the devices that enable the physical object to sense, measure, and act on its environment, and to communicate with other devices or systems, such as a microcontroller, a temperature sensor, a motor, etc.
  - Internet: the network that connects the physical object and its devices to other devices or systems, such as a cloud server, a smartphone, a web application, etc.

- An IoT system can also be described by the following functions:

```
Gather + Enrich + Stream + Manage + Acquire + Organize and Analyze = Internet of Things
```

- This framework shows that an IoT system performs the following functions:
  - Gather: the physical object and its devices collect data from their environment, such as temperature, humidity, location, etc.
  - Enrich: the data is processed and enhanced by the devices or by other systems, such as adding timestamps, encryption, compression, etc.
  - Stream: the data is transmitted and received by the devices or other systems via the internet, using various protocols and standards, such as MQTT, HTTP, CoAP, etc.
  - Manage: the devices and systems are configured, monitored, and controlled remotely, using various tools and platforms, such as IoT Hub, Azure IoT Central, etc.
  - Acquire: the data is stored and accessed by the devices or other systems, using various databases and services, such as SQL, NoSQL, Blob Storage, etc.
  - Organize and Analyze: the data is structured and processed by the devices or other systems, using various methods and techniques, such as machine learning, artificial intelligence, big data analytics, etc.

- An architectural view of IoT is a way of depicting the different layers, components, and interfaces of an IoT system. It can help to understand the design and implementation of IoT solutions, and to identify the challenges and opportunities of each layer.
- A common architectural view of IoT can be represented as follows:

```
+-----------------+    +-----------------+    +-----------------+
| Application     |    | Application     |    | Application     |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
| Service         |    | Service         |    | Service         |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
|

```
