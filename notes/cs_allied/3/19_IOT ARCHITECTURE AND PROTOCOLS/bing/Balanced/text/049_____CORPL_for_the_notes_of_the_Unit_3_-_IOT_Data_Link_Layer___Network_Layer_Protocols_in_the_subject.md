### CORPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CORPL stands for **C**ontrol **O**bjective **R**outing **P**rotocol for **L**ow power and lossy networks.
- It is a network layer protocol designed for IoT applications that require reliable and efficient data delivery in constrained environments.
- It is based on the concept of **control objectives**, which are high-level goals that the network should achieve, such as minimizing delay, maximizing throughput, or balancing energy consumption.
- CORPL uses a distributed algorithm to compute optimal routes based on the control objectives and the network state, such as link quality, traffic load, and node resources.
- CORPL is compatible with the IPv6 Routing Protocol for Low-Power and Lossy Networks (RPL), which is the standard routing protocol for IoT networks.
- CORPL can coexist with other RPL instances that use different control objectives or metrics, and can dynamically switch between them based on the application requirements.
- CORPL has been shown to outperform RPL in terms of packet delivery ratio, end-to-end delay, and energy efficiency in various scenarios, such as smart grid, smart city, and industrial IoT .

Some key points about the IoT data link layer and network layer protocols are:

- The data link layer is responsible for providing reliable and efficient data transmission between adjacent nodes in the network, such as sensors, actuators, gateways, and routers.
- The data link layer consists of protocols like Bluetooth, ZigBee, Wi-Fi, Ethernet, and mobile communication such as 5G, 4G, and 3G .
- The data link layer uses the physical and medium access control (MAC) sublayers to handle the physical characteristics and the access methods of the communication medium, such as radio frequency, infrared, or optical.
- The network layer is responsible for providing end-to-end data delivery across multiple hops in the network, such as from a sensor to a cloud server or from an actuator to a controller.
- The network layer consists of protocols like RPL, CORPL, CARP, and 6LoWPAN .
- The network layer uses the routing and encapsulation sublayers to handle the path selection and the packet formation of the data, such as using IPv6 addresses, headers, and compression techniques.