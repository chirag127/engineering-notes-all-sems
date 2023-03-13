## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

The link layer is the second layer of the OSI model and is responsible for transmitting data between adjacent network nodes. This layer provides error-free transmission of data frames over a physical medium. The link layer is further divided into two sublayers: the Media Access Control (MAC) sublayer and the Logical Link Control (LLC) sublayer.

### Media Access Control (MAC) sublayer
The MAC sublayer is responsible for controlling the access of multiple devices to a shared communication medium. It provides a mechanism for arbitrating access to the shared medium and preventing collisions between simultaneous transmissions. Some of the key concepts related to the MAC sublayer are:

- Carrier Sense Multiple Access with Collision Detection (CSMA/CD): This is a protocol used to avoid collisions in Ethernet networks. Devices listen to the medium and wait for a period of time before transmitting to ensure that the medium is free.
- Token Passing: This is a protocol used in Token Ring networks where a token is passed around the network to regulate access to the shared medium.
- Addressing: The MAC sublayer assigns a unique MAC address to each device on the network to identify it. MAC addresses are usually assigned by the manufacturer of the network interface card (NIC).

### Logical Link Control (LLC) sublayer
The LLC sublayer provides flow control and error control mechanisms to ensure reliable transmission of data between two nodes. It also provides a mechanism for identifying different network protocols. Some of the key concepts related to the LLC sublayer are:

- Flow Control: This mechanism regulates the flow of data between two nodes to prevent one node from overwhelming the other.
- Error Control: This mechanism detects and corrects errors in the data transmitted between two nodes.
- Protocol Identification: The LLC sublayer identifies and multiplexes different network protocols, allowing them to share the same physical medium.

#### Mnemonic: 
Remember MAC and LLC sublayers by thinking of them as "M" and "L" of "ML". 

### Medium Access Control (MAC) and Local Area Networks (LANs)
Local Area Networks (LANs) are computer networks that cover a small geographic area, typically within a building or campus. Ethernet is the most widely used LAN technology today. Here are some key concepts related to MAC and LANs:

- Ethernet: This is a LAN technology that uses CSMA/CD and operates at speeds of up to 10 Gbps.
- Switches: These are devices used in LANs to connect multiple devices together and forward data between them. Switches use MAC addresses to forward data to the correct destination device.
- VLANs: Virtual LANs are logical groupings of devices on a LAN that are separated from each other for security or administrative purposes.

#### Mnemonic:
Remember Ethernet, Switches, VLANs by thinking of them as "ESV". 

In conclusion, the link layer is an important layer of the OSI model that provides reliable transmission of data between two nodes. The MAC sublayer is responsible for controlling access to the shared medium, while the LLC sublayer provides flow control and error control mechanisms. LANs are a common application of the link layer, and Ethernet is the most widely used LAN technology today.