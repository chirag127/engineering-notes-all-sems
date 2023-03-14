#### Link layer in Computer Networks

The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet.  The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to. The link is the physical and logical network component used to interconnect hosts or nodes in the network and a link protocol is a suite of methods and standards that operate only between adjacent network nodes of a network segment. 

The link layer is sometimes described as a combination of the OSI's data link layer (layer 2) and physical layer (layer 1).  The data link layer is the protocol layer that transfers data between nodes on a network segment across the physical layer.  The data link layer provides the functional and procedural means to transfer data between network entities and may also provide the means to detect and possibly correct errors that can occur in the physical layer. 

The link layer is concerned with local delivery of frames between nodes on the same level of the network. Data-link frames, as these protocol data units are called, do not cross the boundaries of a local area network. Inter-network routing and global addressing are higher-layer functions, allowing data-link protocols to focus on local delivery, addressing, and media arbitration. 

Some of the functions and services of the link layer are:

- Framing: The link layer divides the stream of bits received from the network layer into manageable data units called frames.
- Physical addressing: The link layer adds a header to the frame to define the sender and/or receiver of the frame. If the frames are to be distributed to different systems on the network, this layer adds a header to the frame to define the sender and/or receiver of the frame.
- Flow control: The link layer ensures that the sender does not overwhelm the receiver by sending too many frames at once.
- Error control: The link layer detects and may correct errors that can occur in the transmission of frames. The link layer uses techniques such as checksums, cyclic redundancy checks (CRCs), and acknowledgments to ensure reliable data transmission.
- Media access control: The link layer coordinates the access of multiple devices to a shared communication medium. The link layer uses techniques such as ALOHA, carrier sense multiple access (CSMA), CSMA with collision detection (CSMA/CD), and CSMA with collision avoidance (CSMA/CA) to avoid or resolve conflicts among competing devices. 

Some examples of link layer protocols are Ethernet, the IEEE 802.11 WiFi protocols, ATM and Frame Relay.   In the Internet Protocol Suite (TCP/IP), the link layer functionality is contained within the link layer, the lowest layer of the descriptive model, which is assumed to be independent of physical infrastructure.