## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

The Link layer is the second layer of the OSI model and is responsible for transferring data between adjacent network nodes. In this unit, we will learn about the Link layer and its sublayers, Medium Access Control (MAC), and Local Area Networks (LANs).

### Link Layer

The Link layer is responsible for transferring data between two adjacent devices on the same network. It provides services such as error detection and correction, flow control, and framing. The Link layer is divided into two sublayers: Logical Link Control (LLC) and Media Access Control (MAC).

#### Logical Link Control (LLC)

The LLC sublayer is responsible for managing communication between devices on the same network. It handles error detection and correction, flow control, and framing. The LLC sublayer is implemented in software and is independent of the physical layer.

#### Media Access Control (MAC)

The MAC sublayer is responsible for managing access to the physical medium. It handles the transmission and reception of data packets, as well as collision detection and avoidance. The MAC sublayer is implemented in hardware and is specific to the physical layer.

### Medium Access Control (MAC)

The MAC sublayer is responsible for managing access to the physical medium. There are several methods used for this, including Carrier Sense Multiple Access with Collision Detection (CSMA/CD) and Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA).

#### Carrier Sense Multiple Access with Collision Detection (CSMA/CD)

CSMA/CD is used in Ethernet networks and is a contention-based protocol. Before transmitting data, a device listens to the network to ensure that no other device is transmitting. If there is no traffic, the device transmits its data. If there is traffic, the device waits for a random amount of time and then tries again. If two devices transmit data at the same time, a collision occurs, and both devices stop transmitting and wait for a random amount of time before trying again.

#### Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA)

CSMA/CA is used in wireless networks and is a contention-based protocol. Before transmitting data, a device listens to the wireless channel to ensure that no other device is transmitting. If there is no traffic, the device transmits its data. If there is traffic, the device waits for a random amount of time and then tries again. If two devices transmit data at the same time, a collision is avoided by using a backoff algorithm that ensures that the devices do not transmit at the same time.

### Local Area Networks (LANs)

A LAN is a network that is confined to a small geographic area, such as a building or campus. LANs are used to connect devices such as computers, printers, and servers to each other, and to provide access to the Internet. There are several types of LANs, including Ethernet, Token Ring, and Wireless LANs.

#### Ethernet

Ethernet is the most widely used LAN technology. It uses CSMA/CD for medium access control and can operate at speeds of up to 100 Gbps. Ethernet networks are typically implemented using twisted pair, coaxial, or fiber optic cables.

#### Token Ring

Token Ring is a LAN technology that uses a token-passing protocol for medium access control. Devices take turns transmitting data using a token that is passed from device to device. Token Ring networks are typically implemented using twisted pair or fiber optic cables.

#### Wireless LANs

Wireless LANs use radio waves to transmit data and do not require physical cables. They use CSMA/CA for medium access control and can operate at speeds of up to 802.11ax (Wi-Fi 6) which can go up to 9.6 Gbps. Wireless LANs are typically implemented using access points that provide wireless connectivity to devices.

### Conclusion

In this unit, we learned about the Link layer and its sublayers, the MAC sublayer, and the LLC sublayer. We also learned about the different methods used for medium access control, including CSMA/CD and CSMA/CA, and the types of LANs, including Ethernet, Token Ring, and Wireless LANs. Understanding the Link layer and its protocols is essential for designing and managing computer networks.