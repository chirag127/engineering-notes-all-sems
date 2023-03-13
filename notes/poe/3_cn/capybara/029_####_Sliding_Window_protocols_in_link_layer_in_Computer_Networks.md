#### Sliding Window Protocols in Link Layer in Computer Networks

Sliding Window Protocols are used in Link Layer of Computer Networks to provide flow control and error control mechanisms. These protocols allow the sender to transmit multiple frames before receiving an acknowledgement from the receiver. The receiver maintains a window of acceptable frames and sends acknowledgement for only those frames which are within the window.

There are two types of Sliding Window Protocols - Go-Back-N and Selective Repeat. Let's understand them in detail.

##### Go-Back-N Protocol

In Go-Back-N Protocol, the sender can transmit multiple frames before receiving an acknowledgement from the receiver. The receiver maintains a window of acceptable frames and sends acknowledgement for only those frames which are within the window. If the receiver receives a frame with an out-of-sequence number, it discards that frame and all subsequent frames until it receives the frame with the correct sequence number. The sender maintains a timer for each frame it transmits. If it doesn't receive an acknowledgement for a frame within the timer limit, it retransmits all frames starting from that frame.

##### Selective Repeat Protocol

In Selective Repeat Protocol, the sender can transmit multiple frames before receiving an acknowledgement from the receiver. The receiver maintains a window of acceptable frames and sends acknowledgement for only those frames which are within the window. If the receiver receives a frame with an out-of-sequence number, it doesn't discard that frame. Instead, it stores that frame in its buffer and sends the acknowledgement for the last correctly received frame. The sender maintains a timer for each frame it transmits. If it doesn't receive an acknowledgement for a frame within the timer limit, it retransmits only that particular frame.

##### Advantages of Sliding Window Protocols

- Provides flow control and error control mechanisms
- Increases the efficiency of data transmission
- Reduces the number of retransmissions

##### Disadvantages of Sliding Window Protocols

- Increases the complexity of the protocol
- Requires additional memory and processing power at both sender and receiver

##### Learning Tricks and Mnemonics

There aren't any widely known Mnemonics or learning tricks for Sliding Window Protocols. However, students can create their own Mnemonics or use some common ones like "Go Back and Repeat" for Go-Back-N Protocol or "Selective Storage" for Selective Repeat Protocol to remember the basic concepts of these protocols.