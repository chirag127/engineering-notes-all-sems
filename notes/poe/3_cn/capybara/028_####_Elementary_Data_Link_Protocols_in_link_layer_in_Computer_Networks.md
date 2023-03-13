#### Elementary Data Link Protocols in Link Layer in Computer Networks

The link layer is responsible for transferring data between adjacent network nodes. The elementary data link protocols are the simplest form of protocols used in the link layer. Here are some important points to keep in mind about these protocols:

1. The elementary data link protocols provide basic error detection and correction mechanisms for data transmission.

2. There are two types of elementary data link protocols - Stop-and-Wait and Go-Back-N. 

3. Stop-and-Wait protocol is a simple protocol in which the sender sends a single frame and waits for an acknowledgement from the receiver before sending the next frame. This protocol is suitable for low speed and low error rate networks.

4. Go-Back-N protocol is a protocol in which the sender sends multiple frames without waiting for an acknowledgement from the receiver. The receiver sends an acknowledgement for each correctly received frame. If the receiver detects an error in a frame, it discards all subsequent frames and asks the sender to retransmit all frames from the frame with the error onwards. This protocol is suitable for high speed and high error rate networks.

5. The Stop-and-Wait protocol is simpler than the Go-Back-N protocol, but it is less efficient in terms of throughput.

6. To minimize the number of retransmissions, the sender and receiver must agree on the size of the data frames and the size of the acknowledgement frames.

7. The elementary data link protocols are widely used in low-speed networks such as dial-up connections and low-speed wireless networks.

Mnemonic/learning trick:

Stop-and-Wait protocol can be remembered as "stop and wait for acknowledgement", whereas Go-Back-N protocol can be remembered as "go back and retransmit from the frame with an error onwards".