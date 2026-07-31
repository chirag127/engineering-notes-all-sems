### Elementary Data Link Protocols

- Protocols in the data link layer are designed to perform the basic functions of framing, error control and flow control.
- Framing is the process of dividing bit-streams from the physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control is the process of detecting and correcting errors that may occur during transmission or reception of data frames.
- Flow control is the process of regulating the rate of data transmission between the sender and the receiver to avoid congestion or buffer overflow.
- Elementary data link protocols are classified into three categories, as follows:
  - Protocol 1: Unrestricted simplex protocol
    - This protocol assumes that the sender can send data frames continuously without any feedback from the receiver.
    - This protocol is suitable for simplex channels where the receiver can handle any amount of data without errors.
    - This protocol does not provide any error control or flow control mechanisms.
  - Protocol 2: Simplex stop-and-wait protocol
    - This protocol assumes that the sender can send only one data frame at a time and must wait for an acknowledgment (ACK) from the receiver before sending the next frame.
    - This protocol is suitable for simplex channels where the receiver may need some time to process the received frame or may encounter errors.
    - This protocol provides error control by using ACKs and timeouts, and flow control by using stop-and-wait mechanism.
  - Protocol 3: Simplex protocol for a noisy channel
    - This protocol assumes that the sender can send only one data frame at a time and must wait for a positive acknowledgment (ACK) or a negative acknowledgment (NAK) from the receiver before sending the next frame.
    - This protocol is suitable for simplex channels where the receiver may encounter errors frequently or may lose frames.
    - This protocol provides error control by using ACKs, NAKs and timeouts, and flow control by using stop-and-wait mechanism.
    - This protocol also uses sequence numbers to identify and discard duplicate frames.