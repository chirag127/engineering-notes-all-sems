The following is a detailed ASCII diagram for communicating data with H/W units for the notes of the Unit 7 - IoT Applications in the subject of Internet of Things.

The diagram shows a typical IoT system that consists of three layers: the device layer, the network layer, and the application layer. The device layer contains the IoT devices that are embedded with sensors, actuators, and software to collect, process, and transmit data. The network layer provides the connectivity and communication protocols for the IoT devices to send and receive data over the internet. The application layer provides the services and applications that use the data from the IoT devices for various purposes, such as analytics, visualization, control, etc.

The diagram also shows the types of communication that can occur in an IoT system, such as human-to-machine (H2M), machine-to-machine (M2M), and machine-to-human (M2H). H2M communication involves a human giving input to an IoT device, such as speech, text, image, etc. The IoT device then understands, analyzes, and responds to the human input. M2M communication involves IoT devices exchanging data and commands with each other, without any human involvement. M2H communication involves an IoT device sending data or feedback to a human, such as text, image, sound, etc. The human can then view, interpret, or act on the data or feedback.

The diagram uses the following symbols and conventions:

- A rectangle represents an IoT device, such as a sensor, an actuator, a camera, etc.
- A circle represents a network node, such as a router, a gateway, a server, etc.
- A cloud represents a cloud service or platform, such as Azure, AWS, Google Cloud, etc.
- A dashed line represents a wired connection, such as Ethernet, USB, etc.
- A solid line represents a wireless connection, such as Wi-Fi, Bluetooth, Zigbee, etc.
- An arrow represents the direction of data flow or communication.
- A label represents the type or name of the data or communication.

The diagram is as follows:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  IoT Device 1  |     |  IoT Device 2  |     |  IoT Device 3  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Gateway 1     |     |  Gateway 2     |     |  Gateway 3     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Router 1      |     |  Router 2      |     |  Router 3      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Server 1      |     |  Server 2      |     |  Server 3      |
|                |     |                |