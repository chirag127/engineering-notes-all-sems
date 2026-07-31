### Multiple Access Protocols

Multiple Access Protocols are used to share a single communication channel among multiple nodes in a network. These protocols enable efficient and fair access to the channel, ensuring that all nodes get equal opportunities to transmit data. In this unit, we will learn about various multiple access protocols used in Local Area Networks (LANs).

#### 1. Carrier Sense Multiple Access (CSMA)

CSMA protocol is used in LANs such as Ethernet to control access to the shared medium. In this protocol, before transmitting data, a node listens to the channel to check if it is busy. If the channel is idle, the node transmits the data. If the channel is busy, the node waits for a random amount of time before retrying.

#### 2. Carrier Sense Multiple Access with Collision Detection (CSMA/CD)

CSMA/CD is similar to CSMA, but it adds collision detection capability. In this protocol, a node listens to the channel while transmitting data. If the node detects a collision, it stops transmitting and waits for a random amount of time before retrying.

#### 3. Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA)

CSMA/CA is used in wireless LANs to mitigate collisions that can occur due to hidden nodes. In this protocol, a node sends a request to transmit before actually transmitting data. If the channel is idle, the node transmits the data. If the channel is busy, the node waits for a random amount of time before retrying.

#### 4. Token Passing

Token Passing protocol is used in LANs such as Token Ring to control access to the shared medium. In this protocol, a token is passed around the network, giving a node the right to transmit data. Once the node has transmitted the data, it releases the token, allowing other nodes to transmit data.

#### 5. Polling

Polling protocol is used in LANs such as FDDI to control access to the shared medium. In this protocol, a central node called the 'master' polls other nodes to check if they have data to transmit. If a node has data, it transmits the data. If a node does not have data, it responds with a 'no data' message.

Multiple Access Protocols are essential for the efficient and fair sharing of a communication channel in a network. Each protocol has its advantages and disadvantages and is suitable for specific applications. Understanding these protocols is crucial for designing and implementing a reliable and efficient network.