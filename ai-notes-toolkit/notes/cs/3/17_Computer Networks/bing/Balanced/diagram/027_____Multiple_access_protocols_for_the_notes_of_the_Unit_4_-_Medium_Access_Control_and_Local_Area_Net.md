### Multiple access protocols

Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model. These protocols allow a number of nodes or users to access a shared network channel without interference or collision.

#### Categories of multiple access protocols

Multiple access protocols can be broadly classified into three categories :

- **Random access protocols**: Random access protocols assign uniform priority to all connected nodes. Any node can send data whenever it wants, without waiting for a permission or a turn. However, this may result in collisions, where two or more nodes transmit data at the same time on the same channel. To avoid or resolve collisions, random access protocols use techniques such as ALOHA, Carrier Sense Multiple Access (CSMA), CSMA with Collision Detection (CSMA/CD), and CSMA with Collision Avoidance (CSMA/CA).
- **Controlled access protocols**: Controlled access protocols assign different priority levels to different nodes or groups of nodes. A node can send data only when it gets permission or a turn from a central controller or a distributed algorithm. This reduces the chances of collisions, but may introduce some delay or overhead. Examples of controlled access protocols are Reservation, Polling, and Token Passing.
- **Channelization protocols**: Channelization protocols divide the available bandwidth of the shared channel into smaller sub-channels, and assign each sub-channel to a node or a group of nodes. A node can send data only on its assigned sub-channel, without interfering with other nodes. This eliminates collisions, but may waste some bandwidth or require complex synchronization. Examples of channelization protocols are Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA), and Code Division Multiple Access (CDMA).

#### References

: https://www.tutorialspoint.com/multiple-access-protocols-in-computer-networks
: https://www.javatpoint.com/multiple-access-protocols