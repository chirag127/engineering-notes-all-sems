

#### UDP Transport Layer Protocol
- UDP (User Datagram Protocol) is a connectionless, unreliable, and message-oriented protocol. 
- It is used for applications that require fast, low-overhead transmissions, such as streaming audio and video.
- UDP does not require a connection to be established and is therefore suitable for broadcast transmissions. 
- It does not guarantee delivery of data packets and does not provide error correction.
- UDP uses port numbers to identify different applications on the same host. 
- It has a header of 8 bytes and a payload of up to 65,535 bytes.
- UDP is a connectionless protocol, meaning that data is sent without the need to establish a connection between the sender and receiver. 
- The sender does not need to wait for an acknowledgement from the receiver before sending the next packet. 
- This makes UDP a good choice for applications that require fast transmission, such as streaming audio and video.
- UDP is an unreliable protocol, meaning that data packets may be lost or arrive out of order. 
- To ensure reliable delivery, applications must implement their own error correction and retransmission mechanisms.
- UDP is a message-oriented protocol, meaning that the data is sent as discrete messages rather than as a continuous stream. 
- This makes it suitable for applications that require discrete chunks of data, such as file transfers or remote procedure calls.
- UDP is a broadcast protocol, meaning that data can be sent to multiple recipients at once. 
- This makes it suitable for applications that require one-to-many communication, such as streaming audio and video.
- Mnemonics for UDP: 
  - Unreliable Datagram Protocol 
  - Unreliable Delivery Protocol 
  - Unreliable Data Protocol 
  - User Datagram Packet 
  - Universal Datagram Protocol