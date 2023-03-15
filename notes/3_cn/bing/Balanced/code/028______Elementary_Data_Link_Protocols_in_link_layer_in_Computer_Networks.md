#### Elementary Data Link Protocols in link layer in Computer Networks

Protocols in the data link layer are designed so that this layer can perform its basic functions: framing, error control and flow control. Framing is the process of dividing bit-streams from physical layer into data frames whose size ranges from a few hundred to a few thousand bytes. Error control is the process of detecting and correcting errors that may occur during transmission. Flow control is the process of regulating the rate of data transmission between the sender and the receiver.

Elementary data link layer protocols are divided into three different sub categories such as:

- Protocol 1: Unrestricted simplex protocol
- Protocol 2: Simplex stop and wait protocol
- Protocol 3: Simplex protocol for noisy channels

Let us discuss each protocol one by one.

**Protocol 1: Unrestricted simplex protocol**

This protocol assumes that the sender can send data frames continuously without any feedback from the receiver. The receiver simply accepts and processes the incoming frames. This protocol is suitable for applications where the sender has a very low data rate or the receiver has a very high processing speed. However, this protocol does not provide any error control or flow control mechanisms.

**Protocol 2: Simplex stop and wait protocol**

This protocol assumes that the sender can send only one data frame at a time and must wait for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after processing the received frame. This protocol provides error control by using a sequence number for each frame and retransmitting the frame if the acknowledgment is lost or corrupted. This protocol also provides flow control by limiting the sender's data rate to match the receiver's processing speed. However, this protocol has a low efficiency as the sender has to wait for a long time between each frame.

**Protocol 3: Simplex protocol for noisy channels**

This protocol assumes that the sender can send multiple data frames without waiting for acknowledgments, but the receiver can send only negative acknowledgments (NAKs) if it detects an error in a received frame. The sender maintains a window of frames that have been sent but not yet acknowledged. The receiver sends a NAK with the sequence number of the first erroneous frame in the window. The sender then retransmits all the frames from that sequence number onwards. This protocol provides error control by using sequence numbers and NAKs, and flow control by using a window size that adapts to the channel conditions. However, this protocol may suffer from unnecessary retransmissions if the NAKs are lost or corrupted.