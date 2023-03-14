 Here is the content written in markdown format for the topic ### etransmission  in transport layer:

### Etransmission in Transport Layer

The transport layer provides end-to-end communication between application processes running on different hosts. The two most commonly used transport protocols are:

- Transmission Control Protocol (TCP)
- User Datagram Protocol (UDP)

**TCP** provides reliable, ordered, and error-checked delivery of transmitted data. It uses a three-way handshake to establish a connection between two hosts and includes mechanisms for congestion control and flow control. Some key points about TCP are:

- Provides reliable communication with error checking and correction.
- Uses sequential number for ordering packets. Out-of-order packets are reordered.
- Uses acknowledgements and timeouts to ensure reliable delivery.
- Provides congestion control through sliding window protocol.
- Connection-oriented protocol with three-way handshake (SYN, SYN-ACK, ACK).

**UDP** provides fast and efficient transfer of data with minimal error checking. It is a connectionless protocol, meaning there is no establishment of a dedicated end-to-end connection between two hosts. Some key points about UDP are:

- Fast and efficient but provides only best-effort delivery, no guaranteed delivery.
- Connectionless protocol with no handshaking.
- Use for time-sensitive applications (e.g. video streaming) where some packet loss is tolerable.
- Lightweight protocol with minimal overhead (header size 8 bytes).

**Mnemonics**

- TCP = Transmission Control Protocol -> Think **T**ransmission **C**ontrol
- UDP = User Datagram Protocol -> Think **U**ser **D**atagram
- UDP is fast and efficient but no guarantee of delivery -> Think **U**nreliable **D**elivery

[Detailed diagrams, examples, advantages, disadvantages, applications, etc. can be added here if required.]