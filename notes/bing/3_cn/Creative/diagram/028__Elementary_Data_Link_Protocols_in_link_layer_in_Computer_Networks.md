The data link layer is the second layer of the OSI model that provides reliable and efficient communication between adjacent nodes on a network. The data link layer is responsible for framing, error control and flow control. The data link layer protocols are designed to implement these functions in different scenarios.

The elementary data link layer protocols are the simplest protocols that can be used in the data link layer. They are divided into three categories, based on the assumptions and requirements of the communication channel:

- Protocol 1: Unrestricted simplex protocol. This protocol assumes that the sender can transmit data frames continuously without any feedback from the receiver. The receiver does not send any acknowledgments or control frames. This protocol is suitable for simplex channels that are error-free and have unlimited bandwidth.

- Protocol 2: Simplex stop and wait protocol. This protocol assumes that the sender can transmit only one data frame at a time and must wait for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment for each received frame. This protocol is suitable for simplex channels that are error-prone and have limited bandwidth.

- Protocol 3: Simplex protocol for noisy channels. This protocol assumes that the sender can transmit only one data frame at a time and must wait for a positive acknowledgment from the receiver before sending the next frame. The receiver sends a positive acknowledgment for each correctly received frame and a negative acknowledgment for each corrupted frame. The sender retransmits the frame if it receives a negative acknowledgment or a timeout occurs. This protocol is suitable for simplex channels that are noisy and have limited bandwidth.

The following diagram illustrates the basic architecture of a data link layer protocol:

```
+-----------------+      +-----------------+
|                 |      |                 |
|    Sender       |      |    Receiver     |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Data link layer |      | Data link layer |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Physical layer  |      | Physical layer  |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|    Channel      |<---->|    Channel      |
|                 |      |                 |
+-----------------+      +-----------------+
```

The following diagram illustrates the frame format of a data link layer protocol:

```
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Header       |    Payload      |    Trailer      |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
| Control | SeqNo |    Data         | Checksum | Flag |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
```

The header contains the control field and the sequence number field. The control field indicates the type of the frame, such as data, acknowledgment, or negative acknowledgment. The sequence number field identifies the frame uniquely and helps in detecting duplicate or lost frames. The payload contains the data to be transmitted. The trailer contains the checksum field and the flag field. The checksum field is used for error detection and correction. The flag field marks the end of the frame and helps in frame synchronization.