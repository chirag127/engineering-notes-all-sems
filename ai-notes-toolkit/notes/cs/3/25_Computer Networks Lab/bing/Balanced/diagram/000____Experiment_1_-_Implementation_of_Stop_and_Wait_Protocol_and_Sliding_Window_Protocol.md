## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

### Objective
- To understand the basic concepts of flow control and error control in data link layer.
- To implement and compare the performance of stop and wait protocol and sliding window protocol.

### Theory
- Flow control is a mechanism that regulates the amount of data that can be sent by the sender to the receiver, to avoid congestion and buffer overflow.
- Error control is a mechanism that detects and corrects the errors that may occur during data transmission, such as bit errors, frame loss, or duplication.
- Stop and wait protocol is a simple flow control and error control protocol that uses a single buffer at both sender and receiver. The sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after receiving and processing the frame. The sender and receiver use alternating sequence numbers (0 and 1) to distinguish between different frames and acknowledgments.
- Sliding window protocol is an advanced flow control and error control protocol that uses multiple buffers at both sender and receiver. The sender can send multiple frames without waiting for acknowledgments, as long as the number of unacknowledged frames does not exceed the window size. The receiver can receive and process multiple frames out of order, as long as the number of frames in the buffer does not exceed the window size. The sender and receiver use a range of sequence numbers to identify different frames and acknowledgments.

### Procedure
- To implement the stop and wait protocol, follow these steps:
  - Initialize the sender and receiver buffers with sequence number 0.
  - Generate a random frame and send it to the receiver with sequence number 0.
  - Start a timer and wait for an acknowledgment from the receiver with sequence number 0.
  - If the acknowledgment is received before the timer expires, stop the timer and update the sender buffer with sequence number 1. Go to step 2.
  - If the acknowledgment is not received before the timer expires, resend the frame with sequence number 0. Go to step 3.
  - Repeat steps 2 to 5 until all frames are sent and acknowledged.
  - Initialize the receiver buffer with sequence number 0.
  - Receive a frame from the sender with sequence number 0.
  - Check for errors in the frame. If the frame is error-free, process the frame and send an acknowledgment to the sender with sequence number 0. Update the receiver buffer with sequence number 1. Go to step 9.
  - If the frame is corrupted or lost, discard the frame and do not send any acknowledgment. Go to step 8.
  - Receive a frame from the sender with sequence number 1.
  - Check for errors in the frame. If the frame is error-free, process the frame and send an acknowledgment to the sender with sequence number 1. Update the receiver buffer with sequence number 0. Go to step 8.
  - If the frame is corrupted or lost, discard the frame and do not send any acknowledgment. Go to step 10.
  - Repeat steps 8 to 11 until all frames are received and processed.
- To implement the sliding window protocol, follow these steps:
  - Initialize the sender and receiver buffers with sequence numbers 0 to N-1, where N is the window size.
  - Generate a random frame and send it to the receiver with the next available sequence number in the sender buffer.
  - Start a timer for the frame and update the sender buffer by removing the sequence number of the frame.
  - Repeat steps 2 and 3 until the sender buffer is empty or the window size is reached.
  - Wait for an acknowledgment from the receiver with the sequence number of the oldest frame in the window.
  - If the acknowledgment is received before the timer expires, stop the timer and update the sender buffer by adding the sequence number of the acknowledgment. Go to step 2.
  - If the acknowledgment is not received before the timer expires, resend the frame with the sequence number of the oldest frame in the window. Go to step 5.
  - Repeat steps 2 to 7 until all frames are sent and acknowledged.
  - Initialize the receiver buffer with sequence numbers 0 to N-1, where N is the window size.
  - Receive a frame from the sender with a sequence number within the range of the receiver buffer.
  - Check for errors in the frame. If the frame is error-free, process the frame and send an acknowledgment to the sender with the sequence number of the frame. Update the receiver buffer by removing the sequence number