 Here is the content in Markdown format with formal tone and without external links or emojis:

#### UDP Transport layer protocol

- UDP stands for User Datagram Protocol. It is a transport layer protocol used for establishing low-latency and loss-tolerating connections between applications on the network.
- UDP is a connectionless protocol as it does not establish a dedicated end-to-end connection between the sending and receiving hosts. It just appends the source and destination port numbers to the header and sends the datagram.
- Due to the lack of connection establishment, the overhead is low and hence UDP is suitable for applications requiring fast transmission of data such as real-time video and audio streaming.
- However, since there is no connection, reliability is not guaranteed. Datagrams may arrive out of order or may not arrive at all. The application using UDP must take care of checking for errors and ensuring complete delivery of data.
- The header size of UDP is 8 bytes, which makes its overhead very less compared to TCP. This makes it a preferred choice for applications with strict latency requirements.
- Some applications that use UDP are DNS, SNMP, Routing protocols, Voice over IP, Video streaming etc.

The above points cover the key highlights of the UDP transport layer protocol in a formal tone with Markdown formatting and without any external links or emojis. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.