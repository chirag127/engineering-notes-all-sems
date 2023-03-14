#### Multiple access protocols in medium access control

- Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model .
- These protocols allow a number of nodes or users to access a shared network channel, such as a wired, optical or wireless transmission medium  .
- The main challenge of multiple access protocols is to coordinate the access of multiple nodes to the shared channel, while avoiding or minimizing collisions, interference, and wastage of bandwidth  .
- There are different types of multiple access protocols, depending on the channel access control mechanism they use. Some of the common types are  :

  - Random access protocols: In these protocols, each node can transmit data at any time, without sensing or coordinating with other nodes. However, if two or more nodes transmit data simultaneously, a collision occurs and the data is corrupted. To resolve collisions, random access protocols use techniques such as ALOHA, Carrier Sense Multiple Access (CSMA), CSMA with Collision Detection (CSMA/CD), and CSMA with Collision Avoidance (CSMA/CA)  .
  - Controlled access protocols: In these protocols, each node must obtain permission or a token from a central controller or a previous node before transmitting data. This ensures that only one node can access the channel at a time, and collisions are avoided. However, these protocols introduce some delay and overhead in the channel access. Some examples of controlled access protocols are Reservation, Polling, and Token Passing  .
  - Channelization protocols: In these protocols, the channel is divided into smaller sub-channels, and each node is assigned a sub-channel for transmission. The sub-channels can be based on time, frequency, code, or space. This allows multiple nodes to transmit data simultaneously, without interfering with each other. However, these protocols require synchronization and coordination among the nodes and the sub-channels. Some examples of channelization protocols are Time Division Multiple Access (TDMA), Frequency Division Multiple Access (FDMA), Code Division Multiple Access (CDMA), and Orthogonal Frequency Division Multiple Access (OFDMA)  .

- Multiple access protocols are essential for the efficient and fair utilization of the shared network channel, and they have various applications in different types of networks, such as wireless LANs, cellular networks, satellite networks, and broadcast networks  .

: https://www.javatpoint.com/multiple-access-protocols
: https://en.wikipedia.org/wiki/Medium_access_control
: https://www.tutorialspoint.com/multiple-access-protocols-in-computer-networks
: https://byjus.com/gate/multiple-access-protocols-notes/