#### TCP Transport layer protocol

- TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination.
- TCP is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network.
- TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.
- TCP provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating via an IP network.
- TCP uses a three-way handshake to establish a connection between two endpoints. The three steps are: SYN, SYN-ACK, and ACK.
- TCP uses a sliding window mechanism to control the flow of data and avoid congestion. The window size indicates how many bytes can be sent before waiting for an acknowledgment.
- TCP uses sequence numbers and acknowledgment numbers to keep track of the data sent and received. Each byte of data has a unique sequence number, and each acknowledgment contains the next expected sequence number.
- TCP uses checksums to detect errors in the data. The checksum is calculated based on the data and a pseudo-header that contains some information from the IP header. The checksum is verified at the receiver side.
- TCP can handle lost, duplicated, or out-of-order packets by using retransmission, selective acknowledgment, and sequence numbers.
- TCP can adjust the transmission rate based on the network conditions and the receiver's feedback. This is called congestion control. TCP uses various algorithms to implement congestion control, such as slow start, congestion avoidance, fast retransmit, and fast recovery.
- TCP can terminate a connection by using a four-way handshake. The four steps are: FIN, ACK, FIN, ACK.
- TCP can support multiple connections between the same pair of hosts by using port numbers. A port number is a 16-bit number that identifies a specific application or process on a host. A TCP connection is identified by a four-tuple: source IP address, source port number, destination IP address, and destination port number.
- TCP can support various options to enhance its functionality, such as maximum segment size, window scaling, timestamp, selective acknowledgment, and urgent pointer.

Some mnemonics and learning tricks for TCP are:

- To remember the three-way handshake, think of SYN as "synchronize", SYN-ACK as "synchronize and acknowledge", and ACK as "acknowledge".
- To remember the four-way handshake, think of FIN as "finish", and ACK as "acknowledge".
- To remember the port numbers of some common applications, think of:

  - HTTP: 80 (eighty sounds like "hatey", which is similar to "HTTP")
  - HTTPS: 443 (four for secure, four for more, three for free)
  - FTP: 20 and 21 (file transfer protocol has two ports, one for data and one for control)
  - SSH: 22 (secure shell has two twos, which look like snakes)
  - Telnet: 23 (telnet has two threes, which look like phones)
  - SMTP: 25 (simple mail transfer protocol has two fives, which look like envelopes)
  - DNS: 53 (domain name system has five and three, which are the first and last letters of "DNS")
  - DHCP: 67 and 68 (dynamic host configuration protocol has six and seven, which are the first and last letters of "DHCP")
  - POP3: 110 (post office protocol version 3 has one and two zeros, which look like a mailbox)
  - IMAP: 143 (internet message access protocol has one and four threes, which look like letters)
  - SNMP: 161 (simple network management protocol has one and six ones, which look like sticks)