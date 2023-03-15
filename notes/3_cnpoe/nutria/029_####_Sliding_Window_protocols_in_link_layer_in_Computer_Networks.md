
### Sliding Window Protocols in Link Layer in Computer Networks

Sliding window protocols are used in the link layer of computer networks to ensure reliable and efficient data transmission. These protocols are used to control the flow of data and prevent data loss.

The basic idea behind sliding window protocols is to divide the data into frames, which are then sent over the network. A sliding window is used to keep track of the frames that have been sent, and the frames that have been acknowledged.

#### Advantages of Sliding Window Protocols
- Provide reliable data transmission: The sliding window protocol ensures that all frames are delivered successfully and without errors.
- Increase throughput: The sliding window protocol allows for more efficient use of the network bandwidth, resulting in higher throughput.
- Reduce latency: The sliding window protocol reduces the amount of time needed for acknowledgements, resulting in lower latency.

#### Disadvantages of Sliding Window Protocols
- High overhead: The sliding window protocol requires a large amount of overhead, which can reduce the amount of data that can be sent in a given period of time.
- Complex implementation: The sliding window protocol is complex and requires a lot of programming effort to implement.

#### Mnemonics for Sliding Window Protocols
- WINDOW: W-Window size, I-Increment, N-Negative Acknowledgement, D-Data, O-Overflow, W-Window size
- SWIM: S-Sliding Window, W-Window size, I-Increment, M-Maximum Window size

#### Learning Tricks for Sliding Window Protocols
- Visualize the data frames as a train of cars, with each car representing a data frame. The window is like a gate that only allows a certain number of cars through at a time.
- Think of the window as a buffer that holds the frames until they are acknowledged by the receiver.
- Remember that the window size is determined by the sender, and the increment is determined by the receiver.
- Think of acknowledgements as a way for the receiver to tell the sender that the frame has been received correctly.