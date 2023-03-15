### Sliding Window Protocols

Sliding window protocols are data link layer protocols for reliable and sequential delivery of data frames. They are also used in the Transmission Control Protocol (TCP) for flow control and congestion control. The sliding window technique allows the sender to send multiple frames at a time before receiving any acknowledgment from the receiver. The receiver uses the sequence number of each frame to detect any missing or duplicate frames and to reorder them if necessary. The sender and the receiver maintain a window of frames that indicates which frames are expected to be sent or received next. The window size is determined by the available buffer space and the bandwidth-delay product of the channel.

There are two types of sliding window protocols: stop-and-wait ARQ and go-back-N ARQ.

- Stop-and-wait ARQ: In this protocol, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The window size is one for both the sender and the receiver. This protocol is simple but inefficient, as it wastes the channel capacity during the waiting time. The throughput of this protocol is limited by the round-trip time (RTT) of the channel. The sender can send at most one frame per RTT.  

- Go-back-N ARQ: In this protocol, the sender can send up to N frames at a time, where N is the window size of the sender. The receiver has a window size of one and sends a cumulative acknowledgment for the last correctly received frame. If the receiver detects a missing or erroneous frame, it discards all the subsequent frames and sends a negative acknowledgment (NAK) for the missing frame. The sender, upon receiving a NAK or a timeout, retransmits all the frames from the missing frame onwards. This protocol is more efficient than stop-and-wait ARQ, as it utilizes the channel capacity better. However, it may cause unnecessary retransmissions if the channel is noisy or has high latency. The throughput of this protocol depends on the window size and the error rate of the channel.   

- Selective repeat ARQ: In this protocol, the sender can send up to N frames at a time, where N is the window size of the sender. The receiver has a window size of M, where M <= N, and sends a selective acknowledgment (SACK) for each correctly received frame. If the receiver detects a missing or erroneous frame, it buffers all the subsequent frames and sends a NAK for the missing frame. The sender, upon receiving a NAK or a timeout, retransmits only the missing frame. This protocol is more efficient than go-back-N ARQ, as it avoids unnecessary retransmissions and preserves the order of the frames. However, it requires more buffer space and complexity at both the sender and the receiver. The throughput of this protocol depends on the window size, the error rate, and the latency of the channel.   

: https://www.studytonight.com/computer-networks/sliding-window-protocol
: https://www.tutorialspoint.com/sliding-window-protocol
: https://digitalnoteshub.com/sliding-window-protocols-in-computer-networks/
: https://en.wikipedia.org/wiki/Sliding_window_protocol
: https://www.geeksforgeeks.org/sliding-window-protocol-set-1/
: https://eng.libretexts.org/Bookshelves/Computer_Science/Networks/Book%3A_An_Introduction_to_Computer_Networks_(Dordal)/06%3A_Abstract_Sliding_Windows/6.02%3A_Sliding_Windows