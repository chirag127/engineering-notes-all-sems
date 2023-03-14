### MAC Protocol Survey for the Notes of the Unit 4 - Network & Communication Aspects in IoT in the Subject of Internet of Things

In the world of IoT, communication between devices plays a crucial role. The Medium Access Control (MAC) protocol is responsible for managing how devices share the communication medium to transmit their data. In this section, we will discuss the various MAC protocols used in IoT and their advantages and disadvantages.

#### 1. CSMA/CD
- Carrier Sense Multiple Access/Collision Detection (CSMA/CD) is a protocol used in Ethernet networks.
- In this protocol, each device listens to the communication medium before transmitting data. If the medium is busy, the device waits for a random amount of time before trying again.
- If two devices transmit data at the same time, a collision occurs, and both devices wait for a random amount of time before trying again.
- Advantages: Simple and widely used.
- Disadvantages: Inefficient in high traffic networks and not suitable for wireless networks.

#### 2. CSMA/CA
- Carrier Sense Multiple Access/Collision Avoidance (CSMA/CA) is a protocol used in wireless networks.
- In this protocol, each device sends a request to transmit before actually transmitting data. The request includes the estimated time required to transmit data, and if the medium is free for that duration, the data is transmitted.
- Advantages: Suitable for wireless networks and reduces collisions.
- Disadvantages: Reduced efficiency due to the overhead of sending requests before transmitting data.

#### 3. TDMA
- Time Division Multiple Access (TDMA) is a protocol used in networks with a fixed number of devices.
- In this protocol, each device is assigned a specific time slot to transmit data, and the medium is divided into time slots.
- Advantages: Suitable for networks with a fixed number of devices and provides guaranteed time slots for each device.
- Disadvantages: Inefficient in networks with varying traffic and not suitable for networks with a large number of devices.

#### 4. FDMA
- Frequency Division Multiple Access (FDMA) is a protocol used in networks where each device is assigned a specific frequency band.
- In this protocol, each device is assigned a specific frequency band to transmit data, and the medium is divided into frequency bands.
- Advantages: Suitable for networks with a fixed number of devices and reduces collisions.
- Disadvantages: Inefficient in networks with varying traffic and not suitable for networks with a large number of devices.

#### 5. CDMA
- Code Division Multiple Access (CDMA) is a protocol used in networks where multiple devices can transmit data simultaneously.
- In this protocol, each device is assigned a unique code to transmit data, and the codes are used to distinguish between different devices.
- Advantages: Suitable for networks with a large number of devices and allows for simultaneous transmission.
- Disadvantages: Requires complex hardware and is susceptible to interference.

#### Mnemonic
Remember the order of the MAC protocols as "CSMA/CD, CSMA/CA, TDMA, FDMA, CDMA" using the phrase "Cats Can Totally Fetch Cool Dogs."

In conclusion, choosing the appropriate MAC protocol depends on the nature of the IoT network and its requirements. Each protocol has its advantages and disadvantages, and it's essential to choose the one that provides the best performance for the specific application.