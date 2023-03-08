 Here is the content in markdown format for the given topic:

#### Flow control in link layer in Computer Networks

- Flow control is a technique used in link layer (data link layer) to regulate the rate of data transmission between two nodes to prevent overflow.
- It prevents a fast sender from overwhelming a slow receiver by sending data faster than the receiver can process.
- Methods:
    - Stop and wait: Sender sends a frame and waits for ack from receiver before sending next frame. Effective but low efficiency.
    - Sliding window: Sender can send multiple frames before waiting for acks. Window size determines how many frames can be sent. Provides better efficiency but complex.
    - Credit-based: Receiver specifies amount of buffer space available and sender sends data accordingly. Prevents buffer overflow at receiver.
- Advantages: Prevents data loss due to buffer overflow, ensures reliable data transfer.
- Disadvantages: Additional overhead for acknowledgements and feedback, throughput can be low for small window sizes.
- Applications: Data transfer over point-to-point and shared communication channels.

[Here you can include any diagrams or images if required to explain the concept]

[You can also include examples of protocols or codes implementing flow control at link layer if helpful for learning]

The above content explains the flow control techniques at data link layer with their methods, advantages, disadvantages and applications. Please let me know if you would like me to elaborate on any specific point or add any other relevant details.