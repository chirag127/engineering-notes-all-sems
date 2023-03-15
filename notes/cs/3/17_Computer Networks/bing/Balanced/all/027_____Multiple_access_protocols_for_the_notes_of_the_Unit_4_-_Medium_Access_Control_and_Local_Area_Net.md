# Multiple Access Protocols in Computer Networks

Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model. These protocols allow a number of nodes or users to access a shared network channel. Multiple access protocols can be broadly classified into three categories - random access protocols, controlled access protocols and channelization protocols .

## Random Access Protocols

Random access protocols assign uniform priority to all connected nodes. Any node can send data depending on the state of the medium (idle or busy). There is no fixed time for sending data. Random access protocols have two features:

- Collision: When two or more nodes transmit data at the same time, a collision occurs. Collisions degrade the performance of the network and waste bandwidth.
- Collision Detection and Avoidance: To deal with collisions, random access protocols use collision detection and avoidance mechanisms. Collision detection is the process of identifying when a collision has occurred and informing the nodes to stop transmitting. Collision avoidance is the process of preventing collisions from happening by using some techniques such as sensing the medium before transmitting or using a backoff algorithm.

Some examples of random access protocols are:

- ALOHA: ALOHA is the first random access protocol developed for satellite communication. It has two variants: pure ALOHA and slotted ALOHA. In pure ALOHA, nodes transmit data whenever they have data to send, without checking the medium. In slotted ALOHA, nodes transmit data only at the beginning of a time slot, which reduces the collision probability.
- CSMA (Carrier Sense Multiple Access): CSMA is a random access protocol that uses the technique of sensing the medium before transmitting. Nodes listen to the channel and transmit data only if the channel is idle. If the channel is busy, nodes defer their transmission until the channel becomes idle. CSMA has three variants: 1-persistent CSMA, non-persistent CSMA and p-persistent CSMA.
- CSMA/CD (Carrier Sense Multiple Access with Collision Detection): CSMA/CD is a random access protocol that uses the technique of collision detection. Nodes listen to the channel and transmit data only if the channel is idle. If a collision is detected, nodes stop transmitting and wait for a random amount of time before retrying. CSMA/CD is used in Ethernet networks.
- CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance): CSMA/CA is a random access protocol that uses the technique of collision avoidance. Nodes listen to the channel and transmit data only if the channel is idle. Before transmitting, nodes send a short message called Request to Send (RTS) to the intended receiver. The receiver replies with a short message called Clear to Send (CTS) if the channel is clear. The sender then transmits the data and waits for an acknowledgment from the receiver. CSMA/CA is used in wireless networks.

## Controlled Access Protocols

Controlled access protocols assign different priority to different nodes. The access to the channel is controlled by a central node or a distributed algorithm. Nodes have to request permission to send data and wait for their turn. Controlled access protocols have the advantage of avoiding collisions and ensuring fairness among nodes. Some examples of controlled access protocols are:

- Reservation: Reservation is a controlled access protocol that uses a reservation frame to allocate the channel to the nodes. The reservation frame consists of a number of slots, each corresponding to a node. Nodes send their requests in the slots assigned to them. The node that receives the most requests gets the channel for the next frame.
- Polling: Polling is a controlled access protocol that uses a central node called the poller or the primary station to coordinate the access to the channel. The poller sends a message called a poll to each node in a round-robin fashion, asking if they have data to send. The node that receives the poll can send data or decline. The poller then moves to the next node and repeats the process.
- Token Passing: Token passing is a controlled access protocol that uses a special message called a token to grant the access to the channel. The token circulates among the nodes in a logical ring or a bus topology. The node that has the token can send data or pass the token to the next node. The token ensures that only one node can transmit at a time.

## Channelization Protocols

Channelization protocols divide the channel into smaller subchannels and assign them to different nodes. The subchannels can be based on frequency, time or code. Channelization protocols have the advantage of increasing the channel capacity and reducing the interference