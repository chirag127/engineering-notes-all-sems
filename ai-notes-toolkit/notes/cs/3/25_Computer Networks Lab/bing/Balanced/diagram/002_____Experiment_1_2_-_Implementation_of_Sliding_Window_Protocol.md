### Experiment 1.2 - Implementation of Sliding Window Protocol

The sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames. The protocol uses a window size that determines how many frames can be sent by the sender before receiving an acknowledgment from the receiver. The window slides along the sequence of frames as the sender and receiver exchange data and acknowledgments.

The sliding window protocol can be implemented in different ways, such as:

- Stop-and-wait: The simplest sliding window protocol, where the sender sends one frame at a time and waits for an acknowledgment before sending the next frame. The window size is one for both the sender and the receiver.
- Go-back-N: The sender can send up to N frames at a time, where N is the window size, but the receiver can only acknowledge the last correctly received frame. If the receiver detects an error in a frame, it discards that frame and all the subsequent frames until it receives the correct frame. The sender then retransmits all the frames from the last acknowledged frame.
- Selective repeat: The sender can send up to N frames at a time, where N is the window size, and the receiver can acknowledge any correctly received frame. The receiver also buffers the out-of-order frames until the missing frames are received. The sender only retransmits the frames that are not acknowledged within a certain time limit.

To implement the sliding window protocol, the following steps are required:

- Define the data frame structure, which should include a sequence number, a data field, and an error detection code (such as checksum or CRC).
- Define the window size for the sender and the receiver, which should be less than or equal to the maximum sequence number.
- Define the timeout value for the sender, which should be longer than the maximum round-trip time between the sender and the receiver.
- Implement the sender logic, which should include the following functions:
  - Send a frame with the next sequence number and start a timer.
  - Wait for an acknowledgment or a timeout event.
  - If an acknowledgment is received, slide the window forward and send the next frame if the window is not empty.
  - If a timeout occurs, retransmit the frame and restart the timer.
- Implement the receiver logic, which should include the following functions:
  - Receive a frame and check for errors using the error detection code.
  - If the frame is error-free and has the expected sequence number, send an acknowledgment and deliver the data to the upper layer.
  - If the frame is error-free but has an unexpected sequence number, send an acknowledgment with the expected sequence number and discard the frame (or buffer it for selective repeat).
  - If the frame has an error, discard it and do not send an acknowledgment (or send a negative acknowledgment for selective repeat).

The following diagram illustrates the sliding window protocol with a window size of 4 for both the sender and the receiver, using the go-back-N method.

![Sliding window protocol diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Sliding_window.svg/1200px-Sliding_window.svg.png)

: Sliding window protocol - Wikipedia
: Sliding Window Protocol - tutorialspoint.com
: What is the sliding window technique and how does it work?
: Sliding Window Protocol | Set 1 (Sender Side) - GeeksforGeeks