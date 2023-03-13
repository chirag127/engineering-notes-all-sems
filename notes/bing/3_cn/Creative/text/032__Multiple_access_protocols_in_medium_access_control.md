#### Multiple access protocols in medium access control

Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model  . These protocols allow a number of nodes or users to access a shared network channel.

Some of the design criteria for multiple access protocols are:

- Efficiency: The protocol should maximize the utilization of the channel and minimize the overhead and delay.
- Fairness: The protocol should allocate the channel fairly among the competing nodes or users and avoid starvation or domination.
- Robustness: The protocol should be able to handle different traffic patterns and network conditions and adapt to changes in the network topology or size.
- Simplicity: The protocol should be easy to implement and maintain and have low cost and complexity.

Multiple access protocols can be classified into three main categories :

- Random access protocols: In these protocols, all stations have equal priority and can send data depending on the medium's state (idle or busy). There is no fixed time for sending data and collisions may occur. Examples of random access protocols are ALOHA, Carrier Sense Multiple Access (CSMA), CSMA with Collision Avoidance (CSMA/CA) and CSMA with Collision Detection (CSMA/CD).
- Controlled access protocols: In these protocols, a station needs to obtain permission from a central authority or follow a predefined order before sending data. There is a fixed time for sending data and collisions are avoided. Examples of controlled access protocols are Reservation, Polling and Token Passing.
- Channelization protocols: In these protocols, the channel is divided into smaller sub-channels that are assigned to different stations or users. There is no contention for the channel and collisions are avoided. Examples of channelization protocols are Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA) and Code Division Multiple Access (CDMA).