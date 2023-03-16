#### UDP Transport layer protocol

UDP (User Datagram Protocol) is a connectionless transport layer protocol used in computer networking. It is a simple protocol that does not guarantee delivery or order of packets, but is useful for applications that require low latency and can tolerate packet loss.

Here are some key characteristics and features of UDP:

- **Connectionless:** Unlike TCP, UDP is a connectionless protocol, which means that there is no handshaking process between the sender and receiver before data transmission. This makes it faster than TCP, but also less reliable.
- **Unreliable:** UDP does not guarantee delivery of packets or order of transmission. Packets may be lost, duplicated, or arrive out of order.
- **Low overhead:** UDP has a smaller header size than TCP, which means that there is less overhead and it is more efficient for small packets.
- **No congestion control:** UDP does not have built-in mechanisms to control congestion, which means that it can potentially flood the network with packets if the sender does not limit the rate of transmission.
- **Simple:** UDP is a simple protocol that is easy to implement and use. It does not require complex state tracking or error recovery mechanisms like TCP.
- **Used for real-time applications:** UDP is commonly used for real-time applications such as video conferencing, online gaming, and VoIP (Voice over IP), where low latency is more important than reliability.

Overall, UDP is a lightweight and efficient protocol that is well-suited for applications that require low latency and can tolerate some packet loss. However, it is not suitable for applications that require reliable delivery or congestion control.