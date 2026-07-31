# Experiment 1.2 - Implementation of Sliding Window Protocol

## Objective
The objective of this experiment is to implement and simulate the sliding window protocol, which is a feature of packet-based data transmission protocols. The sliding window protocol is used to ensure reliable and sequential delivery of data frames between a sender and a receiver, as well as to optimize the packet flow and avoid congestion.

## Theory
The sliding window protocol works as follows:

- The sender maintains a window of size `ws` that indicates how many frames it can send before receiving an acknowledgment from the receiver. The window slides forward as the sender receives acknowledgments for the sent frames.
- The receiver maintains a window of size `wr` that indicates how many frames it can receive and buffer before sending an acknowledgment to the sender. The window slides forward as the receiver sends acknowledgments for the received frames.
- Each frame has a sequence number that identifies its position in the data stream. The sequence numbers are modulo `n`, where `n` is the maximum number of frames that can be sent or received without wrapping around. The sequence numbers are used to detect and handle lost, duplicated, or out-of-order frames.
- The sender and the receiver use timers to detect and recover from frame losses. The sender sets a timer for each frame it sends and retransmits the frame if the timer expires before receiving an acknowledgment. The receiver sets a timer for each frame it expects and sends a negative acknowledgment (NAK) if the timer expires before receiving the frame.

There are different variants of the sliding window protocol, such as stop-and-wait, go-back-N, and selective repeat, that differ in how they handle frame losses and acknowledgments.

- Stop-and-wait: This is the simplest sliding window protocol, where `ws = wr = 1`. The sender sends one frame at a time and waits for an acknowledgment before sending the next frame. The receiver sends an acknowledgment for each frame it receives. This protocol is inefficient as it does not utilize the full bandwidth of the channel.
- Go-back-N: This is a sliding window protocol where `ws > 1` and `wr = 1`. The sender can send multiple frames at a time without waiting for acknowledgments, but it must keep a copy of each frame in case of retransmission. The receiver sends an acknowledgment for the last correctly received frame in sequence, and discards any out-of-order frames. The sender retransmits all the frames from the last acknowledged frame to the current frame if it receives a NAK or a timeout. This protocol is more efficient than stop-and-wait, but it may waste bandwidth by retransmitting frames that have already been received by the receiver.
- Selective repeat: This is a sliding window protocol where `ws > 1` and `wr > 1`. The sender can send multiple frames at a time without waiting for acknowledgments, but it must keep a copy of each frame in case of retransmission. The receiver can receive and buffer multiple frames out of order, and sends an acknowledgment for each frame it receives. The sender retransmits only the frames that have not been acknowledged by the receiver. This protocol is the most efficient among the sliding window protocols, but it requires more buffer space and complexity at both the sender and the receiver.

## Procedure
The procedure for implementing the sliding window protocol is as follows:

- Define the parameters of the protocol, such as `ws`, `wr`, `n`, and the frame size.
- Create a sender and a receiver process that communicate through a shared channel.
- Implement the sender process as follows:
  - Initialize a variable `sn` to store the sequence number of the next frame to be sent.
  - Initialize a variable `sf` to store the sequence number of the first frame in the window.
  - Initialize a variable `sl` to store the sequence number of the last frame in the window.
  - Initialize an array `buffer` to store the frames to be sent.
  - Initialize an array `timer` to store the timers for each frame in the window.
  - Repeat the following steps until all the data is sent:
    - If the window is not full and there is data to be sent, generate a frame with the sequence number `sn` and the data, and store it in the `buffer`.
    - Send the frame in the `buffer` with the sequence number `sn` to the channel, and start the timer for that frame.
    - Increment `sn` by 1 modulo `n`, and update `sl` accordingly.
    - Wait for an acknowledgment or a timeout from the channel.
    -