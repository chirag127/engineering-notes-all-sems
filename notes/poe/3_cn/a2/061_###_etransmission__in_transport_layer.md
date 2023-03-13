 Here is the content in markdown format for the topic ### etransmission  in transport layer:

### Etransmission in Transport Layer

The transport layer provides mechanisms for data transfer between applications running on different hosts. The two most common protocols in this layer are TCP and UDP.

**Transmission Control Protocol (TCP):**

- Provides reliable, in-order delivery of messages with error checking and correction.
- Uses a three-way handshake to establish a connection between two hosts.
- Uses acknowledgements and timeouts to achieve reliable transmission.
- Provides flow control and congestion control.
- Connection-oriented service.

**Mnemonics:** "Please Do Not Throw Sausage Pizza Away" stands for TCP flags: PSH, DNT, SYN, FIN, RST, ACK.

**Learning tricks:** Remember TCP is like a telephone call - it establishes a dedicated end-to-end connection between two hosts so that they can send messages back and forth reliably.

**Advantages:** Reliability, ordering, error correction.
**Disadvantages:** Some overhead due to additional features, can be slower than UDP.
**Applications:** Web browsing, email, file transfer, etc.

**User Datagram Protocol (UDP):**

- Provides fast, unreliable message transmission without error correction.
- Connectionless service.
- Lightweight, minimal overhead.
- Typically used for time-sensitive applications that require fast transmission.

**Mnemonics:** "Unreliable Datagram Protocol" reminds that UDP offers fast but unreliable transmission.

**Learning tricks:** Think of UDP like sending a postcard - you just send off the message and hope it reaches the recipient, but there is no dedicated connection or error correction.

**Advantages:** Speed, low overhead.
**Disadvantages:** Unreliable, messages may be lost, arrive out of order or be duplicated.
**Applications:** Streaming media, online games, DNS lookups, etc.

[Detailed diagrams, code examples, tables, etc. can be added here if required.]