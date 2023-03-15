 Here is the content in markdown format without any external links or emojis and in a formal tone:

#### Elementary Data Link Protocols in link layer in Computer Networks.

1. Stop-and-wait protocol:
- Sender sends one frame, waits for acknowledgment (ACK) from receiver, then sends next frame.
- Used for asynchronous transmission with no buffering.
- vulnerable to corruption of ACK - sender may stall waiting for ACK that will never come.

2. Go-back-N protocol:
- Sender can transmit N frames before waiting for ACK.
- Receiver must send ACK for each correct frame received.
- If ACK is not received, sender retransmits all unacknowledged frames (goes back N).
- More efficient than stop-and-wait but still vulnerable to lost ACKs.

3. Sliding window protocol:
- Sender can transmit more than N frames before waiting for acknowledgment.
- Window size determines how many frames can be sent without waiting for ACK.
- Both sender and receiver maintain a "window" of allowed sequence numbers.
- ACKs "slide" the window by increasing the left boundary.
- More efficient and robust than go-back-N, used in many data link protocols.

The content tries to highlight the key points around the three Elementary Data Link Protocols in a formal tone with points and without any external links or emojis. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.