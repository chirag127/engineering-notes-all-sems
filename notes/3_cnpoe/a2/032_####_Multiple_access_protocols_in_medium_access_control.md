 Here is the content in markdown format on the topic #### Multiple access protocols in medium access control:

#### Multiple access protocols in medium access control

The multiple access protocols in medium access control determine how multiple stations can share the communication medium. The main protocols are:

- **CSMA/CD (Carrier Sense Multiple Access/Collision Detection):** In CSMA/CD, a station senses the medium before transmission to check for absence of other transmissions. If the medium is sensed idle, the station transmits. If collision is detected, the transmission is aborted and a random backoff time is set before attempting to transmit again. This is used in Ethernet.

- **CSMA/CA (Carrier Sense Multiple Access/Collision Avoidance):** In CSMA/CA, a station senses the medium and if idle, it sends a short control packet to reserve the medium before actual transmission. If no other station sends a reservation packet, the transmission happens. This avoids collisions and is used in 802.11 Wi-Fi.

- **Token Passing:** In token passing, a special packet called token is passed around the network and only the station possessing the token can transmit. After transmission, the token is passed to the next station. This is a collision-free protocol used in FDDI and Token Ring networks.

- **Polling:** In polling, a central controller polls each station sequentially. When polled, a station can transmit. This is a collision-free protocol but can suffer from inefficiency if there are more stations. It is used in some wired networks.

Advantages and disadvantages of these protocols can be discussed along with examples and applications. Mnemonics and learning tricks can also be included if they aid in easy remembering of the protocols and concepts. The content can be expanded with more details and diagrams as required for studying from the material.