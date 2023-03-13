The TCP/IP protocol suite is a set of communication protocols that are used in the Internet and similar computer networks. It consists of four layers: the application layer, the transport layer, the internet layer, and the network access layer. Each layer has a specific function and interacts with the adjacent layers.

The application layer provides the interface for the user applications, such as web browsers, email clients, file transfer programs, etc. It uses protocols such as HTTP, SMTP, FTP, etc. to exchange data with the transport layer.

The transport layer provides reliable and efficient data transmission between the application layer and the internet layer. It uses protocols such as TCP and UDP to segment, reassemble, and order the data packets. TCP also provides error detection, flow control, and congestion control mechanisms.

The internet layer provides the routing and addressing functions for the data packets. It uses protocols such as IP, ICMP, ARP, etc. to assign unique IP addresses to each device and to determine the best path for the packets to reach their destination.

The network access layer provides the physical and data link functions for the data packets. It uses protocols such as Ethernet, Wi-Fi, PPP, etc. to encode, decode, and transmit the data packets over the network medium.

The following diagram illustrates the basic architecture of the TCP/IP protocol suite in computer networks:

```
+--------------------------+--------------------------+--------------------------+
|        Application       |        Application       |        Application       |
|          Layer           |          Layer           |          Layer           |
+--------------------------+--------------------------+--------------------------+
|        Transport         |        Transport         |        Transport         |
|          Layer           |          Layer           |          Layer           |
+--------------------------+--------------------------+--------------------------+
|         Internet         |         Internet         |         Internet         |
|          Layer           |          Layer           |          Layer           |
+--------------------------+--------------------------+--------------------------+
|      Network Access      |      Network Access      |      Network Access      |
|          Layer           |          Layer           |          Layer           |
+--------------------------+--------------------------+--------------------------+
|          Media           |          Media           |          Media           |
+--------------------------+--------------------------+--------------------------+
```