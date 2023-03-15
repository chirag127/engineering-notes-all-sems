#### Framing in link layer in Computer Networks

- Framing is a function of the data link layer that provides a way for a sender to transmit a set of bits that are meaningful to the receiver   .
- Framing uses frames to send or receive data. A frame is a protocol data unit at the data link layer that consists of a link layer header followed by a packet.
- The link layer header contains information such as source and destination addresses, error-checking codes, and control information.
- Framing is necessary because the physical layer only accepts and transfers a stream of bits without any regard to meaning or structure.
- Framing also helps to synchronize the sender and receiver by marking the start and end of each frame.
- There are different types of framing methods, such as character-oriented, bit-oriented, and clock-based framing .
- Character-oriented framing uses special characters to indicate the start and end of each frame, such as STX (start of text) and ETX (end of text). This method is simple but may encounter problems if the data contains the same special characters.
- Bit-oriented framing uses a special bit pattern, such as 01111110, to indicate the start and end of each frame. This method is more efficient but requires bit stuffing to avoid confusion if the data contains the same bit pattern.
- Clock-based framing uses a clock signal to synchronize the sender and receiver and to determine the frame boundaries. This method is reliable but requires a dedicated channel for the clock signal.