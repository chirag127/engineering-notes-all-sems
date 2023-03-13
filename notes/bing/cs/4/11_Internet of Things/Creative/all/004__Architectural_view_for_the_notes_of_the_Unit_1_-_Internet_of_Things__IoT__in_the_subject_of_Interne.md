### Architectural view for the notes of the Unit 1 - Internet of Things (IoT) in the subject of Internet of Things

- The architectural view of IoT is a way of describing the design and implementation of a concrete system architecture that uses IoT devices and services.
- A view is composed of viewpoints, which aggregate several architectural concepts in order to make the work with views easier.
- There are different ways of defining the architectural view of IoT, but one of the most common and basic ones is the 4-stage IoT architecture , which consists of the following layers:
  - **Device layer**: This layer deals with the establishment of the physical layer in the environment. It includes the sensors and actuators that collect and capture the data from the devices and systems that are under control and observation. The device layer also performs some local processing and filtering of the data before sending it to the network layer.
  - **Network layer**: This layer deals with the transportation of the data from the device layer to the cloud layer. It includes all the network devices and protocols that enable the communication and connectivity of the IoT devices. The network layer can use different types of networks, such as wired, wireless, cellular, or satellite. The network layer also performs some security and encryption functions to protect the data in transit.
  - **Cloud layer**: This layer deals with the storage, processing, analysis, and management of the data from the network layer. It includes the cloud platforms and services that provide the computing and storage resources for the IoT applications. The cloud layer can use different types of cloud models, such as public, private, or hybrid. The cloud layer also performs some data analytics and machine learning functions to extract insights and value from the data.
  - **Application layer**: This layer deals with the presentation and visualization of the data and insights from the cloud layer. It includes the applications and dashboards that provide the user interface and interaction for the IoT system. The application layer can use different types of devices, such as smartphones, tablets, or laptops. The application layer also performs some feedback and control functions to enable the user to interact with the IoT devices and systems.

- A possible mnemonic to remember the 4-stage IoT architecture is **DANC** (Device, Network, Cloud, Application).
- A possible ascii diagram to illustrate the 4-stage IoT architecture is:

```
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  Application    |     |     Cloud       |     |    Network      |     |    Device       |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  Visualization  |     |   Data storage  |     |  Communication  |     |  Data capture   |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  Feedback and   |     |   Data analysis |     |  Security and   |     |  Local          |
|  control        |     |                 |     |  encryption     |     |  processing     |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
```