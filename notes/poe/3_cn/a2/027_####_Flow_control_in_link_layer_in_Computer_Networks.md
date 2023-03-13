 Here is the content written in markdown format on the topic #### Flow control in link layer in Computer Networks:

#### Flow control in link layer in Computer Networks

The link layer is responsible for controlling the flow of data between two connected nodes to avoid congestion. Following are the main flow control techniques used in the link layer:

1. Stop and Wait ARQ: In this technique, the sender sends a frame and waits for the ACK from the receiver. If ACK is received, it sends the next frame else retransmits the same frame. This is inefficient as sender remains idle waiting for the ACK.
2. Sliding Window Protocol: This overcomes the inefficiency of Stop and Wait ARQ. The sender maintains a window of multiple frames that can be sent without receiving ACK. On receiving ACK, the window slides over and more frames are sent. The window size is adjustable. Popular implementations are HDLC and TCP.
3. Buffering: The receiving node maintains a buffer to hold frames that arrive before they are processed. If the buffer is full, it sends a pause frame to the sender to stop transmission until the buffer has space to accommodate more frames. This is done in Ethernet.

Mnemonics:
- Stop and Wait - Sender waits, then goes
- Sliding Window - Multiple frames slide, no waiting
- Buffering - receive buffer says stop or go

Advantages:
- Prevent congestion and data loss
- Ensure in-order delivery of data
Disadvantages:
- Adds to latency
- Complex to implement

Applications: All data link layer and network layer protocols implement some form of flow control to provide reliable data transfer with minimal loss and congestion.

[Detailed diagrams and examples can be added here for more clarity.]