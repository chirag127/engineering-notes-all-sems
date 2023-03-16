# 6LoWPAN

6LoWPAN stands for IPv6 over Low-Power Wireless Personal Area Networks. It is a networking technology or adaptation layer that allows IPv6 packets to be carried efficiently within small link layer frames, such as those defined by IEEE 802.15.4.

- 6LoWPAN is a mesh network that is robust, scalable, and can heal on its own. It delivers low-cost and secure communication in IoT devices.
- It uses IPv6 protocol and so it can be directly routed to cloud platforms. It offers one-to-many and many-to-one routing. In the network, leaf nodes can be in sleep mode for a longer duration of time.
- The 6LoWPAN network is connected to the IPv6 network using an edge router. The edge router handles three actions: 1) the data exchange between 6LoWPAN devices and the Internet (or other IPv6 network); 2) local data exchange between devices inside the 6LoWPAN; and 3) the generation and maintenance of the radio subnet (the 6LoWPAN network).
- The most basic requirements for a link layer to support 6LoWPAN are framing, unicast transmission and addressing. Addressing is required to differentiate between nodes on a link, and to form IPv6 addresses which are then elided by 6LoWPAN compression.
