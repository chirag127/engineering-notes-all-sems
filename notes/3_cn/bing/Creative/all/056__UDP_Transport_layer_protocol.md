#### UDP Transport layer protocol

- UDP stands for User Datagram Protocol. It is one of the core communication protocols of the Internet protocol suite, also known as UDP/IP suite. 
- UDP is a simple, connectionless and unreliable transport layer protocol that does not require prior communication to set up communication channels or data paths.  
- UDP provides checksums for data integrity, and port numbers for addressing different functions at the source and destination of the datagram. 
- UDP does not provide any guarantees to the upper layer protocol for message delivery, ordering, or duplicate protection.   If transmission reliability is desired, it must be implemented in the user's application.
- UDP is suitable for purposes where error checking and correction are either not necessary or are performed in the application.  UDP avoids the overhead of such processing in the protocol stack.
- UDP is transaction-oriented, suitable for simple query-response protocols such as the Domain Name System (DNS) or the Network Time Protocol (NTP). 
- UDP provides datagrams, suitable for modeling other protocols such as IP tunneling or remote procedure call (RPC) and the Network File System (NFS). 
- UDP is simple, suitable for bootstrapping or other purposes without a full protocol stack, such as the Dynamic Host Configuration Protocol (DHCP) and the Trivial File Transfer Protocol (TFTP). 
- UDP is more efficient in terms of both latency and bandwidth than TCP, which is the dominant transport layer protocol used with most of the Internet services. 
- UDP is used for real-time services like computer gaming, voice or video communication, live conferences, etc. where dropping packets is preferable to waiting for packets delayed due to retransmission.  

UDP Header –

- UDP header is an 8-bytes fixed and simple header, while for TCP it may vary from 20 bytes to 60 bytes. 
- The first 8 Bytes contains all necessary header information and the remaining part consist of data. 
- UDP port number fields are each 16 bits long, therefore the range for port numbers is defined from 0 to 65535; port number 0 is reserved. 
- Port numbers help to distinguish different user requests or processes. 

| Source Port | Destination Port |
| ----------- | ---------------- |
| 16 bits     | 16 bits          |

| Length      | Checksum         |
| ----------- | ---------------- |
| 16 bits     | 16 bits          |

- Source Port: Source Port is a 2 Byte long field used to identify the port number of the source. 
- Destination Port: It is a 2 Byte long field, used to identify the port of the destined packet. 
- Length: Length is the length of UDP including the header and the data. It is a 16-bits field. 
- Checksum: Checksum is 2 Bytes long field. It is the 16-bit one’s complement of the one’s complement sum of the UDP header, the pseudo-header of information from the IP header, and the data, padded with zero octets at the end (if necessary) to make a multiple of two octets.  

Notes –

- Unlike TCP, the Checksum calculation is not mandatory in UDP. 
- No Error control or flow control is provided by UDP. Hence UDP depends on IP and ICMP for error reporting. 
- Also UDP provides port numbers so that is can differentiate between users requests. 
- Applications of UDP: 
  - Used for simple request-response communication when the size of data is less and hence there is lesser concern about flow and error control.
  - It is a suitable protocol for multicasting as UDP supports packet switching.
  - UDP is used for some routing update protocols like RIP (Routing Information Protocol).
  - Normally used for real-time applications which can not tolerate uneven delays between sections of a received message.
  - Following implementations uses UDP as a transport layer protocol: NTP (Network Time Protocol), DNS (Domain Name Service), BOOTP, DHCP, NNP (Network News Protocol).

Mnemonics and learning tricks for UDP Transport layer protocol –

- To remember the attributes of UDP, you can use