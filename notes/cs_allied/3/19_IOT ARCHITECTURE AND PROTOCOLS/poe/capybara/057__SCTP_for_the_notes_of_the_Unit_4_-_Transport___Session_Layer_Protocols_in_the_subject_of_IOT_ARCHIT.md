### SCTP

SCTP (Stream Control Transmission Protocol) is a transport layer protocol that provides reliable, message-oriented communication between two endpoints. It is designed to support the transmission of multiple streams of data between two hosts.

Here are some key features of SCTP:

- **Message-Oriented Communication**: SCTP is message-oriented, which means that it allows applications to send and receive messages of fixed or variable length. This makes it ideal for applications that require reliable, ordered delivery of messages, such as telephony and messaging applications.

- **Reliability**: SCTP provides reliable transport of messages between two endpoints. It uses a mechanism called selective acknowledgment (SACK) to ensure that all messages are received in the correct order.

- **Ordered Delivery**: SCTP guarantees that messages are delivered in the order in which they were sent. This is important for applications that require ordered delivery, such as voice and video applications.

- **Flow Control**: SCTP provides flow control mechanisms to prevent the sender from overwhelming the receiver with too much data. This ensures that the receiver can process the data at its own pace.

- **Multiplexing**: SCTP supports the transmission of multiple streams of data between two hosts. Each stream is identified by a unique stream identifier (SID), which allows the receiver to distinguish between different streams of data.

- **Path Management**: SCTP supports the use of multiple paths between two hosts. This allows it to provide redundancy and improve performance by using the most efficient path for each stream of data.

- **Heartbeats**: SCTP uses heartbeats to monitor the connectivity of the endpoints. If one endpoint fails to respond to a heartbeat, the other endpoint can take action to re-establish the connection.

SCTP is used in a variety of applications, including telephony, messaging, and video conferencing. It is also used in some Internet of Things (IoT) applications that require reliable, message-oriented communication between two endpoints.