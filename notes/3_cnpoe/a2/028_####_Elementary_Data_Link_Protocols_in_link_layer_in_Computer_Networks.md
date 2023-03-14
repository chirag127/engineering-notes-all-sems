 Here is the content in markdown format on the topic #### Elementary Data Link Protocols in link layer in Computer Networks:

#### Elementary Data Link Protocols in link layer in Computer Networks

The data link layer transforms the physical layer into a reliable link over which to transmit data between network devices. Some of the key protocols at the data link layer are:

- Stop-and-Wait Protocol: In this protocol, the sender sends a frame and waits for an acknowledgement (ACK) from the receiver before sending the next frame. If ACK is not received within a timeout period, the frame is retransmitted. Though simple, efficiency is low as sender has to wait for each ACK.
- Go-Back-N Protocol: The sender can send N frames before expecting an ACK. If an ACK is not received for a frame, all frames sent after the lost frame are retransmitted. Throughput is higher than Stop-and-Wait but window size (N) is limited by buffer size and latency.
- Selective Repeat Protocol: The receiver acknowledges specific frames received rather than just the next expected frame (as in Stop-and-Wait & Go-Back-N). The sender retransmits only the lost frames, leading to higher efficiency. However, the protocol is more complex to implement.

Advantages and disadvantages of the protocols can be compared. Examples and applications in reliable data transfer can be discussed. Mnemonics can be 'STOP and WAIT for ACK', 'Go Back N frames if lost' and 'Selectively REPEAT lost frames' for the 3 protocols respectively. Detailed diagrams and codes can also be included for better understanding. The content aims to be a detailed yet concise study guide on the topic.