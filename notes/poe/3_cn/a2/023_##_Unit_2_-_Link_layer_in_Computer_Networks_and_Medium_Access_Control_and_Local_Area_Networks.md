 Here is the content in markdown format for ## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks:

## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

- The link layer is the lowest layer in the TCP/IP model and handles data transmission between devices on the same local network.
- The main functions of the link layer are:

- Framing: Packaging data into frames that include source and destination address
- Error detection and correction: Detecting and fixing transmission errors using techniques like CRC and ARQ
- Medium access control: Coordinating access to the shared network medium using techniques like CSMA/CD for Ethernet
- Flow control: Adjusting transmission rates to prevent overwhelming receivers
- Congestion control: Managing network congestion

- Popular LAN technologies like Ethernet operate at the link layer. The MAC address is used for addressing at the link layer.
- Error detection uses CRC (Cyclic Redundancy Check) which generates a checksum from the data that is sent along with the data. The receiver calculates the checksum again and compares it to detect errors.
- Error correction uses ARQ (Automatic Repeat reQuest) where the receiver requests retransmission of corrupted data packets.
- Medium access control methods include:

- CSMA/CD: Carrier Sense Multiple Access with Collision Detection used by Ethernet
- Token passing: A token is passed between devices to authorize access to the medium
- Scheduling: Time slots are assigned to devices to transmit data

- Advantages of link layer: Low overhead, simple, handles local errors and congestion
- Disadvantages: Limited range (only local network), less robust error handling than higher layers

- Applications: Local area networks, wireless networks, Internet access networks

- Mnemonics and learning tricks:
CRC - Cyclic Redundancy Chicken detects errors
CSMA/CD - Courteous Station May Access/Collide Detect shares Ethernet
ARQ - Automatic Repeat reQuest corrects errors