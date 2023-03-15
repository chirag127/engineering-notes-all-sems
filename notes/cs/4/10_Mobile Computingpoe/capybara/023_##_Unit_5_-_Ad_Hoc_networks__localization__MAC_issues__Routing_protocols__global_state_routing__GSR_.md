## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

Ad Hoc networks are wireless networks that are formed between devices without the need for a central access point. These networks are useful in settings where there is no pre-existing infrastructure, such as disaster relief operations or military missions. 

### Ad Hoc Networks

#### Advantages of Ad Hoc Networks
- Flexibility: Ad hoc networks can be set up quickly and easily in any location without the need for a pre-existing network infrastructure.
- Cost-Effective: Since there is no need for a central access point or other infrastructure, Ad hoc networks can be set up at a lower cost than traditional networks.
- Resilience: Ad hoc networks can continue to operate even if some nodes fail, making them useful in disaster relief operations or military missions.

#### Disadvantages of Ad Hoc Networks
- Security: Since Ad hoc networks are not protected by a central access point, they are more vulnerable to hacking and other security threats.
- Limited Range: The range of Ad hoc networks is limited, making them unsuitable for large-scale operations.
- Interference: Ad hoc networks can be affected by interference from other wireless devices, which can cause disruptions in communication.

#### Mnemonic
An easy way to remember the advantages of Ad hoc networks is the acronym FCR - Flexibility, Cost-Effective, and Resilience.

### Localization

Localization is the process of determining the location of a device within a wireless network. This is useful in settings where the location of a device is important, such as in military operations or emergency response situations.

#### Methods of Localization
- Triangulation: This method involves using the signal strength of multiple access points to determine the location of a device.
- Time of Arrival (TOA): This method involves measuring the time it takes for a signal to travel from a device to an access point to determine the distance between the two.
- Angle of Arrival (AOA): This method involves measuring the angle at which a signal arrives at an access point to determine the location of a device.

### MAC Issues

MAC (Media Access Control) is the protocol used by wireless devices to access the network. MAC issues can arise when there are multiple devices trying to access the network at the same time.

#### Solutions to MAC Issues
- Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA): This protocol involves devices listening to the network to determine if it is available before transmitting data.
- Time Division Multiple Access (TDMA): This protocol involves dividing the available time on the network into time slots, with each device being assigned a specific time slot for transmitting data.

### Routing Protocols

Routing protocols are used to determine the best path for data to travel between devices in a network.

#### Types of Routing Protocols
- Proactive Routing Protocols: These protocols maintain a constant map of the network and use that map to determine the best path for data to travel.
- Reactive Routing Protocols: These protocols only determine the best path for data when it is needed, which can result in faster routing times but also increased network overhead.
- Hybrid Routing Protocols: These protocols combine the best features of proactive and reactive routing protocols.

#### Mnemonic
A helpful mnemonic for remembering the types of routing protocols is PRRH - Proactive, Reactive, and Hybrid.

### Global State Routing (GSR)

Global State Routing (GSR) is a routing protocol that uses a global state database to determine the best path for data to travel between devices.

#### Advantages of GSR
- Scalability: GSR can scale to support large networks without compromising performance.
- Flexibility: GSR can be used in a variety of network topologies.
- Reliability: GSR is highly reliable, with multiple backup paths available in case of network failures.

#### Disadvantages of GSR
- Complexity: GSR can be complex to set up and maintain, requiring specialized knowledge and skills.
- High Overhead: GSR can generate a lot of network overhead, which can impact performance in some settings.