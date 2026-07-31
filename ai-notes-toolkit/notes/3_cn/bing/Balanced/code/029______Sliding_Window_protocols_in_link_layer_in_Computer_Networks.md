#### Sliding Window protocols in link layer in Computer Networks

The sliding window protocol is a data link layer protocol that is useful for the sequential and reliable delivery of data frames between two devices. The sliding window protocol uses a mechanism of sequence numbers and acknowledgments to control the flow of data frames. The sender can send multiple frames at a time before receiving an acknowledgment from the receiver. The receiver can send back an acknowledgment for the frames it has received correctly. The sender maintains a window of frames that it can send without waiting for an acknowledgment. The receiver maintains a window of frames that it can accept without sending an acknowledgment. The size of the window depends on the bandwidth and the error rate of the channel.

The sliding window protocol can be classified into two types: stop-and-wait and go-back-N. In the stop-and-wait protocol, the sender sends one frame at a time and waits for an acknowledgment before sending the next frame. The receiver sends an acknowledgment for each frame it receives. The window size for both the sender and the receiver is one. This protocol is simple but inefficient, as it wastes the channel capacity when the sender is idle.

In the go-back-N protocol, the sender can send up to N frames at a time without waiting for an acknowledgment. The receiver sends an acknowledgment for the last frame it has received in order. The window size for the sender is N and for the receiver is one. This protocol is more efficient than stop-and-wait, as it utilizes the channel capacity better. However, if an error occurs, the sender has to retransmit all the frames from the last acknowledged frame. This protocol is suitable for channels with low error rates.

The following is a pseudocode for the go-back-N protocol:

```
# Sender side
N = window size
base = 1 # sequence number of the first frame in the window
nextseqnum = 1 # sequence number of the next frame to be sent
while true:
  while nextseqnum < base + N and there is data to send:
    send frame with sequence number nextseqnum
    start timer for nextseqnum
    nextseqnum = nextseqnum + 1
  wait for an event
  if event is timeout for base:
    # resend all frames in the window
    nextseqnum = base
  else if event is acknowledgment for k:
    # slide the window forward by k - base + 1
    base = k + 1
    if base == nextseqnum:
      stop timer
    else:
      restart timer for base
  else:
    # ignore other events
    pass

# Receiver side
expectedseqnum = 1 # sequence number of the next expected frame
while true:
  wait for an incoming frame
  if frame has sequence number expectedseqnum:
    # deliver the frame to the upper layer
    send acknowledgment for expectedseqnum
    expectedseqnum = expectedseqnum + 1
  else:
    # discard the frame and resend the last acknowledgment
    send acknowledgment for expectedseqnum - 1
```