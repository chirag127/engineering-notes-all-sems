#### Multiple access protocols in medium access control

- Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model  .
- These protocols allow a number of nodes or users to access a shared network channel, such as a wireless channel or a bus network, without interfering with each other or causing collisions  .
- Multiple access protocols can be classified into three main categories: random access, controlled access, and channelization.
  - Random access protocols: In these protocols, all stations have equal priority and can send data depending on the medium's state (idle or busy). There is no fixed time for sending data and no central controller to coordinate the transmissions. Examples of random access protocols are ALOHA, Carrier Sense Multiple Access (CSMA), CSMA with Collision Avoidance (CSMA/CA), and CSMA with Collision Detection (CSMA/CD) .
  - Controlled access protocols: In these protocols, there is a central controller or a predefined rule that determines which station can access the channel at a given time. The stations have to request permission or wait for their turn to send data. Examples of controlled access protocols are Reservation, Polling, and Token Passing.
  - Channelization protocols: In these protocols, the channel is divided into smaller subchannels or time slots that are assigned to different stations. The stations can only send data in their assigned subchannels or time slots, and there is no contention or collision among them. Examples of channelization protocols are Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA), and Code Division Multiple Access (CDMA).

- The choice of a multiple access protocol depends on various factors, such as the type of network, the traffic characteristics, the channel conditions, the performance requirements, and the cost and complexity of implementation.
- Some advantages of multiple access protocols are:
  - They enable efficient and fair use of the shared channel by multiple stations  .
  - They reduce the delay and overhead of data transmission by avoiding or minimizing collisions and retransmissions .
  - They adapt to the dynamic and unpredictable nature of network traffic and channel conditions by using feedback or sensing mechanisms .
- Some disadvantages of multiple access protocols are:
  - They introduce additional complexity and overhead in the MAC sublayer, such as framing, error control, synchronization, and coordination .
  - They may not guarantee the quality of service (QoS) or the fairness of access for all stations, especially in high traffic or noisy scenarios .
  - They may suffer from performance degradation or instability due to channel errors, hidden terminals, exposed terminals, or capture effects .

- A possible mnemonic to remember the three categories of multiple access protocols is: **RCC** (Random, Controlled, Channelization). A possible learning trick to remember the examples of each category is: **APCT** (ALOHA, Polling, CDMA, Token Passing). The first letter of each example corresponds to the first letter of the category it belongs to.