Smart metering is a process of measuring, collecting, and analyzing utilities distribution and consumption, and communicating with metering devices either on a schedule or on request. Smart metering solutions use IoT devices and platforms to enable remote monitoring and control of energy consumption, as well as data visualization and analytics. Smart metering can help improve energy efficiency, reduce costs, and support smart grid applications.

The following diagram illustrates the basic architecture of a smart metering solution using IoT:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Smart Meters   |<----->|  Data Collector |<----->|  IoT Platform   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
  |                 \     /                 |       |                 |
  |                  \   /                  |       |                 |
  |                   \ /                   |       |                 |
  |                    X                    |       |                 |
  |                   / \                   |       |                 |
  |                  /   \                  |       |                 |
  |                 /     \                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Utility Grid   |       |  Communication  |       |  Data Analysis  |
|                 |       |  Network        |       |  and Services   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The main components of the architecture are:

- Smart Meters: These are electronic devices that measure and record the energy consumption of the consumers. They can communicate with the data collector and the utility grid using wired or wireless protocols. They can also support remote control and configuration functions.
- Data Collector: This is a device or a software that collects the data from the smart meters and sends it to the IoT platform. It can also perform some data processing and filtering functions. It can communicate with the smart meters and the IoT platform using various protocols, such as ZigBee, Wi-Fi, cellular, or LoRaWAN.
- IoT Platform: This is a cloud-based or on-premise platform that provides the data storage, management, visualization, and analytics functions for the smart metering solution. It can also provide the integration and communication with other services and applications, such as billing, demand response, or smart grid management. It can communicate with the data collector and the data analysis and services using various protocols, such as MQTT, HTTP, or AMQP.
- Data Analysis and Services: These are the applications and services that use the data from the IoT platform to provide various functions, such as energy efficiency, cost reduction, fault detection, or load balancing. They can also provide the user interface and feedback for the consumers and the utility providers. They can communicate with the IoT platform and the communication network using various protocols, such as REST, WebSocket, or CoAP.
- Communication Network: This is the network that connects the data collector, the IoT platform, and the data analysis and services. It can use various technologies, such as Ethernet, Wi-Fi, cellular, or satellite.
- Utility Grid: This is the physical infrastructure that delivers the energy to the consumers and receives the feedback from the smart meters. It can also support the smart grid functions, such as demand response, load management, or distributed generation. It can communicate with the smart meters and the data collector using various protocols, such as PLC, RF, or optical fiber.