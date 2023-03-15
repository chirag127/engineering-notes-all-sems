#### Flow control in link layer in Computer Networks

Flow control is a technique that allows two stations working at different speeds to communicate with each other. It is a set of measures taken to regulate the amount of data that a sender can send so that a fast sender does not overwhelm a slow receiver.

In data link layer, flow control restricts the number of frames the sender can send before it waits for an acknowledgment from the receiver. Approaches of flow control can be broadly classified into two categories:

- Stop-and-wait: The sender sends one frame and waits for an acknowledgment from the receiver before sending the next frame. This method is simple but inefficient, as the sender has to wait for the round-trip time of each frame.
- Sliding window: The sender can send multiple frames without waiting for an acknowledgment, but it has to keep track of a window size that indicates how many frames can be sent at a time. The window size can be fixed or variable, depending on the protocol. This method is more efficient and can utilize the channel capacity better.

Here is a pseudocode example of a sliding window protocol with a fixed window size of 4:

```
# Sender side
window_size = 4
next_frame_to_send = 0
last_ack_received = -1
while (true) {
  # Send up to window_size frames
  while (next_frame_to_send < last_ack_received + window_size) {
    send_frame(next_frame_to_send)
    next_frame_to_send++
  }
  # Wait for an acknowledgment or a timeout
  event = wait_for_event()
  if (event == ACK) {
    # Update the last_ack_received
    last_ack_received = get_ack_number()
  } else if (event == TIMEOUT) {
    # Resend all frames in the window
    next_frame_to_send = last_ack_received + 1
  }
}

# Receiver side
window_size = 4
expected_frame = 0
while (true) {
  # Receive a frame
  frame = receive_frame()
  if (frame.number == expected_frame) {
    # Deliver the frame to the upper layer
    deliver_data(frame.data)
    # Send an acknowledgment
    send_ack(frame.number)
    # Update the expected_frame
    expected_frame++
  } else {
    # Discard the frame and resend the last acknowledgment
    send_ack(expected_frame - 1)
  }
}
```