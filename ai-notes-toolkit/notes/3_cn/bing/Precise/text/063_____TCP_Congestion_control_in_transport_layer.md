### TCP Congestion control in transport layer

- TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination.
- TCP is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network.
- TCP is arguably one of the most important Internet protocols, as it carries a much higher volume of traffic on the Internet than any other transport-layer protocol.
- Because TCP carries so much traffic, its congestion control algorithm is the main technique which prevents the Internet from slowing to a crawl due to over-utilization.
- There are three phases that TCP uses for congestion control: slow start, congestion avoidance, and congestion detection.
- In the first phase of congestion control, the sender sends the packet and gradually increases the number of packets until it reaches a threshold.
- TCP flow control is more variable and allows the sender and receiver to adjust the flow for optimum efficiency.
- TCP can modify its window size based on ECN.
- Different operating systems handle it differently. ECN is not widely used and most OS's have it disabled by default.