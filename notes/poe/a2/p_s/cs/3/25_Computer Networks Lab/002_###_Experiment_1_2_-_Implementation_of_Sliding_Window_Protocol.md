 Here is the content in markdown format for the topic ### Experiment 1.2 - Implementation of Sliding Window Protocol:

### Experiment 1.2 - Implementation of Sliding Window Protocol

- Sliding Window Protocol is a flow control technique used in computer networking. It allows multiple frames to be transmitted before an acknowledgement is received. This increases efficiency.
- The sender maintains a window which is a range of sequence numbers of frames that can be sent before receiving an acknowledgement. The window slides over the sequence number space as acknowledgements are received.
- The receiver sends acknowledgements for the frames received. The acknowledgements contain the sequence number of the next expected frame. This informs the sender about which frames have been received and which frames can be removed from the window.
- The size of the window depends on the bandwidth-delay product of the network. It should be large enough to keep the network busy but small enough to provide flow control.
- The steps in implementation are:

1. Initialize send and receive sequence number to 0. Initialize send and receive window size.
2. Receiver sends acknowledgement for next expected sequence number.
3. Sender checks if send window is not full. If not full, send frames till window is full. Increment send sequence number for each frame sent.
4. Receiver receives frames and sends acknowledgement for the highest sequence number received.
5. Sender slides window on receiving acknowledgements and removes acknowledged frames from the window.

- Advantages: Increased efficiency due to multiple frames in transit. Handles network delays and variable delays.
- Disadvantages: Complex to implement. Require mechanisms to handle lost or corrupted frames.
- Applications: Used in protocols like TCP to provide reliable data transfer on the Internet.

[Detailed diagrams and examples can be added here to aid understanding]