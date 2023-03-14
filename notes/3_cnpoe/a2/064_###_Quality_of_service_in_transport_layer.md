 Here is the content in markdown format on the topic ### Quality of service in transport layer:

### Quality of service in transport layer

The transport layer provides different quality of service options to the upper layer applications. The quality of service refers to the level of guarantee on the delivery of data and service. The different QoS options provided by the transport layer are:

1. Best effort: This is the default service where the transport layer does not provide any guarantee on delivery of data. The packets are sent on first come first serve basis and no priority is given to any packet. The applications that do not require high reliability like web browsing use the best effort service.

2. Guaranteed delivery: In this service, the transport layer guarantees the delivery of packets to the destination. It uses acknowledgements and retransmissions to ensure all packets are delivered. The file transfer applications use this service.

3. Throughput: The transport layer can guarantee a certain level of throughput to the applications. The throughput refers to the amount of data transferred per unit time. Real-time applications like video streaming may require a minimum throughput guarantee from the transport layer.

4. Delay bound: The transport layer can provide a delay bound which is the maximum time taken by a packet to reach the destination. This delay guarantee is required for real-time applications like VoIP calls which are delay sensitive.

5. Packet loss rate: The transport layer can provide a guarantee on maximum packet loss rate to the application. For example, it can guarantee that no more than 1% of the packets will be lost. Applications like video streaming which are sensitive to packet loss use this QoS option.

**Mnemonics:**

- BEst effort - Browsers use
- Guaranteed - File Transfer uses
- Throughput - Video streaming needs
- Delay - VoIP calls are sensitive
- Loss - Video streaming avoids

[Detailed diagrams, examples, codes, advantages, disadvantages, and applications can be added here if required.]