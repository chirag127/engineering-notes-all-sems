#### Elementary Data Link Protocols in link layer in Computer Networks

- Protocols in the data link layer are designed so that this layer can perform its basic functions: framing, error control and flow control.
- Framing is the process of dividing bit-streams from physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control is the process of detecting and correcting errors that may occur during transmission.
- Flow control is the process of regulating the rate of data transmission between sender and receiver to avoid congestion or buffer overflow.
- Elementary data link layer protocols are divided into three different sub categories such as:
  - Protocol 1: Unrestricted simplex protocol
  - Protocol 2: Simplex stop and wait protocol
  - Protocol 3: Simplex protocol for noisy channels
- Let us discuss each protocol one by one.

##### Protocol 1: Unrestricted simplex protocol
- This protocol is the simplest form of data link layer protocol.
- It assumes that the communication channel is error-free and there is no need for error or flow control.
- The sender can send data frames continuously without waiting for any acknowledgment from the receiver.
- The receiver can only receive data frames and cannot send any feedback to the sender.
- This protocol is suitable for applications where data transmission is one-way and the data rate is low.
- For example, a printer connected to a computer can use this protocol to receive print commands from the computer.
- A possible diagram of this protocol is shown below:

```
Sender                          Receiver
  |                               |
  |  Frame 1                      |
  |------------------------------>|
  |                               |
  |  Frame 2                      |
  |------------------------------>|
  |                               |
  |  Frame 3                      |
  |------------------------------>|
  |                               |
  |  Frame 4                      |
  |------------------------------>|
  |                               |
  |  Frame 5                      |
  |------------------------------>|
  |                               |
  |  Frame 6                      |
  |------------------------------>|
  |                               |
```

##### Protocol 2: Simplex stop and wait protocol
- This protocol is an improvement over the unrestricted simplex protocol.
- It assumes that the communication channel is still error-free but there is a need for flow control.
- The sender can send only one data frame at a time and must wait for an acknowledgment from the receiver before sending the next frame.
- The receiver can send an acknowledgment to the sender after receiving a data frame.
- The acknowledgment can be a simple signal or a special frame that indicates the successful reception of the data frame.
- This protocol is suitable for applications where data transmission is one-way but the data rate is high or variable.
- For example, a video streaming service can use this protocol to send video frames to a client.
- A possible diagram of this protocol is shown below:

```
Sender                          Receiver
  |                               |
  |  Frame 1                      |
  |------------------------------>|
  |                               |
  |                         ACK 1 |
  |<------------------------------|
  |                               |
  |  Frame 2                      |
  |------------------------------>|
  |                               |
  |                         ACK 2 |
  |<------------------------------|
  |                               |
  |  Frame 3                      |
  |------------------------------>|
  |                               |
  |                         ACK 3 |
  |<------------------------------|
  |                               |
  |  Frame 4                      |
  |------------------------------>|
  |                               |
  |                         ACK 4 |
  |<------------------------------|
  |                               |
```

##### Protocol 3: Simplex protocol for noisy channels
- This protocol is an improvement over the simplex stop and wait protocol.
- It assumes that the communication channel is noisy and there is a need for both error and flow control.
- The sender can send only one data frame at a time and must wait for a positive acknowledgment from the receiver before sending the next frame.
- The receiver can send a positive acknowledgment to the sender after receiving a data frame without any error.
- The receiver can also send a negative acknowledgment to the sender after receiving a data frame with an error.
- The sender can retransmit the data frame if it does not receive any acknowledgment or receives a negative acknowledgment from the receiver within a specified time limit.
- The