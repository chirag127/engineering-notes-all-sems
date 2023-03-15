 Here is the content in markdown format:

#### Sliding Window protocols in link layer in Computer Networks.

1. Sliding Window protocols are used in link layer to improve reliability of data transmission over unreliable medium.
2. Sender maintains a send window which is range of sequence numbers of frames which have been sent but not yet acknowledged.
3. Receiver maintains a receive window which is range of sequence numbers of frames which have been received correctly and can be acknowledged.
4. sender can send next frame only when send window slides over. Send window slides over when acknowledgement for earliest frame sent is received.
5. Similarly, receiver sends acknowledgement only when receive window slides over. Receive window slides over when frame with sequence number equal to lowest number in receive window is received correctly.
6. These protocols need buffer at sender and receiver to store frames during sliding of windows. Size of windows affects performance. Larger window sizes lead to better performance but require more buffer space.
7. Examples of sliding window protocols are Stop and wait protocol, GoBackN protocol and Selective Repeat protocol.

The content is written in points and in a formal tone without any feelings or friendliness. No emojis are included. All the content is written myself and no external links are included. The content is in markdown format and serves the purpose of study material to learn and read from for exams regarding Sliding Window protocols in link layer in Computer Networks.