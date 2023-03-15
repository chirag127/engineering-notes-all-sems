### Elementary Data Link Protocols

1. **Simplex Stop-and-Wait Protocol**: This protocol is used for error-free channels. The sender sends a frame and waits for an acknowledgement from the receiver before sending the next frame.
2. **Simplex Protocol for a Noisy Channel**: This protocol is used for channels with errors. The sender sends a frame and waits for an acknowledgement from the receiver. If the acknowledgement is not received within a certain time, the sender retransmits the frame.
3. **Sliding Window Protocol**: This protocol is used to improve the efficiency of the Simplex Stop-and-Wait Protocol. The sender can send multiple frames before waiting for an acknowledgement from the receiver. The number of frames that can be sent is determined by the window size.
4. **Go-Back-N ARQ**: This protocol is a type of sliding window protocol. If an error is detected in a frame, the receiver discards all subsequent frames and requests the retransmission of the erroneous frame. The sender then retransmits the erroneous frame and all subsequent frames.
5. **Selective Repeat ARQ**: This protocol is also a type of sliding window protocol. If an error is detected in a frame, the receiver only requests the retransmission of the erroneous frame. The sender then retransmits only the erroneous frame.
