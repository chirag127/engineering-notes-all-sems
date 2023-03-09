 Here is the content in markdown format for the given topic:

## Experiment 9 - Applications using TCP and UDP Sockets

### TCP Sockets
- TCP provides reliable, ordered, and error-checked delivery of transmitted data.
- Some applications that use TCP sockets:
    - HTTP: Used for web browsing. Data is transmitted reliably with in-order delivery.
    - FTP: Used for file transfer. Data is transmitted reliably with in-order delivery.
    - Email: SMTP protocol uses TCP for reliable and in-order delivery of emails.
- Advantages: Reliability, ordering, and error-checking. Data is delivered correctly and in the right order.
- Disadvantages: More overhead due to additional reliability mechanisms. Can be slower than UDP.

### UDP Sockets
- UDP provides fast, efficient transmission of data with minimal overhead.
- Some applications that use UDP sockets:
    - DNS: Used for IP address lookup. Speed is prioritized over reliability. Some packet loss is tolerable.
    - TFTP: Used for simple file transfer. Speed is prioritized over reliability. Some packet loss is tolerable.
    - Streaming media: Speed is prioritized over reliability. Some packet loss is tolerable.
- Advantages: Lightweight, minimal overhead, and fast.
- Disadvantages: No reliability mechanisms. Packets may be lost, delivered out of order, or corrupted.

[Detailed diagrams and examples can be added here for more clarity and learning.]

The content explains the two types of sockets - TCP and UDP sockets. The applications, advantages, and disadvantages of using each socket type are discussed. Additional details can be added in the form of diagrams or examples to enhance understanding. Please let me know if you would like me to modify or expand the answer.