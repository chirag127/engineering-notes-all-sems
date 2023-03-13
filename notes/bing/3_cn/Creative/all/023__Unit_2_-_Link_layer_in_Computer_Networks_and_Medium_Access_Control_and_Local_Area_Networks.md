## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

- The link layer, or layer 2, is the second layer of the OSI model of computer networking. It is responsible for transferring data between nodes on a network segment across the physical layer.
- The link layer is divided into two sublayers: the data link layer and the medium access control (MAC) layer.
- The data link layer provides the functional and procedural means to transfer data between network entities and may also provide error detection and correction. It encapsulates the network layer packets into frames and adds a header and a trailer to each frame.
- The MAC layer is responsible for controlling the access of multiple nodes to a shared medium, such as a wireless channel or a bus network. It coordinates the transmission and reception of frames and avoids or resolves collisions.
- Some of the functions of the link layer are:
  - Framing: dividing the data stream into frames of fixed or variable size.
  - Addressing: adding source and destination addresses to the frames to identify the nodes on the link.
  - Flow control: regulating the rate of data transmission between the sender and the receiver to avoid buffer overflow.
  - Error control: detecting and correcting errors in the frames using techniques such as parity check, checksum, or cyclic redundancy check (CRC).
  - Medium access control: determining when and how a node can access the shared medium using protocols such as ALOHA, CSMA/CD, CSMA/CA, or TDMA.
  - Link management: establishing, maintaining, and terminating the link between the nodes using protocols such as HDLC, PPP, or SLIP.

- Some of the examples of link layer protocols are:
  - Ethernet: a widely used wired LAN technology that uses CSMA/CD for medium access control and supports various data rates and frame formats.
  - Wi-Fi: a wireless LAN technology that uses CSMA/CA for medium access control and supports various standards such as 802.11a/b/g/n/ac/ax.
  - Bluetooth: a wireless personal area network (PAN) technology that uses frequency hopping spread spectrum (FHSS) for medium access control and supports various profiles such as headset, keyboard, or mouse.
  - ATM: a high-speed switched network technology that uses fixed-size cells of 53 bytes and supports various quality of service (QoS) classes and traffic types.

- Some of the mnemonics and learning tricks for the link layer are:
  - To remember the functions of the link layer, use the acronym FAMEL: Framing, Addressing, Medium access control, Error control, Link management.
  - To remember the types of errors that can occur in the link layer, use the acronym BUD: Bit errors, Undetected errors, Dropped frames.
  - To remember the types of medium access control protocols, use the acronym CAT: Contention-based, Allocation-based, Token-based.