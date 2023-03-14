## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

- The link layer is the lowest layer of the Internet Protocol Suite (TCP/IP) that is responsible for transferring data between nodes on a network segment across the physical layer.
- The link layer is divided into two sublayers: the medium access control (MAC) sublayer and the logical link control (LLC) sublayer.
- The MAC sublayer controls the hardware that interacts with the transmission medium, such as wired, optical, or wireless media. It also provides addressing and channel access control mechanisms for concurrent transmission.
- The LLC sublayer provides flow control and multiplexing for the logical link, such as EtherType, VLAN tag, etc. It also provides error detection and correction for some link layer protocols.
- The link layer protocols are specific to the physical layer standards, such as Ethernet, WiFi, ATM, Frame Relay, etc. Each protocol has its own frame format, addressing scheme, and error control method.
- The link layer frames, also called protocol data units (PDUs), do not cross the boundaries of a local area network (LAN). They are encapsulated and decapsulated by the network layer protocols, such as IP, for inter-network routing and global addressing.
- The link layer is analogous to a neighborhood traffic cop; it arbitrates between parties contending for access to a medium, without concern for their ultimate destination. It also detects and recovers from collisions, and may provide mechanisms to reduce or prevent them.
- The link layer is also involved in cellular networks, such as UMTS and LTE, where it is divided into multiple protocol layers, such as the Packet Data Convergence Protocol (PDCP), the Radio Link Control (RLC) protocol, and the MAC protocol.

### Mnemonics and learning tricks

- To remember the functions of the link layer, use the acronym **FAME**: **F**rame, **A**ddress, **M**edia, **E**rror.
- To remember the sublayers of the link layer, use the acronym **MAC and Cheese**: **M**edium **A**ccess **C**ontrol and **C**ontrol, **H**ardware, **E**rror, **E**ncapsulation, **S**ervice.
- To remember the difference between MAC and LLC, use the phrase **MAC is the hardware, LLC is the software**. MAC deals with the physical aspects of the transmission medium, while LLC deals with the logical aspects of the data link.
- To remember some of the link layer protocols, use the acronym **E-WAFFLE**: **E**thernet, **W**iFi, **A**TM, **F**rame **R**elay, **F**DDI, **L**AN, **E**therType.