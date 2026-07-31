#### Elementary Data Link Protocols in link layer in Computer Networks

Elementary Data Link Protocols are protocols that are designed to perform the basic functions of the data link layer, such as framing, error control and flow control. Framing is the process of dividing bit-streams from the physical layer into data frames whose size ranges from a few hundred to a few thousand bytes. Error control is the process of detecting and correcting errors that may occur during transmission. Flow control is the process of regulating the rate of data transmission between the sender and the receiver.

There are three types of elementary data link protocols, depending on the characteristics of the channel and the requirements of the application :

- Protocol 1: Unrestricted Simplex Protocol. This protocol is used for noiseless channels, where no errors or losses can occur. It is also known as the Simplest Protocol. In this protocol, the sender sends data frames continuously without waiting for any acknowledgment from the receiver. The receiver simply accepts and processes the frames. There is no error control or flow control in this protocol.
- Protocol 2: Simplex Stop-and-Wait Protocol. This protocol is used for noisy channels, where errors or losses can occur, but the channel is simplex, meaning that data can only flow in one direction. In this protocol, the sender sends one data frame and waits for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after receiving and processing a frame. If the sender does not receive an acknowledgment within a certain time, it retransmits the frame. This protocol provides error control but not flow control.
- Protocol 3: Simplex Protocol for Noisy Channels. This protocol is used for noisy channels, where errors or losses can occur, and the channel is duplex, meaning that data can flow in both directions. In this protocol, the sender and the receiver use sequence numbers to identify and order the frames. The sender sends one data frame with a sequence number and waits for an acknowledgment with the same sequence number from the receiver before sending the next frame. The receiver sends an acknowledgment with the sequence number of the last correctly received frame. If the sender does not receive an acknowledgment with the expected sequence number within a certain time, it retransmits the frame. This protocol provides both error control and flow control.

The following is a pseudocode for the sender and the receiver of Protocol 3:

```
# Sender
seq = 0 # sequence number of the frame to be sent
while (true) {
  frame = make_frame(data, seq) # create a frame with data and sequence number
  send(frame) # send the frame
  start_timer() # start a timer
  while (true) {
    wait_for_event() # wait for an event
    if (event == frame_arrival) { # a frame has arrived
      ack = receive() # receive the frame
      if (ack.seq == seq) { # the acknowledgment has the expected sequence number
        stop_timer() # stop the timer
        seq = 1 - seq # toggle the sequence number
        break # exit the inner loop
      }
    }
    else if (event == timeout) { # the timer has expired
      send(frame) # resend the frame
      start_timer() # restart the timer
    }
  }
}

# Receiver
seq = 0 # sequence number of the frame to be received
while (true) {
  wait_for_event() # wait for an event
  if (event == frame_arrival) { # a frame has arrived
    frame = receive() # receive the frame
    if (frame.seq == seq) { # the frame has the expected sequence number
      data = extract_data(frame) # extract the data from the frame
      process_data(data) # process the data
      seq = 1 - seq # toggle the sequence number
    }
    ack = make_frame(empty, seq) # create an acknowledgment with the sequence number
    send(ack) # send the acknowledgment
  }
}
```