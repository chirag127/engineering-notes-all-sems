### TCP Congestion control in transport layer

Transmission Control Protocol (TCP) is a reliable transport protocol that ensures data is transmitted without loss or corruption. TCP congestion control is a critical component of the protocol that manages the network congestion during data transmission.

TCP congestion control ensures that the network does not become congested and that packets are not lost due to congestion. This is achieved by monitoring the network for signs of congestion and adjusting the transmission rate accordingly.

Here are some important points to keep in mind when studying TCP congestion control:

1. Slow start: When a new TCP connection is established, TCP starts with a low transmission rate and gradually increases the rate until it detects signs of congestion.

2. Congestion avoidance: Once slow start is complete, TCP enters congestion avoidance mode. In this mode, TCP monitors the network for signs of congestion and adjusts the transmission rate accordingly.

3. Fast retransmit and recovery: If TCP detects that a packet has been lost, it retransmits the packet and enters fast recovery mode. In this mode, TCP reduces the transmission rate and gradually increases it as it receives acknowledgements from the receiver.

4. Explicit congestion notification: TCP can receive explicit notifications from routers that the network is congested. When this happens, TCP reduces the transmission rate to avoid further congestion.

Mnemonics and learning tricks for TCP congestion control:

1. "Slow and steady wins the race" - Slow start is a critical part of TCP congestion control, and taking it slow at the start can help prevent congestion later on.

2. "Avoid congested roads" - Congestion avoidance mode helps TCP steer clear of congested areas, just like how we avoid congested roads when driving.

Overall, TCP congestion control is a vital component of the TCP protocol that ensures reliable data transmission over the network. Understanding the different modes of TCP congestion control and the strategies for managing congestion is essential for anyone working with network protocols.