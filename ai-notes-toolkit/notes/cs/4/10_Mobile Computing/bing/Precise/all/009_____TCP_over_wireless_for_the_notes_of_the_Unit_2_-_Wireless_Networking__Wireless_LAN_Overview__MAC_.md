# TCP over Wireless

TCP (Transmission Control Protocol) is a protocol that enables the scalability of the internet through its flow control mechanisms. It is used for web browsing, which is expected to be the dominant application in wireless data networks .

Wireless networks, such as 3G networks, exhibit high delays and high error rates. TCP assumes a relatively reliable underlying network where most packet losses are due to congestion. However, in a wireless network, packet losses will occur more often due to unreliable wireless links than due to congestion .

To deal with packet losses due to fading, shadowing, and contention, TCP optimization for wireless networks should preferably maintain TCP end-to-end semantics with minimal dependence on intermediate nodes. The development of advanced 3G networks and services makes it necessary to find a way of improving TCP's efficiency and resource utilization .

One solution is to split the TCP connection at the wireless interface, namely, the base station, which in turn uses some other reliable connection to connect to the destination. This solution is referred to as split-connection .

The desired attributes of a solution for TCP over wireless networks are that it must maintain TCP’s end-to-end semantics, meaning that a packet is acknowledged only after being received by the final destination. Additionally, modifications must be local, meaning that only the Base Station (BS) and Mobile Host (MH) are in the control of the wireless service provider. It is not possible to change all locations that the MH visits .