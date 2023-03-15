Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on elementary data link protocols for the notes of the Unit 3 - Link layer in the subject of Computer Networks.

### Elementary Data Link Protocols

- Protocols in the data link layer are designed so that this layer can perform its basic functions: framing, error control and flow control.
- Framing is the process of dividing bit-streams from physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control is the process of detecting and correcting errors that may occur during transmission or reception of data frames.
- Flow control is the process of regulating the rate of data transmission between the sender and the receiver to avoid congestion or buffer overflow.
- Elementary data link protocols are classified into three categories, as given below:
  - Protocol 1: Unrestricted simplex protocol
  - Protocol 2: Simplex stop and wait protocol
  - Protocol 3: Simplex protocol for a noisy channel

#### Protocol 1: Unrestricted simplex protocol

- This protocol assumes that the sender can send data frames at any time without any restriction.
- The receiver does not send any feedback or acknowledgment to the sender.
- This protocol is suitable for applications where the sender has a very low data rate or the channel is very reliable.
- The main disadvantage of this protocol is that it does not provide any error control or flow control.
- The sender does not know if the receiver has received the data frames correctly or not.
- The receiver does not know if the sender has more data frames to send or not.

#### Protocol 2: Simplex stop and wait protocol

- This protocol assumes that the sender can send only one data frame at a time and must wait for an acknowledgment from the receiver before sending the next data frame.
- The receiver sends an acknowledgment (ACK) to the sender after receiving a data frame correctly.
- The sender uses a timer to detect the loss of acknowledgment and retransmits the data frame if the timer expires.
- This protocol provides error control but not flow control.
- The main disadvantage of this protocol is that it has a low utilization of the channel capacity.
- The sender remains idle for most of the time waiting for the acknowledgment.
- The channel is also idle for the time it takes for the acknowledgment to travel from the receiver to the sender.

#### Protocol 3: Simplex protocol for a noisy channel

- This protocol assumes that the channel is noisy and may corrupt or lose data frames or acknowledgments.
- The sender and the receiver use sequence numbers to identify and order the data frames.
- The sender sends a data frame with a sequence number and waits for an acknowledgment with the same sequence number.
- The receiver sends an acknowledgment with the sequence number of the last correctly received data frame.
- The sender uses a timer to detect the loss of acknowledgment or data frame and retransmits the data frame if the timer expires.
- The receiver uses a buffer to store the out-of-order data frames and delivers them to the upper layer in order.
- This protocol provides both error control and flow control.
- The main disadvantage of this protocol is that it still has a low utilization of the channel capacity.
- The sender and the receiver can send or receive only one data frame at a time.
- The channel is also idle for the time it takes for the acknowledgment or data frame to travel from one end to the other.