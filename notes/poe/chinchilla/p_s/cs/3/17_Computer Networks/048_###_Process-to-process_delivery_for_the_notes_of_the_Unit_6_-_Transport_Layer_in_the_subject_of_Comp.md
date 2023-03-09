### Process-to-process delivery for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

The Transport Layer is responsible for providing process-to-process communication services over the network. It ensures that data is delivered to the correct application process running on the receiving host. This layer is responsible for breaking down the data into smaller segments and reassembling them at the receiving end. 

The process-to-process delivery is achieved through the following protocols:

1. Transmission Control Protocol (TCP)
TCP provides a reliable, connection-oriented service that guarantees the delivery of data to the destination. It establishes a virtual connection between the sender and the receiver before transmitting data. TCP breaks the data into segments, adds sequence numbers to each segment, and sends them to the receiver. The receiver acknowledges the receipt of each segment and requests retransmission of any missing segments. TCP also performs flow control to prevent the sender from overwhelming the receiver.

2. User Datagram Protocol (UDP)
UDP provides a connectionless, unreliable service that does not guarantee the delivery of data to the destination. It does not establish a virtual connection before transmitting data. UDP breaks the data into datagrams and sends them to the receiver. The receiver can receive the datagrams in any order and may miss some datagrams. UDP does not perform flow control or error correction.

TCP and UDP are used by various applications depending on their requirements. For example, applications that require reliable data delivery such as email, file transfer, and web browsing use TCP. Applications that require low latency and can tolerate some loss of data such as video streaming, online gaming, and VoIP use UDP.

Advantages of process-to-process delivery:

1. Provides reliable and efficient delivery of data to the destination.
2. Enables multiple applications to communicate over the same network.
3. Supports different types of applications with varying requirements.

Disadvantages of process-to-process delivery:

1. TCP can introduce latency due to the establishment of a virtual connection before transmission of data.
2. UDP does not guarantee the delivery of data, which can result in loss of data.
3. Both protocols can be susceptible to congestion in the network, leading to decreased performance.

Examples of applications that use process-to-process delivery:

1. Email clients such as Microsoft Outlook and Apple Mail use TCP for reliable delivery of emails.
2. File transfer protocols such as FTP and SFTP use TCP for reliable delivery of files.
3. Video streaming services such as Netflix and YouTube use UDP for low latency delivery of video.

In conclusion, process-to-process delivery is an essential function of the Transport Layer in computer networks. TCP and UDP protocols provide reliable and efficient delivery of data to the destination, and applications can choose the appropriate protocol depending on their requirements.