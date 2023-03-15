# Unit 3 - Link layer

The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet. The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to. The link layer is also known as the data link layer or layer 2 in the OSI model of computer networking.

Some of the functions of the link layer are:

- Framing: The link layer receives packets from the network layer and divides them into small frames, then sends each frame bit-by-bit to the physical layer.
- Error control: The link layer detects and corrects errors that may occur in the physical layer. The link layer may use techniques such as checksums, cyclic redundancy checks, or forward error correction to ensure the reliability of the transmission.
- Flow control: The link layer regulates the data flow between the sender and the receiver to avoid congestion and buffer overflow. The link layer may use techniques such as stop-and-wait, sliding window, or backpressure to control the flow of frames.
- Media access control: The link layer coordinates the access of multiple devices to a shared medium, such as a wireless channel or a bus network. The link layer may use techniques such as contention-based, reservation-based, or polling-based protocols to avoid collisions and ensure fair allocation of the medium.
- Addressing: The link layer assigns unique identifiers to each device on a link, such as MAC addresses or link-local addresses. The link layer may use techniques such as ARP, RARP, or NDP to resolve the mapping between link-layer addresses and network-layer addresses.
- Link management: The link layer establishes, maintains, and terminates the links between devices on a network. The link layer may use techniques such as PPP, HDLC, or L2TP to negotiate the parameters and protocols of the link.

The link layer is responsible for the delivery of frames between adjacent nodes on a network. The link layer may use different protocols and standards depending on the type and characteristics of the link, such as Ethernet, Wi-Fi, Bluetooth, or ATM. The link layer may also provide services such as bridging, switching, or routing to interconnect different links and networks.