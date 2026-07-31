 Here is the content in markdown format without any emojis or external links:

### Medium Access Control Protocols for Broadcast Networks

- ALOHA: Pure ALOHA and Slotted ALOHA are the two variations of ALOHA protocol. In Pure ALOHA, nodes transmit whenever they have data to send resulting in collision. In Slotted ALOHA, time is divided into slots and nodes are allowed to transmit only at slot boundaries reducing chances of collision.
- Carrier Sense Multiple Access (CSMA): In CSMA, nodes check the channel for activity (Carrier Sensing) before transmitting. If the channel is sensed busy, nodes wait for a random time before sensing the channel again. This random delay reduces the possibility of collision. CSMA is not efficient for high load conditions.
- CSMA with Collision Avoidance (CSMA/CA): In CSMA/CA, nodes follow a backoff mechanism where the backoff time is increased exponentially after every unsuccessful transmission attempt reducing the collision probability. IEEE 802.11 uses CSMA/CA.
- CSMA with Collision Detection (CSMA/CD): In CSMA/CD, nodes check the channel for activity before transmitting. If a transmission is detected while transmitting, the ongoing transmission is aborted and a random backoff time is waited before trying to transmit again. Ethernet uses CSMA/CD.

The above points cover the key medium access control protocols used for broadcast networks. The protocols aim to enable efficient sharing of the communication channel among the nodes while reducing the collision probability.