# Quality of Service

Quality of Service (QoS) refers to the ability of a network to provide improved service to certain network traffic. This is achieved by providing dedicated bandwidth, controlled jitter and latency, and improved loss characteristics. QoS is particularly important for the transport of traffic with special requirements, such as real-time audio and video.

The Transport Layer is responsible for providing end-to-end communication services for applications. It provides services such as connection-oriented data stream support, reliability, flow control, and multiplexing. The Transport Layer can also provide QoS support by using different transport protocols that have different QoS characteristics.

Some of the key QoS parameters that can be controlled by the Transport Layer include:

- Bandwidth: The amount of data that can be transmitted over a network in a given period of time.
- Delay: The time it takes for a packet to travel from the source to the destination.
- Jitter: The variation in delay of packets.
- Packet loss: The percentage of packets that are lost during transmission.

There are several transport protocols that can provide QoS support, including:

- TCP: Transmission Control Protocol is a connection-oriented protocol that provides reliable, in-order delivery of data. It uses flow control and congestion control mechanisms to adjust the rate of data transmission based on network conditions.
- UDP: User Datagram Protocol is a connectionless protocol that provides low-latency, best-effort delivery of data. It is often used for real-time applications such as voice and video.
- SCTP: Stream Control Transmission Protocol is a connection-oriented protocol that provides reliable, in-order delivery of data. It also supports multi-homing, which allows a connection to be established over multiple network paths.

In summary, Quality of Service is an important aspect of the Transport Layer in Computer Networks. It allows the network to provide improved service to certain traffic, and different transport protocols can be used to provide different levels of QoS support. Some of the key QoS parameters that can be controlled by the Transport Layer include bandwidth, delay, jitter, and packet loss.