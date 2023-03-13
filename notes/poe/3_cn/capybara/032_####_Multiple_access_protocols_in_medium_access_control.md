#### Multiple access protocols in medium access control

In computer networking, multiple access protocols are used to allow multiple devices to share a common communication channel. Medium access control (MAC) is a sublayer of the data link layer that implements multiple access protocols. In this section, we will discuss some of the multiple access protocols used in MAC.

1. **Carrier Sense Multiple Access (CSMA)**: This protocol is used in Ethernet. In CSMA, a device listens to the communication channel before transmitting data. If the channel is busy, the device waits for a random amount of time before trying again. CSMA is simple and easy to implement, but it may cause collisions when multiple devices try to transmit at the same time.

2. **Carrier Sense Multiple Access with Collision Detection (CSMA/CD)**: This protocol is also used in Ethernet. In CSMA/CD, a device listens to the communication channel before transmitting data. If the channel is busy, the device waits for a random amount of time before trying again. If a collision occurs, the devices stop transmitting and wait for a random amount of time before trying again. CSMA/CD reduces the likelihood of collisions, but it may still occur in heavy traffic situations.

3. **Token Passing**: This protocol is used in Token Ring networks. In token passing, a token is passed around the network, and only the device with the token can transmit data. After transmitting data, the device passes the token to the next device in the network. Token passing guarantees that only one device can transmit at a time, but it may cause delays if a device holds onto the token for a long time.

4. **Polling**: This protocol is used in some legacy networks. In polling, a central device called a master polls each device in the network and asks if it has data to transmit. The master then grants permission to the device to transmit. Polling ensures that each device has a chance to transmit, but it may cause delays if the master has to wait for a device to transmit.

Mnemonics and learning tricks:

Unfortunately, there are no easy mnemonics or learning tricks for these multiple access protocols. The best way to remember them is to understand their characteristics and differences. Practicing with examples and scenarios can also help in understanding how these protocols work in real-world situations.

Advantages and disadvantages:

- CSMA is simple and easy to implement, but it may cause collisions.
- CSMA/CD reduces the likelihood of collisions, but collisions may still occur in heavy traffic situations.
- Token passing guarantees that only one device can transmit at a time, but it may cause delays if a device holds onto the token for a long time.
- Polling ensures that each device has a chance to transmit, but it may cause delays if the master has to wait for a device to transmit.

Examples and applications:

- CSMA and CSMA/CD are used in Ethernet networks.
- Token passing is used in Token Ring networks.
- Polling is used in some legacy networks.

In conclusion, understanding the multiple access protocols used in MAC is essential for designing and maintaining computer networks. Practicing with examples and scenarios can help in understanding how these protocols work in real-world situations.