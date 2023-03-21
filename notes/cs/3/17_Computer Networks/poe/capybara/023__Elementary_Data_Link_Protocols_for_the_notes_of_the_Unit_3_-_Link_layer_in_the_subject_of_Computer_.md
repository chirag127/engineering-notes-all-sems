

### Elementary Data Link Protocols

The Link layer is responsible for the transfer of data between two adjacent nodes in a network. The data link protocols are the set of rules that govern this transfer of data. The elementary data link protocols are the basic building blocks for data link protocols.

Here are some important points to keep in mind about elementary data link protocols:

- The main purpose of elementary data link protocols is to provide reliable data transfer over an unreliable transmission medium.
- The two most popular elementary data link protocols are Stop-and-Wait and Sliding Window.
- Stop-and-Wait protocol is a simple protocol where the sender sends one frame at a time and waits for an acknowledgement from the receiver before sending the next frame.
- Sliding Window protocol is a more advanced protocol where the sender can send multiple frames without waiting for an acknowledgement from the receiver. The receiver acknowledges the frames it receives and sends a window size to the sender.
- The window size determines the number of frames that the sender can send before waiting for an acknowledgement from the receiver.
- The most common sliding window protocol is the Go-Back-N protocol, where the sender resends all the frames after the lost frame.
- Another sliding window protocol is the Selective Repeat protocol, where the sender only resends the lost frame, not all the frames after it.
- The elementary data link protocols are used in point-to-point communication and not in broadcast communication.
- The data link layer also provides error detection and correction using techniques such as CRC, checksum, and parity bit.

In conclusion, elementary data link protocols are the basic building blocks for data link protocols that provide reliable data transfer over an unreliable transmission medium. Stop-and-Wait and Sliding Window are the two most popular elementary data link protocols. These protocols are used in point-to-point communication and provide error detection and correction using techniques such as CRC, checksum, and parity bit.