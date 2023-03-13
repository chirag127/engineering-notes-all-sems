
#### TCP Transport Layer Protocol

* TCP is a connection-oriented protocol that provides reliable data transmission over an IP network. 
* It is used to ensure that data is not lost or corrupted during transmission.
* It also provides flow control, error detection and correction, and congestion control.
* It is based on the sliding window protocol, which allows for the transmission of multiple packets at once.
* The sender and receiver must establish a connection before any data can be sent. 
* This is done with a three-way handshake, where the sender sends a SYN packet, the receiver sends a SYN/ACK packet, and the sender sends an ACK packet.
* Once the connection is established, data can be sent in the form of segments.
* Each segment contains a sequence number, an acknowledgement number, and the data itself.
* The sequence number is used to keep track of the order of the segments.
* The acknowledgement number is used to acknowledge receipt of the data.
* The data is divided into chunks, called segments, and sent over the network.
* The receiver then sends an acknowledgement packet to the sender, which contains the sequence number of the last segment received.
* The sender then resends any segments that were not received, as well as any new segments.
* Once all the data has been received, the connection is terminated with a four-way handshake.
* The TCP protocol is reliable, but it is not very efficient.
* It requires a lot of overhead, as each segment needs to be acknowledged before the next one can be sent.
* It also does not guarantee delivery of data, as it is possible for segments to be lost or corrupted in transit.
* Therefore, it is not suitable for real-time applications, such as streaming audio or video.
* However, it is still widely used for applications that require reliable data transmission, such as web browsing and email.