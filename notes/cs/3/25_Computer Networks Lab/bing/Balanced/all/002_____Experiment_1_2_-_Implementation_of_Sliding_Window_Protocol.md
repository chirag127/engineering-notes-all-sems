# Experiment 1.2 - Implementation of Sliding Window Protocol

## Objective
- To understand the concept of sliding window protocol and its types.
- To implement sliding window protocol using Python programming language.
- To simulate the transmission and reception of data frames using sliding window protocol.

## Theory
- Sliding window protocol is a method of flow control and error control for reliable data transmission in computer networks.
- It allows the sender to send multiple data frames before waiting for an acknowledgment from the receiver.
- It also allows the receiver to accept multiple data frames before sending an acknowledgment to the sender.
- The sender and the receiver maintain a window of frames that can be sent or received at any time. The window size is determined by the available buffer space and the bandwidth of the channel.
- The window slides along the sequence of frames as the sender transmits new frames and the receiver acknowledges them.
- There are two types of sliding window protocol: stop-and-wait and go-back-N.

### Stop-and-wait
- In stop-and-wait protocol, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- The receiver sends an acknowledgment for each frame it receives.
- The sender and the receiver have a window size of one frame.
- The advantage of stop-and-wait protocol is its simplicity and reliability.
- The disadvantage of stop-and-wait protocol is its low efficiency and utilization of the channel, as the sender has to wait for a round-trip time (RTT) between each frame transmission.

### Go-back-N
- In go-back-N protocol, the sender can send up to N frames at a time without waiting for an acknowledgment from the receiver, where N is the window size.
- The receiver sends an acknowledgment for the last frame it receives in order, and discards any out-of-order frames.
- The sender maintains a timer for each frame it sends. If the timer expires before receiving an acknowledgment, the sender assumes that the frame or the acknowledgment is lost, and retransmits all the frames from the last acknowledged frame.
- The advantage of go-back-N protocol is its higher efficiency and utilization of the channel, as the sender can send multiple frames in a burst.
- The disadvantage of go-back-N protocol is its higher complexity and overhead, as the sender and the receiver have to maintain a larger window size and handle retransmissions.

## Implementation
- To implement sliding window protocol using Python, we need to use the following modules:
  - socket: to create and manage sockets for communication between the sender and the receiver.
  - threading: to create and manage threads for concurrent execution of the sender and the receiver functions.
  - random: to generate random numbers for simulating frame loss and corruption.
  - time: to measure and control the time intervals for frame transmission and acknowledgment.
- We also need to define the following constants and variables:
  - MAX_SEQ: the maximum sequence number of a frame, which is 7 in this experiment.
  - FRAME_SIZE: the size of a frame in bytes, which is 4 in this experiment.
  - WINDOW_SIZE: the size of the sliding window, which is 4 in this experiment.
  - TIMEOUT: the timeout interval for a frame in seconds, which is 5 in this experiment.
  - LOSS_PROB: the probability of frame loss in the channel, which is 0.1 in this experiment.
  - CORRUPT_PROB: the probability of frame corruption in the channel, which is 0.1 in this experiment.
  - sender_socket: the socket object for the sender.
  - receiver_socket: the socket object for the receiver.
  - sender_address: the address tuple for the sender, which is ('localhost', 8000) in this experiment.
  - receiver_address: the address tuple for the receiver, which is ('localhost', 8001) in this experiment.
  - data: the list of data frames to be sent by the sender, which is ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111'] in this experiment.
  - ack: the list of acknowledgment frames to be sent by the receiver, which is ['ACK0', 'ACK1', 'ACK2', 'ACK3', 'ACK4', 'ACK5', 'ACK6', 'ACK7'] in this experiment.
  - next_frame_to_send: the sequence number of the next frame to be sent by the sender, initialized to 0.
  - frame_expected: the sequence number of the next frame expected by the receiver, initialized to 0.
  - buffer: the list of frames buffered by the receiver, initialized to an empty list.
  - timer