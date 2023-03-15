

#### Sliding Window protocols in link layer in Computer Networks

1. Sliding Window protocols are used to control the flow of data in the link layer of a computer network.

2. The window size is a parameter that determines the number of frames that can be sent before an acknowledgement is received.

3. The sender maintains a window of frames that it can send before needing to wait for an acknowledgement from the receiver.

4. The receiver also maintains a window of frames that it can receive before needing to send an acknowledgement to the sender.

5. Sliding window protocols can be implemented using either a stop-and-wait protocol or a go-back-N protocol.

6. In a stop-and-wait protocol, the sender sends one frame at a time, waiting for an acknowledgement before sending the next frame.

7. In a go-back-N protocol, the sender sends multiple frames at a time, and the receiver acknowledges all of the frames at once.

8. Sliding window protocols are used to improve the efficiency of the network by reducing the amount of time spent waiting for acknowledgements.