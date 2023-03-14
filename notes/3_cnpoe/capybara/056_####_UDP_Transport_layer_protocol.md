#### UDP Transport layer protocol

The User Datagram Protocol (UDP) is a transport layer protocol that is used for sending data over the internet. Unlike the Transmission Control Protocol (TCP), UDP is a connectionless protocol, which means that it does not establish a reliable connection before sending data. Instead, UDP simply sends data packets, called datagrams, to the destination without any guarantees about their delivery.

Here are some important points to remember about the UDP protocol:

- UDP is a simple protocol that is used for applications that require low latency and high throughput, such as online gaming, streaming media, and real-time communication.
- UDP does not provide any reliable delivery guarantees, such as error checking, retransmission, or flow control. This means that packets may be lost, duplicated, or arrive out of order.
- UDP does not establish a connection before sending data. Instead, each datagram is sent independently and may be received by the destination in any order.
- UDP does not include any congestion control mechanisms, which means that it may contribute to network congestion if it is used excessively.
- UDP is often used in conjunction with other protocols, such as the Domain Name System (DNS), which uses UDP to make simple queries for host names and IP addresses.

Here are some mnemonic devices that may help you remember the key features of UDP:

- "UDP is Unreliable, Unconnected, and Uncontrolled."
- "UDP is like sending a postcard: you don't know if it will arrive, and you don't get a receipt."

While UDP has its limitations, it is an important protocol for many applications that require low latency and high throughput. By understanding the basics of UDP, you can better understand how data is sent over the internet and how to optimize your network for different types of applications.