 Here is the content in markdown format for Unit 4 - Transport Layer in Computer Networks:

## Unit 4 - Transport Layer in Computer Networks

The Transport Layer is responsible for end-to-end delivery of the complete message or file. It provides the upper layer applications running at the source and destination hosts with communication services.

Some key responsibilities of the Transport Layer are:

- Segmentation and Reassembly: The Transport Layer divides the message into segments and reassembles the segments into the original message at the receiving end.
- Connection Establishment, Management and Release: The Transport Layer handles the connection between the sending and receiving applications. It establishes, maintains and releases the connection.
- Sequence Numbers: The Transport Layer assigns sequence numbers to the segments to ensure proper ordering of the segments at the destination.
- Error Control: The Transport Layer implements mechanisms to detect and possibly recover from errors that may occur during transmission.
- Flow Control: The Transport Layer implements mechanisms to avoid overwhelming the receiver with too many segments. It regulates the transmission rate between the sender and receiver.

The two primary Transport Layer protocols are:

- Transmission Control Protocol (TCP): Provides reliable, ordered and error-checked delivery of transmitted packets over IP networks. It is a connection-oriented protocol.
- User Datagram Protocol (UDP): Provides fast but unordered and unerror-checked delivery of transmitted packets over IP networks. It is a connectionless protocol.

Some mnemonics and learning tricks for TCP:

- Think of TCP as a Telephone Call Process - where connection is established first, communication takes place and then the connection is terminated.
- The TCP handshake uses the sequence SYN, SYN-ACK, ACK to establish a connection - remember it as 'I (SYN) want to talk, Do (SYN-ACK) you want to talk, Yes (ACK) I want to talk'
- TCP provides guaranteed delivery with ordered, error-checked packets - think 'GOODE' for Guaranteed, Ordered, Error-checked, Delivery

[Detailed explanations, ASCII diagrams, examples, advantages, disadvantages, applications, etc. can be added here for TCP and UDP if required.]