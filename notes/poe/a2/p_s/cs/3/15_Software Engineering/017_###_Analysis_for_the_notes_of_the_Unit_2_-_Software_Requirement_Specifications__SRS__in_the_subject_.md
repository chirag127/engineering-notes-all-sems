 Here is the content in markdown format for the topic -

#### Elementary Data Link Protocols in link layer in Computer Networks

1. Stop-and-Wait Protocol -
- In this protocol, sender sends a frame and waits for acknowledgement (ACK) from receiver before sending next frame.
- If ACK is not received within timeout period, sender retransmits the same frame.
- Advantage - Simple to implement. Disadvantage - Low efficiency due to waiting for ACK.
- Application - When frames are short and propagation delay is high.

2. Go-Back-N (GBN) Protocol -
- Sender can send N frames before waiting for ACK.
- If ACK for a frame is not received, all frames after the lost one are retransmitted.
- Sequence numbers are used to keep track of frames.
- Advantage - Higher efficiency than Stop and Wait. Disadvantage - Wastage of bandwidth if multiple frames are lost.
- Application - When network is relatively reliable and frame loss is infrequent.

3. Selective Repeat (SR) Protocol -
- Receiver acknowledges each frame individually.
- Sender retransmits only the lost frames.
- Advantage - Efficient as only lost frames are retransmitted. Disadvantage - Complex to implement.
- Application - When network is unreliable and frame loss is frequent.

[Additional details, diagrams, codes, tables, advantages, disadvantages, examples, applications can be included here for better understanding and learning.]