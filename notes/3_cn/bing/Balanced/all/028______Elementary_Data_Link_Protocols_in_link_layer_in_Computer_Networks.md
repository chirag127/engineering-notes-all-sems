#### Elementary Data Link Protocols in link layer in Computer Networks

- Protocols in the data link layer are designed to perform the basic functions of framing, error control and flow control.
- Framing is the process of dividing bit-streams from physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control is the process of detecting and correcting errors that may occur during transmission or reception of data frames.
- Flow control is the process of regulating the rate of data transmission between the sender and the receiver to avoid congestion or buffer overflow.
- Elementary data link protocols are classified into three categories, as given below:

  - Protocol 1: Unrestricted simplex protocol
  - Protocol 2: Simplex stop-and-wait protocol
  - Protocol 3: Simplex protocol for noisy channels.

- Let us discuss each protocol one by one.

##### Protocol 1: Unrestricted simplex protocol

- This protocol is used for noiseless channels, that is, channels that do not introduce any errors or losses in the data frames.
- In this protocol, the sender can send data frames continuously without waiting for any acknowledgment or feedback from the receiver.
- The receiver simply accepts and processes the incoming data frames.
- This protocol has no error control and no flow control mechanisms.
- This protocol is simple and efficient, but it is not realistic, as most channels are prone to errors and losses.
- This protocol can be represented by the following state diagram:

```
Sender:                        Receiver:

+------+                      +------+
|      |                      |      |
| Send |--------------------->| Recv |
|      |                      |      |
+------+                      +------+
```

##### Protocol 2: Simplex stop-and-wait protocol

- This protocol is used for noisy channels, that is, channels that may introduce errors or losses in the data frames.
- In this protocol, the sender sends one data frame and waits for an acknowledgment (ACK) from the receiver before sending the next data frame.
- The receiver sends an ACK after receiving and processing a data frame correctly.
- If the sender does not receive an ACK within a specified time-out period, it assumes that the data frame or the ACK was lost or corrupted, and retransmits the data frame.
- This protocol has error control but no flow control mechanisms.
- This protocol is reliable but inefficient, as the sender has to wait for each ACK, which reduces the channel utilization and throughput.
- This protocol can be represented by the following state diagram:

```
Sender:                        Receiver:

+------+                      +------+
|      |                      |      |
| Send |--------------------->| Recv |
|      |                      |      |
+------+                      +------+
   ^                            |
   |                            |
   |                            v
   |                          +------+
   |                          |      |
   +--------------------------| Send |
                              | ACK  |
                              |      |
                              +------+
```

##### Protocol 3: Simplex protocol for noisy channels

- This protocol is an improvement over protocol 2, as it introduces a sequence number for each data frame and ACK to avoid the problem of duplicate frames.
- In this protocol, the sender and the receiver agree on a window size of one, that is, the sender can have only one outstanding (unacknowledged) data frame at a time.
- The sender attaches a sequence number (0 or 1) to each data frame and alternates between them for successive frames.
- The receiver checks the sequence number of the incoming data frame and sends an ACK with the same sequence number if the frame is correct and in order.
- The sender expects an ACK with the same sequence number as the data frame it sent. If it receives an ACK with a different sequence number, it discards it and retransmits the data frame.
- This protocol has error control and flow control mechanisms, but the window size of one limits the channel utilization and throughput.
- This protocol can be represented by the following state diagram:

```
Sender:                        Receiver:

+------+                      +------+
|      |                      |      |
| Send |--------------------->| Recv |
| 0    |                      | 0    |
|      |                      |      |
+------+                      +------+
   ^                            |
   |                            |
   |                            v
   |                          +------+
   |                          |      |
   +--------------------------| Send |
                              | ACK  |
                              | 0    |
                              |      |
                              +------+
   |                            |
   |                            |
   v                            |
+------+                      +------+
|      |                      |      |
|

```
