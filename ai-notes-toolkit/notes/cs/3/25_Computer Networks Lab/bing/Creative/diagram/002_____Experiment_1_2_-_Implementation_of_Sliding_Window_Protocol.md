### Experiment 1.2 - Implementation of Sliding Window Protocol

#### Objective
- To understand the concept and working of sliding window protocol.
- To implement sliding window protocol in a simulated network environment.

#### Theory
- Sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames.
- Sliding window protocol uses a window size to control how many frames can be sent by a sender before receiving an acknowledgment from the receiver.
- The window size is the number of frames that can be in transit at any given time. The window slides along the sequence of frames as the sender and receiver exchange frames and acknowledgments.
- There are two types of sliding window protocol: Go-Back-N ARQ and Selective Repeat ARQ.
- Go-Back-N ARQ allows the sender to send up to N frames without waiting for acknowledgments, but the receiver can only send a cumulative acknowledgment for the last correctly received frame. If a frame is lost or corrupted, the receiver discards all the subsequent frames until the sender retransmits the missing frame. The sender uses a timer to detect the loss of frames and retransmits all the frames from the missing one to the end of the window.
- Selective Repeat ARQ allows the sender to send up to N frames without waiting for acknowledgments, and the receiver can send a selective acknowledgment for each correctly received frame. If a frame is lost or corrupted, the receiver buffers the subsequent frames until the sender retransmits the missing frame. The sender uses a timer for each frame and retransmits only the frames that are not acknowledged.

#### Procedure
- To implement sliding window protocol, we need to simulate a network environment with a sender and a receiver connected by a channel that can introduce errors and delays.
- We can use a programming language such as C or Java to write the code for the sender and the receiver processes, and use sockets or pipes to communicate between them.
- The sender and the receiver processes should follow the algorithm of the sliding window protocol, using variables such as sequence number, window size, buffer size, timer, acknowledgment, etc.
- The sender process should generate frames with random data and send them to the receiver process through the channel, using the sliding window protocol to control the flow and error recovery.
- The receiver process should receive the frames from the channel and send acknowledgments to the sender process, using the sliding window protocol to ensure reliable and sequential delivery.
- The channel should simulate the network conditions by introducing random errors and delays in the transmission of frames and acknowledgments.
- The sender and the receiver processes should print the status of the sliding window protocol, such as the sequence number, window size, buffer size, timer, acknowledgment, etc., for each frame and acknowledgment exchanged.
- The experiment should be repeated for different values of window size, buffer size, error rate, and delay rate, and the performance of the sliding window protocol should be analyzed and compared.