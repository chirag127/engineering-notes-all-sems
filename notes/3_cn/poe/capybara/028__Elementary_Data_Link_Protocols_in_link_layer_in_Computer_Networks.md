#### Elementary Data Link Protocols in Link Layer in Computer Networks

Elementary Data Link Protocols are the fundamental protocols used in the link layer of Computer Networks. These protocols are responsible for establishing a reliable communication channel between two devices connected through a physical medium. In this section, we will discuss some of the elementary data link protocols used in the link layer.

1. Stop-and-Wait Protocol:
   - It is a simple protocol where the sender sends a data frame and waits for an acknowledgment from the receiver before sending the next frame.
   - The receiver sends an acknowledgment frame to the sender after receiving a data frame.
   - If the sender does not receive an acknowledgment within a specified time, it retransmits the frame.

2. Go-Back-N Protocol:
   - This protocol allows the sender to transmit multiple frames without waiting for an acknowledgment for each frame.
   - The receiver sends an acknowledgment for the last frame received and all the previous frames.
   - If the sender does not receive an acknowledgment for a frame, it retransmits all the frames starting from the unacknowledged frame.

3. Selective Repeat Protocol:
   - This protocol is an improvement over the Go-Back-N protocol.
   - The receiver sends an acknowledgment for each received frame, and the sender maintains a window of frames that can be transmitted.
   - If the sender does not receive an acknowledgment for a frame, it retransmits only that frame instead of retransmitting all the frames.

4. High-Level Data Link Control (HDLC) Protocol:
   - It is a widely used protocol for data transfer in the link layer.
   - It provides a reliable communication channel between two devices.
   - It supports three types of frames: Information frames, Supervisory frames, and Unnumbered frames.
   
These elementary data link protocols play a crucial role in ensuring a reliable and efficient communication channel between two devices. Understanding the working of these protocols is essential for anyone working in the field of Computer Networks.