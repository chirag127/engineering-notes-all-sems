#### Multiple access protocols in medium access control

- Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model  .
- These protocols allow a number of nodes or users to access a shared network channel, such as a wireless channel or a bus network, without interfering with each other or causing collisions  .
- Multiple access protocols can be classified into three main categories: random access, controlled access, and channelization.
  - Random access protocols: In these protocols, all stations have equal priority and can send data depending on the medium's state (idle or busy). There is no fixed time for sending data and no central controller to coordinate the transmissions. Examples of random access protocols are ALOHA, Carrier Sense Multiple Access (CSMA), CSMA with Collision Avoidance (CSMA/CA), and CSMA with Collision Detection (CSMA/CD) .
  - Controlled access protocols: In these protocols, the stations have to compete for the right to access the medium or follow a predefined order. There is a central controller or a distributed algorithm that determines which station can send data at a given time. Examples of controlled access protocols are Reservation, Polling, and Token Passing.
  - Channelization protocols: In these protocols, the medium is divided into smaller sub-channels that can be allocated to different stations. The sub-channels can be based on frequency, time, or code. Examples of channelization protocols are Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA), and Code Division Multiple Access (CDMA).
- The choice of a multiple access protocol depends on several factors, such as the type of network, the traffic characteristics, the reliability requirements, the power consumption, and the cost.
- Some advantages of multiple access protocols are:
  - They enable multiple users to share a common channel efficiently and fairly  .
  - They reduce the overhead and latency of establishing and maintaining connections.
  - They increase the network capacity and throughput.
- Some disadvantages of multiple access protocols are:
  - They may cause collisions, interference, or contention among the stations, which can degrade the performance and reliability of the network .
  - They may require complex hardware and software to implement and coordinate the protocols.
  - They may not be suitable for all types of networks or applications.

- A possible mnemonic to remember the three categories of multiple access protocols is: **RCC** (Random, Controlled, Channelization).
- A possible learning trick to compare the different random access protocols is to use the following table:

| Protocol | Description | Advantages | Disadvantages |
|----------|-------------|------------|---------------|
| ALOHA | Stations send data whenever they have it and retransmit after a random time if a collision occurs | Simple and decentralized | Low efficiency and high collision probability |
| CSMA | Stations sense the medium before sending data and wait if it is busy | Higher efficiency and lower collision probability than ALOHA | Still vulnerable to collisions and hidden terminal problem |
| CSMA/CA | Stations sense the medium and send a short request-to-send (RTS) frame before sending data. They wait for a clear-to-send (CTS) frame from the receiver before sending data | Reduces collisions and hidden terminal problem | Increases overhead and latency |
| CSMA/CD | Stations sense the medium and send data. They monitor the medium during transmission and abort if a collision is detected. They retransmit after a random time | Reduces wastage of bandwidth and latency | Requires fast collision detection and abort mechanism |