### Experiment 1.2 - Implementation of Sliding Window Protocol

The sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames. The protocol uses a window size that determines how many frames can be sent by the sender before receiving an acknowledgment from the receiver. The window size can vary depending on the protocol and the network conditions. The protocol also requires the receiver to send acknowledgments for the received frames, and allows the sender to retransmit the lost or corrupted frames.

The sliding window protocol can be implemented in different ways, such as:

- Stop-and-wait: The simplest sliding window protocol, where the sender sends one frame at a time and waits for the acknowledgment before sending the next frame. The window size is one for both the sender and the receiver.
- Go-back-N: The sliding window protocol where the sender can send multiple frames (up to the window size) without waiting for the acknowledgments, but the receiver can only send a cumulative acknowledgment for the last correctly received frame. If the sender does not receive an acknowledgment within a certain time, it retransmits all the frames from the last acknowledged frame. The window size for the sender is greater than one, but the window size for the receiver is one .
- Selective repeat: The sliding window protocol where the sender can send multiple frames (up to the window size) without waiting for the acknowledgments, and the receiver can send individual acknowledgments for each frame. The sender only retransmits the frames that are not acknowledged or are corrupted. The window size for both the sender and the receiver is greater than one .

To implement the sliding window protocol, the following steps are required:

- Define the window size for the sender and the receiver, and the sequence number range for the frames.
- Initialize the sender and the receiver windows, and the sequence numbers for the frames.
- Simulate the data transmission process, where the sender sends frames within its window, the receiver receives frames and sends acknowledgments, and the sender updates its window based on the acknowledgments and retransmits the lost or corrupted frames.
- Record the performance metrics, such as the throughput, the delay, the efficiency, and the error rate of the protocol.

The following code block shows a possible pseudocode for implementing the sliding window protocol:

```python
# Define the window size, the sequence number range, and the error rate
window_size = 4
seq_num_range = 8
error_rate = 0.1

# Initialize the sender and the receiver windows, and the sequence numbers
sender_window = []
receiver_window = []
sender_seq_num = 0
receiver_seq_num = 0

# Define a function to simulate the transmission of a frame
def transmit_frame(frame):
  # Simulate a random error in the frame
  if random() < error_rate:
    frame.error = True
  # Simulate a random delay in the frame
  frame.delay = random() * 10
  # Send the frame to the receiver
  receiver_window.append(frame)

# Define a function to simulate the reception of a frame
def receive_frame(frame):
  # Check if the frame has an error
  if frame.error:
    # Discard the frame and do not send an acknowledgment
    return
  # Check if the frame has the expected sequence number
  if frame.seq_num == receiver_seq_num:
    # Process the frame and send an acknowledgment
    process(frame)
    send_ack(frame)
    # Update the receiver sequence number and window
    receiver_seq_num = (receiver_seq_num + 1) % seq_num_range
    receiver_window.remove(frame)
  # Check if the frame is within the receiver window
  elif frame.seq_num in receiver_window:
    # Resend the acknowledgment for the frame
    send_ack(frame)

# Define a function to simulate the sending of an acknowledgment
def send_ack(frame):
  # Create an acknowledgment with the same sequence number as the frame
  ack = Ack(frame.seq_num)
  # Simulate a random delay in the acknowledgment
  ack.delay = random() * 10
  # Send the acknowledgment to the sender
  sender_window.append(ack)

# Define a function to simulate the reception of an acknowledgment
def receive_ack(ack):
  # Check if the acknowledgment is within the sender window
  if ack.seq_num in sender_window:
    # Update the sender window
    sender_window.remove(ack.seq_num)
    # Check if the acknowledgment is for the first frame in

```
