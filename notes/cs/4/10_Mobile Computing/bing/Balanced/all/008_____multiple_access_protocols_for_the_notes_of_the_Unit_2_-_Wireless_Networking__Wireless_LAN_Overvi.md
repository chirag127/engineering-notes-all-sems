# Multiple Access Protocols

- Multiple access protocols are used to coordinate the access of multiple nodes or users to a shared network channel, such as a wireless LAN or a satellite network.
- Multiple access protocols can be classified into three categories: random access, controlled access, and channelization.
- Random access protocols allow nodes to transmit data whenever they have data to send, without any coordination with other nodes. However, this may result in collisions, which degrade the network performance and waste the channel bandwidth.
- Controlled access protocols require nodes to obtain permission from a central controller or from other nodes before transmitting data. This reduces the probability of collisions, but introduces some delay and overhead in the network.
- Channelization protocols divide the channel into smaller subchannels, and assign each subchannel to a node or a group of nodes. This avoids collisions, but may not utilize the channel efficiently if some subchannels are idle or underutilized.

## Random Access Protocols

- Some common random access protocols that may be used in wireless networks are:

  - ALOHA: It is a simple protocol that allows nodes to transmit data whenever they have data to send, without any sensing or reservation. It is prone to collisions, especially when the network load is high. There are two variants of ALOHA: pure ALOHA and slotted ALOHA. Pure ALOHA does not have any synchronization among nodes, while slotted ALOHA divides the time into equal slots and requires nodes to transmit only at the beginning of a slot. Slotted ALOHA has a higher throughput than pure ALOHA, but still suffers from collisions .
  - CSMA: It stands for Carrier Sense Multiple Access. It is a protocol that requires nodes to sense the channel before transmitting data. If the channel is busy, the node defers its transmission until the channel becomes idle. This reduces the chance of collisions, but does not eliminate them completely. There are different variants of CSMA, such as 1-persistent CSMA, non-persistent CSMA, and p-persistent CSMA, which differ in how nodes choose their backoff time after sensing a busy channel .
  - CSMA/CA: It stands for Carrier Sense Multiple Access with Collision Avoidance. It is a protocol that enhances CSMA by using a handshake mechanism to reserve the channel before transmitting data. The sender node first sends a Request to Send (RTS) frame to the receiver node, and waits for a Clear to Send (CTS) frame from the receiver. If the sender receives the CTS, it proceeds to transmit the data frame, otherwise it backs off and retries later. This protocol avoids collisions by preventing other nodes from transmitting during the RTS-CTS-data exchange. It is used in IEEE 802.11 / WiFi networks, potentially using a distributed coordination function .

## Controlled Access Protocols

- Some common controlled access protocols that may be used in wireless networks are:

  - Reservation ALOHA (R-ALOHA): It is a protocol that combines ALOHA and reservation techniques. It divides the time into frames, and each frame consists of two subframes: a reservation subframe and a data subframe. Nodes use the reservation subframe to send reservation requests to a central controller, which then allocates the data subframe slots to the nodes based on their requests. This protocol reduces collisions and improves the throughput of ALOHA, but introduces some delay and overhead in the network.
  - Mobile Slotted Aloha (MS-ALOHA): It is a protocol that adapts slotted ALOHA to the dynamic nature of mobile networks. It allows nodes to change their slots according to their mobility and traffic patterns. Nodes use a reservation slot to inform the central controller about their slot preferences, and the controller assigns the slots to the nodes based on their requests and the availability of the slots. This protocol improves the performance and flexibility of slotted ALOHA, but requires some synchronization and coordination among nodes and the controller.
  - Polling: It is a protocol that uses a central controller to poll each node in a predefined order and grant them the channel access. The controller maintains a list of active nodes and cycles through them, asking each node if it has data to send. If the node has data, it transmits the data to the controller or to the destination node, otherwise it waits for the next poll. This protocol avoids collisions and ensures fair access to the channel, but introduces some delay and overhead in the network.

## Channelization