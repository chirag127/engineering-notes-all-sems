 Here is the content in markdown format for the topic #### Switching techniques and multiplexing in Computer Networks:

#### Switching techniques and multiplexing in Computer Networks

Switching techniques are used to connect multiple devices in a network and transmit data between them efficiently. Some key switching techniques used in computer networks are:

- Circuit switching: A dedicated end-to-end path is established between the source and destination devices before the actual data transmission. The resources are reserved for the connection for the entire duration even if there is no data transmission. Examples: Old telephone networks.
- Message switching: Data is transmitted in discrete messages which are routed independently based on the address information. The route of different messages can be different. Examples: SMS, earlier e-mail networks.
- Packet switching: Data is split into packets which are routed independently to the destination. The packets may take different routes to reach the destination. Examples: Internet, Ethernet.

Multiplexing is a technique by which multiple data streams are combined into one signal over a shared medium. Some key types of multiplexing are:

- Frequency division multiplexing (FDM): different data streams are allocated different frequency bands to transmit over the shared medium.
- Time division multiplexing (TDM): different data streams are allocated different time slots to transmit over the shared medium.
- Wavelength division multiplexing (WDM): different data streams are allocated different wavelengths of light to transmit over the shared optical fiber medium.

Mnemonics:
- CIRCUIT: C - Circuit, I - switching
- MESSAGE: M - Message, E - switching
- PACKET: P - Packet, K - switching

Advantages of packet switching over circuit switching:
- Efficient use of resources as resources are allocated on demand
- Robust as packets can take different routes to reach the destination
- Scalable as more data streams can be accommodated easily

Disadvantages of packet switching:
- Packets can take varying time to reach destination resulting in out of order delivery/jitter
- Overhead for adding address information to packets
- Possibility of packet loss/corruption

[Include diagrams/examples/codes/tables/applications as needed]