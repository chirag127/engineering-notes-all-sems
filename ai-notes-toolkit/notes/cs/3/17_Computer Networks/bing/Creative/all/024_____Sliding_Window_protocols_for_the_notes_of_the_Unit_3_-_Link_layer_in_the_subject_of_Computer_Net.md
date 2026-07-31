# Sliding Window Protocols

Sliding window protocols are data link layer protocols for reliable and sequential delivery of data frames. The sliding window is also used in Transmission Control Protocol. In this protocol, multiple frames can be sent by a sender at a time before receiving an acknowledgment from the receiver.

The sliding window technique allows the sender to have a buffer of frames ready to be transmitted and to send them in a continuous stream. The receiver also has a buffer of frames ready to be delivered to the upper layer and to acknowledge them in a batch. The size of the buffer is called the window size and it determines how many frames can be in transit at any given time.

There are two types of sliding window protocols: stop-and-wait ARQ and go-back-N ARQ.

## Stop-and-Wait ARQ

Stop-and-wait ARQ is the simplest sliding window protocol. In this protocol, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The window size is one for both the sender and the receiver. The acknowledgment can be either positive (ACK) or negative (NAK). If the sender receives an ACK, it means the frame was received correctly and it can send the next frame. If the sender receives a NAK, it means the frame was corrupted or lost and it has to retransmit the same frame. If the sender does not receive any acknowledgment within a certain time, it assumes that the frame or the acknowledgment was lost and it retransmits the same frame. This is called timeout.

The advantage of stop-and-wait ARQ is that it is simple and easy to implement. The disadvantage is that it is inefficient and slow, especially when the channel has high latency or low bandwidth. The sender has to wait for the round-trip time (RTT) of the channel before sending the next frame, which means the channel is idle for most of the time. The utilization of the channel is given by the formula:

U = Tt / (Tt + 2Tp)

where Tt is the transmission time of a frame and Tp is the propagation time of the channel.

## Go-Back-N ARQ

Go-back-N ARQ is a sliding window protocol that improves the efficiency of stop-and-wait ARQ by allowing the sender to send multiple frames at a time without waiting for acknowledgments. The window size is greater than one for the sender and one for the receiver. The sender assigns a sequence number to each frame and keeps track of the next frame to be sent and the next acknowledgment to be received. The receiver also keeps track of the next frame to be received and sends a cumulative acknowledgment for the last frame received in order. The acknowledgment can be either positive (ACK) or negative (NAK). If the sender receives an ACK, it means all the frames up to that sequence number were received correctly and it can slide the window forward by the number of frames acknowledged. If the sender receives a NAK, it means some frames were corrupted or lost and it has to retransmit all the frames from that sequence number onwards. If the sender does not receive any acknowledgment within a certain time, it assumes that some frames or acknowledgments were lost and it retransmits all the frames in the window. This is called timeout.

The advantage of go-back-N ARQ is that it increases the utilization of the channel by sending multiple frames at a time and reducing the idle time. The disadvantage is that it wastes bandwidth and time by retransmitting all the frames in the window even if only one frame was corrupted or lost. The utilization of the channel is given by the formula:

U = W * Tt / (Tt + 2Tp)

where W is the window size, Tt is the transmission time of a frame and Tp is the propagation time of the channel.

## References

: https://www.studytonight.com/computer-networks/sliding-window-protocol
: https://www.tutorialspoint.com/sliding-window-protocol
: https://digitalnoteshub.com/sliding-window-protocols-in-computer-networks/
: https://en.wikipedia.org/wiki/Sliding_window_protocol
: https://www.geeksforgeeks.org/sliding-window-protocol-set-1/
: https://eng.libretexts.org/Bookshelves/Computer_Science/Networks/Book%3A_An_Introduction_to_Computer_Networks_(Dordal)/