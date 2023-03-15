## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

The link layer is the lowest layer in the OSI model of computer networking. It is responsible for the transmission of data between two directly connected nodes. The link layer is responsible for the following tasks:

1. Framing: The link layer takes the packets from the network layer and encapsulates them into frames. Each frame contains a header, payload, and trailer. The header contains the source and destination addresses, while the trailer contains error detection and correction information.

2. Error detection and correction: The link layer is responsible for detecting and correcting errors that may occur during transmission. This is done using techniques such as parity checking, checksums, and cyclic redundancy checks (CRC).

3. Flow control: The link layer is responsible for regulating the flow of data between two nodes. This is done to prevent the receiver from being overwhelmed by the sender.

4. Medium access control: The link layer is responsible for controlling access to the shared communication medium. This is done using techniques such as time division multiple access (TDMA), frequency division multiple access (FDMA), and carrier sense multiple access with collision detection (CSMA/CD).

Local Area Networks (LANs) are computer networks that are designed to operate over a small geographical area, such as a home, office, or campus. LANs are typically used to connect computers and other devices within a single building or group of buildings.

The most common type of LAN is the Ethernet LAN. Ethernet LANs use the CSMA/CD protocol for medium access control. In an Ethernet LAN, all devices are connected to a shared communication medium, such as a coaxial cable or twisted pair cable. When a device wants to transmit data, it listens to the medium to see if it is free. If the medium is free, the device transmits its data. If the medium is busy, the device waits for a random amount of time before trying again.

Mnemonics and learning tricks:
- **F**raming, **E**rror detection and correction, **F**low control, **M**edium access control: **F**our **E**ssential **F**unctions of the **M**edium access control sublayer.
- **C**arrier **S**ense **M**ultiple **A**ccess with **C**ollision **D**etection: **C**ats **S**ee **M**ice **A**nd **C**hase **D**own.