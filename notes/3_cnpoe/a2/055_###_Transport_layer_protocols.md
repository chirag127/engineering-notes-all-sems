 Here is the content in markdown format on the topic ### Transport layer protocols:

### Transport layer protocols

The transport layer protocols provide end-to-end communication between processes running on different hosts. The key transport layer protocols are:

- TCP: Transmission Control Protocol is a reliable, ordered, and error-checked delivery of transmitted data.

 Mnemonic: "TCP guarantees delivery of packets"

Advantages: reliable data transmission, congestion control, flow control
Disadvantages: overhead, slower than UDP
Applications: HTTP, FTP, SMTP, etc.

- UDP: User Datagram Protocol is an unreliable but faster datagram protocol.

Mnemonic: "UDP is fast but no guarantee of delivery"

Advantages: fast, low overhead
Disadvantages: no guarantee of delivery, order, or error-checking
Applications: DNS, DHCP, streaming media, voice calls, etc.

- SCTP: Stream Control Transmission Protocol is a reliable transport protocol for message-oriented applications.

Advantages: multi-homing (fault tolerance), multiple streams
Disadvantages: not widely supported
Applications: telephony signaling, remote file system sharing

[Detailed diagrams and examples can be added here if required.]

The choice between TCP and UDP depends on the application requirements. TCP is suitable for applications that require high reliability, while UDP is suitable for applications such as real-time streaming that require fast delivery.

Hope this helps! Let me know if you would like me to elaborate on any of the points or add more details to the content.