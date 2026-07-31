# Elementary Data Link Protocols

- Protocols in the data link layer are designed to perform the basic functions of framing, error control and flow control.
- Framing is the process of dividing bit-streams from the physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control is the process of detecting and correcting errors that may occur during transmission or reception of data frames.
- Flow control is the process of regulating the rate of data transmission between the sender and the receiver to avoid congestion or buffer overflow.
- Elementary data link protocols are classified into three categories, as follows:
  - Protocol 1: Unrestricted simplex protocol
    - This protocol assumes that the sender can send data frames continuously without any feedback from the receiver.
    - The receiver simply accepts and processes the incoming frames.
    - This protocol is suitable for simplex channels where errors are negligible and the receiver can handle any data rate.
  - Protocol 2: Simplex stop-and-wait protocol
    - This protocol assumes that the sender can send only one data frame at a time and must wait for an acknowledgment (ACK) from the receiver before sending the next frame.
    - The receiver sends an ACK after processing each frame and discards any duplicate frames.
    - This protocol is suitable for simplex channels where errors may occur and the receiver has a limited buffer capacity.
  - Protocol 3: Simplex protocol for a noisy channel
    - This protocol assumes that the sender can send only one data frame at a time and must wait for an ACK or a negative acknowledgment (NAK) from the receiver before sending the next frame.
    - The receiver sends an ACK if the frame is received correctly and a NAK if the frame is corrupted or lost.
    - The sender retransmits the frame if it receives a NAK or a timeout occurs.
    - This protocol is suitable for simplex channels where errors are frequent and the receiver has a limited buffer capacity.