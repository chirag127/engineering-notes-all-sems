#### Switching techniques and multiplexing in Computer Networks

Switching techniques are methods of connecting multiple devices in a network and transferring data between them. Multiplexing is a technique of combining multiple signals into one signal over a shared medium. Both techniques are used to improve the efficiency and performance of communication networks.

There are three main types of switching techniques:

- **Circuit switching**: In circuit switching, two nodes communicate with each other over a dedicated communication path. The path is established before the data transmission and remains active until the communication is over. The path is reserved exclusively for the two nodes and no other node can use it. Circuit switching is reliable and guarantees a constant bandwidth, but it is inefficient and costly. An example of circuit switching is the traditional telephone network.

- **Message switching**: In message switching, the whole message is treated as a data unit. The message is stored and forwarded by intermediate nodes until it reaches the destination. The message may take different paths and may arrive out of order. There is no dedicated path or reservation of bandwidth. Message switching is flexible and can handle variable-length messages, but it introduces delay and overhead. An example of message switching is email.

- **Packet switching**: The packet switching technique is derived from message switching where the message is broken down into smaller chunks called packets. Each packet has a header that contains the source and destination addresses and other information. The packets are routed independently by intermediate nodes and may take different paths. The packets are reassembled at the destination. There is no dedicated path or reservation of bandwidth. Packet switching is efficient and scalable, but it may cause congestion and loss of packets. An example of packet switching is the internet.

Multiplexing can be done in different ways, depending on the type of signal and the medium. Some common types of multiplexing are:

- **Frequency division multiplexing (FDM)**: In FDM, the frequency spectrum of the medium is divided into several non-overlapping frequency bands. Each signal is modulated by a different carrier frequency and transmitted over a different band. The signals are separated at the receiver by using filters. FDM is suitable for analog signals and can be used in radio, television, and cable networks.

- **Time division multiplexing (TDM)**: In TDM, the time axis of the medium is divided into several time slots. Each signal is assigned a different time slot and transmitted over the medium in a round-robin fashion. The signals are separated at the receiver by using synchronization. TDM is suitable for digital signals and can be used in telephone, cellular, and optical networks.

- **Statistical multiplexing**: Statistical multiplexing is a communication link sharing technique, which is used in packet switching. The shared linking is variable in statistical multiplexing, whereas it is fixed in TDM or FDM. This is a strategic application for maximizing the utilization of bandwidth. This can increase the efficiency of network, as well. Statistical multiplexing is based on the principle of demand and availability. The signals are transmitted over the medium only when they have data to send and when the medium is available. The signals are separated at the receiver by using headers. Statistical multiplexing is suitable for bursty and unpredictable traffic and can be used in internet and wireless networks.

A simple mnemonic to remember the types of switching techniques is:

- Circuit switching: **C**onstant path, **C**onstant bandwidth, **C**ostly
- Message switching: **M**essage as a unit, **M**emory required, **M**ore delay
- Packet switching: **P**acket as a unit, **P**ath varies, **P**erformance better

A simple mnemonic to remember the types of multiplexing is:

- FDM: **F**requency bands, **F**ilters, **F**or analog signals
- TDM: **T**ime slots, **T**iming, **T**or digital signals
- Statistical multiplexing: **S**hared link, **S**tatistics, **S**uitable for packet switching
