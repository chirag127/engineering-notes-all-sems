### Elementary Data Link Protocols

Data link layer is responsible for the reliable transfer of data frames between adjacent nodes over a physical link. The elementary data link protocols are the basic building blocks of data link layer protocols that ensure reliable data transfer.

Here are some of the elementary data link protocols:

1. Stop-and-Wait Protocol
- In this protocol, the sender sends a single frame and waits for an acknowledgment from the receiver before sending the next frame.
- The receiver sends an acknowledgment frame to the sender after receiving the frame successfully.
- If the sender does not receive an acknowledgment frame within a specified time, it retransmits the same frame.
- This protocol has a low efficiency and is not suitable for high-speed networks.

2. Go-Back-N Protocol
- In this protocol, the sender sends a sequence of frames without waiting for an acknowledgment after each frame.
- The receiver sends an acknowledgment frame for the last correctly received frame.
- If the sender does not receive an acknowledgment frame for a certain number of frames, it retransmits all the frames starting from the one that was not acknowledged.
- This protocol supports high-speed networks but has higher overhead due to the need for storing multiple frames.

3. Selective Repeat Protocol
- In this protocol, the sender sends a sequence of frames without waiting for an acknowledgment after each frame.
- The receiver sends an acknowledgment frame for each correctly received frame.
- If the sender does not receive an acknowledgment frame for a certain frame, it retransmits only that particular frame, instead of retransmitting all the frames from that point.
- This protocol is suitable for high-speed networks and has a lower overhead than the Go-Back-N protocol.

These elementary data link protocols play a crucial role in ensuring reliable data transfer between adjacent nodes over a physical link. Understanding these protocols is essential for designing and implementing efficient data link layer protocols in computer networks.