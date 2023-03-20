### Datagram for the notes of the Unit 3 - Scripting in the subject of Web Technology

- A datagram is a basic unit of information that is exchanged between two network devices. It is an independent, self-contained entity that carries sufficient information to be routed from the source to the destination computer without relying on any previous communication between the two.

- In the context of web technology, datagrams are used to transfer data between web servers and clients. When a user accesses a website, the web server sends a datagram containing the requested data to the client's browser, which then displays the data on the user's screen.

- Datagram protocols, such as the User Datagram Protocol (UDP), are used in situations where speed and efficiency are more important than reliability. Unlike Transmission Control Protocol (TCP), which ensures that all data packets are received in the correct order and without errors, UDP does not provide any such guarantees. However, this makes it faster and more efficient for certain types of data transfer.

- UDP datagrams are often used in real-time applications, such as video streaming and online gaming, where speed is critical and the occasional dropped packet is acceptable. In contrast, TCP is more commonly used in web applications where reliability is important, such as e-commerce sites and online banking.

- When sending datagrams, it is important to consider the size of the datagram and the maximum transmission unit (MTU) of the network. If a datagram is too large to fit within a single packet, it will be broken up into multiple packets, which can lead to delays and potential packet loss. To avoid this, it is recommended to limit the size of datagrams and to use a protocol that supports fragmentation and reassembly, such as IP.

- In summary, datagrams are an essential component of web technology and are used to transfer data between web servers and clients. Understanding how datagrams work and their role in network communication is important for anyone working in the field of web development.