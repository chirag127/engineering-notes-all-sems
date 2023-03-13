 Here is the content on ### Window management in transport layer in markdown format:

### Window management in transport layer

The transport layer manages the amount of data that can be exchanged between two hosts at a time. This is known as window management and helps in controlling congestion and flow control.

- **Congestion control**: Prevents a fast sender from overwhelming a slow receiver by limiting the amount of data in transit. The sender should not send more data than the receiver can handle. This is achieved using windows and acknowledgements. If the receiver is getting overwhelmed, it can send a smaller window size. Upon receiving a smaller window size, the sender reduces its sending rate.
- **Flow control**: Prevents a fast sender from overflowing the receiver's input buffer. The receiver advertises a window size which limits the amount of data that can be in transit at a time. The sender cannot send more data than the advertised window size. Upon receiving and processing some data, the receiver can increase the window size to allow more data to be sent.

** Mnemonics: **
Think of congestion control as traffic regulation to prevent JAM while flow control is preventing the pipe from overflowing.

** Advantages: **
- Prevents overwhelming the receiver and dropping packets
- Provides reliable data transfer using sequence and acknowledgement numbers along with window management

** Examples: **
- TCP uses a sliding window protocol for congestion and flow control
- Selective acknowledgements (SACKs) provide more efficient congestion and flow control in TCP

[Detailed explanations, diagrams, codes, etc. can be added here if required.]