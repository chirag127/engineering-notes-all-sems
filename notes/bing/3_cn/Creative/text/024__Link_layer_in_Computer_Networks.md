#### Link layer in Computer Networks

- The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet.
- The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to.
- The link layer is responsible for transferring data between nodes on a network segment across the physical layer.
- The link layer may also provide the means to detect and possibly correct errors that can occur in the physical layer.
- The link layer is concerned with local delivery of frames between nodes on the same level of the network.
- The link layer provides and gives data reliability and provides various tools to establish, maintain, and also release data link connections between network nodes.
- The link layer performs the following functions:
  - Framing: The packet received from the Network layer is known as a frame in the Data link layer. At the sender’s side, the Data link layer encapsulates the packet with a header and a trailer. At the receiver’s side, the Data link layer decapsulates the packet and sends it to the Network layer.
  - Addressing: The data link layer encapsulates the source and destination’s MAC address / physical address in the header of the frame. The MAC address is used to identify the nodes on the same network segment.
  - Error Control: Data link layer detects and corrects the errors that can occur in the transmission of frames. The errors can be detected by using techniques such as parity check, checksum, or cyclic redundancy check (CRC). The errors can be corrected by using techniques such as stop-and-wait ARQ, go-back-N ARQ, or selective repeat ARQ.
  - Flow Control: Data link layer controls the flow of data between the sender and the receiver to avoid congestion and data loss. The flow control can be implemented by using techniques such as stop-and-wait, sliding window, or backpressure.
  - Media Access Control: Data link layer regulates the access of multiple nodes to the shared medium. The media access control can be implemented by using techniques such as contention-based (e.g., CSMA/CD, CSMA/CA) or reservation-based (e.g., token ring, token bus) protocols.