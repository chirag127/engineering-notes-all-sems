### Sliding Window Protocols

- Sliding window protocols are data link layer protocols for reliable and sequential delivery of data frames.
- The sliding window is a technique that allows the sender to send multiple frames at a time before receiving any acknowledgment from the receiver.
- The sliding window is also used in the Transmission Control Protocol (TCP) at the transport layer.
- The sliding window is a variable-sized buffer that slides along the data stream, indicating the range of frames that can be sent or received at any time.
- The sliding window size is determined by the available buffer space at the receiver and the bandwidth-delay product of the channel.
- The sliding window protocols can be classified into two types: stop-and-wait ARQ and sliding window ARQ.
- Stop-and-wait ARQ is a simple protocol that uses a window size of one frame. The sender sends one frame and waits for an acknowledgment from the receiver before sending the next frame.
- Sliding window ARQ is a more efficient protocol that uses a window size of more than one frame. The sender can send multiple frames within the window without waiting for acknowledgments. The receiver can send cumulative or selective acknowledgments to the sender.
- Sliding window ARQ can be further divided into two subtypes: go-back-N ARQ and selective repeat ARQ.
- Go-back-N ARQ is a protocol that uses a cumulative acknowledgment scheme. The receiver sends an acknowledgment for the last correctly received frame and discards any out-of-order frames. The sender maintains a timer for each frame and retransmits all the frames from the last acknowledged frame if the timer expires.
- Selective repeat ARQ is a protocol that uses a selective acknowledgment scheme. The receiver sends an acknowledgment for each correctly received frame and buffers any out-of-order frames. The sender maintains a timer for each frame and retransmits only the lost or corrupted frames if the timer expires.
- Sliding window protocols are used to improve the efficiency and reliability of data transmission in networks with high latency or noisy channels.