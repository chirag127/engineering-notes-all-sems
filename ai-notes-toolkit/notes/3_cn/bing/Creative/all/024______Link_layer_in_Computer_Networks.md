#### Link layer in Computer Networks

- The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet.
- The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to.
- The link layer is responsible for transferring data between nodes on a network segment across the physical layer.
- The link layer may also provide the means to detect and possibly correct errors that can occur in the physical layer.
- The link layer is concerned with local delivery of frames between nodes on the same level of the network.
- The link layer is also known as the data link layer or layer 2 in the OSI model of computer networking .
- The link layer can be divided into two sublayers: the logical link control (LLC) sublayer and the media access control (MAC) sublayer .
- The LLC sublayer provides services such as flow control, error control, and multiplexing to the upper layers.
- The MAC sublayer deals with the access to the shared medium, such as Ethernet, Wi-Fi, or Bluetooth.
- The MAC sublayer encapsulates the source and destination's MAC address or physical address in the frame header.
- The MAC address is a unique identifier for each device on a network, usually assigned by the manufacturer.
- The MAC address is 48 bits long and written in hexadecimal notation, such as 00:0A:95:9D:68:16.
- A mnemonic to remember the MAC address format is: **M**y **A**unt **C**ooks **A**pple **P**ie **S**ixteen **T**imes.
- The MAC sublayer also performs frame delimiting, which is the process of identifying the start and end of a frame on the medium.
- The MAC sublayer uses special bits or patterns to mark the boundaries of a frame, such as the preamble and the start frame delimiter (SFD) in Ethernet.
- A frame is a unit of data at the link layer, which consists of a header, a payload, and a trailer.
- The header contains information such as the source and destination MAC addresses, the frame type, and the frame length.
- The payload contains the data from the upper layers, such as an IP packet or an ARP request.
- The trailer contains a checksum or a cyclic redundancy check (CRC) to detect errors in the frame.
- A frame can be represented as follows:

```
+----------------+----------------+----------------+----------------+
| Preamble | SFD | Destination MAC address | Source MAC address |
+----------------+----------------+----------------+----------------+
| Frame type | Frame length | Payload | CRC |
+----------------+----------------+----------------+----------------+
```

- The link layer performs several functions, such as framing, addressing, error control, flow control, and media access control.
- Framing is the process of dividing the data stream into frames and adding the header and trailer to each frame.
- Addressing is the process of identifying the source and destination nodes on the network using their MAC addresses.
- Error control is the process of detecting and correcting errors that can occur in the transmission of frames.
- Flow control is the process of regulating the rate of data transmission between the sender and the receiver to avoid congestion or buffer overflow.
- Media access control is the process of coordinating the access to the shared medium among multiple nodes.
- The link layer can use different protocols and standards to perform its functions, depending on the type of network and medium.
- Some examples of link layer protocols and standards are Ethernet, Wi-Fi, Bluetooth, PPP, HDLC, and ATM.
- Ethernet is the most widely used link layer protocol for wired networks, such as LANs.
- Wi-Fi is the most widely used link layer protocol for wireless networks, such as WLANs.
- Bluetooth is a link layer protocol for short-range wireless communication, such as personal area networks (PANs).
- PPP is a link layer protocol for point-to-point communication, such as dial-up or DSL connections.
- HDLC is a link layer protocol for synchronous serial communication, such as leased lines or IS