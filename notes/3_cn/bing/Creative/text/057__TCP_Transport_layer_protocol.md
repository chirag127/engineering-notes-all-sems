#### TCP Transport layer protocol

- TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination .
- TCP is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network .
- TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.
- TCP includes mechanisms to solve many of the problems that arise from packet-based messaging, such as lost packets, out of order packets, duplicate packets, and corrupted packets.
- TCP employs network congestion avoidance. However, there are vulnerabilities in TCP, including denial of service, connection hijacking, TCP veto, and reset attack.
- TCP originated in the initial network implementation in which it complemented the Internet Protocol (IP). Therefore, the entire suite is commonly referred to as TCP/IP.
- TCP is the protocol used most commonly on top of IP, and the Internet protocol stack is sometimes referred to as TCP/IP.
- TCP provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating via an IP network.
- Major internet applications such as the World Wide Web, email, remote administration, and file transfer rely on TCP, which is part of the Transport Layer of the TCP/IP suite. SSL/TLS often runs on top of TCP.
- TCP is divided into a modular architecture consisting of the Transmission Control Protocol and the Internet Protocol.
- TCP uses a three-way handshake to establish a connection between two computers. The first computer sends a packet with the SYN bit set to 1 (SYN = \"synchronize?\"). The second computer sends back a packet with the ACK bit set to 1 (ACK = \"acknowledge!\") plus the SYN bit set to 1. The first computer replies back with an ACK.
- TCP uses sequence and acknowledgement numbers to keep track of which data was successfully received, which data was lost, and which data was accidentally sent twice.
- TCP uses the FIN bit to close the connection when either computer no longer wants to send or receive data. A computer initiates closing the connection by sending a packet with the FIN bit set to 1 (FIN = finish). The other computer replies with an ACK and another FIN. After one more ACK from the initiating computer, the connection is closed.
- TCP segments contain a header and data. The TCP header contains many fields, such as source port number, destination port number, checksum, sequence number, acknowledgement number, SYN bit, ACK bit, and FIN bit .
- The TCP header can range in size from 20 to 60 bytes, depending on the size of the options field .