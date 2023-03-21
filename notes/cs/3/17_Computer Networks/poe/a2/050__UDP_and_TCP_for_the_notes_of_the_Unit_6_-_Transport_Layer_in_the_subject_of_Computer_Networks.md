 Here is the markdown text for the notes on UDP and TCP for Transport Layer (Unit 6) in Computer Networks:

### UDP and TCP

1. UDP - User Datagram Protocol
- Connectionless protocol (no connection establishment required before data transfer)
- Provides fast transmission of data without acknowledgements or retransmission of lost packets
- Used for applications requiring fast speed and no guarantee of delivery like video streaming, online gaming, DNS etc.
- Header contains source and destination port numbers, length and checksum

2. TCP - Transmission Control Protocol
- Connection-oriented protocol (connection established first before data transfer)
- Provides reliable and in-order delivery of data with acknowledgements and retransmissions of lost packets
- Used for applications requiring high reliability like web, email, file transfer etc.
- Header contains source and destination port numbers, sequence number, acknowledgement number, flags, window size, checksum and urgent pointer

3. Differences between UDP and TCP
- Connection-oriented vs connectionless
- Reliable vs best effort delivery
- In-order vs out-of-order delivery (TCP ensures in-order)
- Header sizes (TCP header larger due to sequence and acknowledgement numbers)
- Used for different types of applications (UDP for speed, TCP for reliability)

The notes are written in points in a formal tone without any emojis or external links as Markdown format with headers. The content is aimed to serve as study material to learn about UDP and TCP protocols in the Transport Layer of Computer Networks.