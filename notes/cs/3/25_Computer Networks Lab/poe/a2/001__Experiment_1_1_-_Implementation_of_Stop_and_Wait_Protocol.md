 Here is the formal content in markdown format without any feelings or emojis for the topic - Experiment 1.1 - Implementation of Stop and Wait Protocol:

### Experiment 1.1 - Implementation of Stop and Wait Protocol

1. Stop and Wait is the simplest error control protocol. It uses acknowledgements and timeouts to ensure data delivery.
2. The sender sends one frame and waits for an acknowledgement from the receiver.
3. If ACK is received, the sender sends the next frame.
4. If timeout occurs without receiving ACK, the sender retransmits the same frame.
5. This process continues until all frames are transmitted.
6. The receiver sends ACK for every frame received.
7. Sequence numbers are used to track frames. The sender adds sequence number to each frame. The receiver checks sequence number to detect duplicate frames.
8. Stop and Wait has low utilisation of the link as sender has to wait for ACK before sending next frame.
9. Throughput can be increased using Sliding Window protocol.

The content summarizes the key points about Stop and Wait protocol without any feelings or emojis in a formal tone with points and in Markdown format. Let me know if you would like me to modify or expand the content.