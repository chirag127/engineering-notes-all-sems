Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model. These protocols allow a number of nodes or users to access a shared network channel  .

There are different types of multiple access protocols, such as random access, controlled access, and channelization protocols. Each type has its own advantages and disadvantages, depending on the network scenario and requirements.

#### Multiple access protocols in medium access control

```
+----------------------+----------------------+----------------------+
| Random Access        | Controlled Access    | Channelization       |
+----------------------+----------------------+----------------------+
| ALOHA                | Reservation          | Frequency Division   |
| CSMA                 | Polling              | Multiple Access      |
| CSMA/CA              | Token Passing        | (FDMA)               |
| CSMA/CD              |                      | Time Division        |
|                      |                      | Multiple Access      |
|                      |                      | (TDMA)               |
|                      |                      | Code Division        |
|                      |                      | Multiple Access      |
|                      |                      | (CDMA)               |
|                      |                      | Space Division       |
|                      |                      | Multiple Access      |
|                      |                      | (SDMA)               |
|                      |                      | Orthogonal Frequency |
|                      |                      | Division Multiple    |
|                      |                      | Access (OFDMA)       |
+----------------------+----------------------+----------------------+
```

The diagram above shows some examples of multiple access protocols in each category. The following is a brief description of each protocol:

- ALOHA: A simple protocol that allows any station to transmit data whenever it wants, without sensing the channel. It has a high probability of collisions and low channel utilization.
- CSMA: A protocol that requires the station to sense the channel before transmitting data. If the channel is busy, the station waits until it becomes idle. It reduces the collisions but does not eliminate them.
- CSMA/CA: A protocol that uses a collision avoidance mechanism, such as sending a short request-to-send (RTS) frame before transmitting data. The receiver responds with a clear-to-send (CTS) frame, and then the data transmission begins. It is used in wireless networks, such as IEEE 802.11.
- CSMA/CD: A protocol that uses a collision detection mechanism, such as monitoring the voltage level on the channel during transmission. If a collision is detected, the station stops transmitting and waits for a random time before retrying. It is used in wired networks, such as Ethernet.
- Reservation: A protocol that requires the station to reserve the channel before transmitting data. The reservation can be done by sending a special frame or by using a separate control channel. It reduces the collisions but introduces some delay.
- Polling: A protocol that uses a master station to control the access of other stations. The master station polls each station in a round-robin fashion and grants them the permission to transmit data. It eliminates the collisions but introduces some overhead and delay.
- Token Passing: A protocol that uses a special frame, called a token, to grant the access to the channel. The token is passed from one station to another in a logical ring or bus topology. The station that has the token can transmit data until it releases the token. It eliminates the collisions but introduces some delay and complexity.
- Frequency Division Multiple Access (FDMA): A protocol that divides the channel into multiple frequency bands and assigns each band to a different station. The stations can transmit data simultaneously without interfering with each other. It requires a high-quality channel and a precise synchronization.
- Time Division Multiple Access (TDMA): A protocol that divides the channel into multiple time slots and assigns each slot to a different station. The stations can transmit data sequentially without interfering with each other. It requires a precise synchronization and a guard time between slots.
- Code Division Multiple Access (CDMA): A protocol that uses a unique code to modulate the data of each station. The stations can transmit data simultaneously on the same frequency band without interfering with each other. The receiver can recover the data by using the same code as the sender. It requires a complex encoding and decoding process and a power control mechanism.
- Space Division Multiple Access (SDMA): A protocol that uses multiple antennas or beams to create multiple spatial channels and assigns each channel to a different station. The stations can transmit data simultaneously without interfering