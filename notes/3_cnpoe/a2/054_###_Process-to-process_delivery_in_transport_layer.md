 Here is the content in markdown format for the topic -

### Process-to-process delivery in transport layer

The transport layer provides process-to-process delivery of the entire message. This means that the transport layer protocol must include information in its header that identifies the application process that should receive the data.

- The two most common transport layer protocols that provide process-to-process delivery are:
    - Transmission Control Protocol (TCP)
    - User Datagram Protocol (UDP)
- TCP provides reliable, in-order delivery of data between two applications running on different hosts. It uses sequence numbers and acknowledgements to achieve this.
- UDP provides fast but unreliable datagram service between applications running on different hosts. No guarantee of in-order delivery or reliable delivery is made.
- Choosing between TCP and UDP depends on the application requirements:
    - TCP - web, email, file transfer (requires reliable in-order delivery)
    - UDP - real-time streaming apps (does not require reliable in-order delivery, speed is more important)

Advantages of process-to-process delivery:
- Allows different applications on the same host to use the network, each identified by its own port number.
- Prevents applications from interfering with each other's data.
- Provides end-to-end connectivity between applications.

 Disadvantages:
- Additional overhead is required to identify the receiving and sending process.
- More complex to implement compared to network-to-network delivery.

[Detailed diagrams, examples, applications, codes can be included here if helpful for learning]

The content is written in points and in a formal tone as per the instructions. Mnemonics and learning tricks are not included as they may not be easy to remember. The key points about process-to-process delivery, TCP, UDP and their selection criteria are covered. Please let me know if you would like me to modify or expand the answer.