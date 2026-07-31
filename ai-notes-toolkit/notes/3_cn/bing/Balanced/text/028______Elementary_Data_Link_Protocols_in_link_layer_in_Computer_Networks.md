#### Elementary Data Link Protocols in link layer in Computer Networks

- The data link layer is responsible for framing, error control and flow control in the communication between two adjacent nodes in a network.
- Framing is the process of dividing the bit stream from the physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control is the process of detecting and correcting errors that may occur during transmission or reception of data frames.
- Flow control is the process of regulating the rate of data transmission between the sender and the receiver to avoid congestion or buffer overflow.
- There are different types of protocols in the data link layer that perform these functions in different ways. Some of the elementary data link protocols are:

  - Protocol 1: Unrestricted simplex protocol
    - This protocol assumes that there is a one-way communication channel between the sender and the receiver, and that there are no errors or losses in the channel.
    - The sender simply sends data frames continuously without waiting for any acknowledgment or feedback from the receiver.
    - The receiver accepts and processes the incoming data frames as fast as possible.
    - This protocol is simple and efficient, but it does not provide any error or flow control mechanisms.
    - This protocol is suitable for applications that do not require reliable or bidirectional communication, such as broadcasting or streaming.

  - Protocol 2: Simplex stop-and-wait protocol
    - This protocol assumes that there is a one-way communication channel between the sender and the receiver, but that there may be errors or losses in the channel.
    - The sender sends one data frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
    - The receiver sends an acknowledgment for each received frame after checking for errors. If the frame is corrupted or lost, the receiver does not send any acknowledgment and discards the frame.
    - The sender uses a timer to detect the loss of acknowledgment and retransmits the frame if the timer expires.
    - This protocol provides error control, but it does not provide flow control. It also suffers from low efficiency and long delay due to the waiting time between frames.

  - Protocol 3: Simplex protocol for noisy channels
    - This protocol assumes that there is a one-way communication channel between the sender and the receiver, and that there may be errors or losses in the channel. It also assumes that the channel may introduce duplicate frames due to noise or retransmission.
    - The sender sends one data frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The sender also adds a sequence number to each frame to distinguish between original and duplicate frames.
    - The receiver sends an acknowledgment for each received frame after checking for errors and sequence number. If the frame is corrupted, lost or duplicated, the receiver does not send any acknowledgment and discards the frame.
    - The sender uses a timer to detect the loss of acknowledgment and retransmits the frame if the timer expires.
    - This protocol provides error control and handles duplicate frames, but it does not provide flow control. It also suffers from low efficiency and long delay due to the waiting time between frames.