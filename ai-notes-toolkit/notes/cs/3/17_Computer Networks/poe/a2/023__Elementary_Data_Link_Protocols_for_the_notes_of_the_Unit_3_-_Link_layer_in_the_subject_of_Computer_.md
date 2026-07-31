 Here is the content in markdown format without any emojis or external links:

### Elementary Data Link Protocols

- Stop-and-wait protocol: The sender sends a frame and waits for an acknowledgement (ACK) from the receiver before sending the next frame. If ACK is not received within a timeout period, the frame is retransmitted.
- Go-back-N protocol: The sender can send up to N frames before waiting for an ACK. If an ACK is not received for a frame, all unacknowledged frames are retransmitted.
- Selective reject protocol: The receiver sends a selective reject (SREJ) for the missed or corrupted frames. Only the missed/corrupted frames are retransmitted instead of all the unacknowledged frames.

The key features of data link protocols are:

- Framing: The protocol encapsulates the network layer packet into frames and includes additional header information for delivery.
- Addressing: Source and destination addresses are added to identify the sender and receiver.
- Error detection and correction: Detection of errors can be done using parity checks or cyclic redundancy checks (CRC). Correction can be done using forward error correction (FEC) codes.
- Flow and congestion control: The rate of transmission is controlled to avoid congestion in the network.
- Multiple access control: Protocols coordinate the access of multiple devices to the shared medium.

The goal of data link protocols is to provide reliable data transmission over the physical layer. Efficiency and performance can be improved by incorporating features like piggybacking acknowledgements and frame sequencing.