# Functional View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The functional view of the IoT reference architecture describes the system's runtime functional components, their responsibilities, default functions, interfaces and primary interactions .
- The functional view follows the modular structure of functional blocks organized into layers, as it was proposed e.g. in SENSEI.
- The functional view is use-case- and application-independent and is therefore not compatible to the concept of views and viewpoints one-by-one.
- The functional view consists of four main layers: Device Layer, Network Layer, Service Layer and Application Layer .
- The Device Layer contains the physical devices that are connected to the IoT system, such as sensors, actuators, gateways, etc. The Device Layer is responsible for data acquisition, device management, device discovery and device configuration.
- The Network Layer provides the communication infrastructure and protocols for data transmission between devices and services. The Network Layer is responsible for network management, network discovery, network security and network optimization.
- The Service Layer provides the core functionalities and services of the IoT system, such as data processing, data storage, data analysis, data visualization, etc. The Service Layer is responsible for service management, service discovery, service composition and service orchestration.
- The Application Layer contains the specific applications and use cases that utilize the IoT system, such as smart home, smart city, smart health, etc. The Application Layer is responsible for application management, application discovery, application integration and application customization.
- The functional view also defines the cross-layer functionalities that span across multiple layers, such as security, privacy, trust, identity, etc. These functionalities are responsible for ensuring the reliability, safety, and quality of the IoT system.
- The functional view can be represented by a diagram that shows the functional components, their interfaces, and their interactions. An example of such a diagram is shown below :

```
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Device        |
|    Layer        |      |    Layer        |      |    Layer        |      |    Layer        |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Device        |
|  Management     |      |  Management     |      |  Management     |      |  Management     |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Device        |
|  Discovery      |      |  Discovery      |      |  Discovery      |      |  Discovery      |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Device        |
|  Integration    |      |  Composition    |      |  Security       |      |  Configuration  |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Data          |
|  Customization  |      |  Orchestration  |      |  Optimization   |      |  Acquisition    |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |