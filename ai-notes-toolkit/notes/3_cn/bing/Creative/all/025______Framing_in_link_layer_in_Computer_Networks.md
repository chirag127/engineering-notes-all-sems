#### Framing in link layer in computer networks

- Framing is a function of the data link layer that provides a way for a sender to transmit a set of bits that are meaningful to the receiver.
- Framing uses frames to send or receive data. A frame is a digital data transmission unit that consists of a data link layer header followed by a packet.
- The data link layer header contains information such as source and destination addresses, error-checking codes, and control information.
- The packet contains the data from the network layer or the upper layers.
- Framing is necessary because the physical layer only accepts and transfers a stream of bits without any regard to meaning or structure.
- Framing also helps to synchronize the sender and receiver by marking the start and end of each frame.
- There are different types of framing methods, such as character-oriented, bit-oriented, and clock-based .
- Character-oriented framing uses special characters to indicate the start and end of each frame, such as STX (start of text) and ETX (end of text). An example of character-oriented framing is BISYNC.
- Bit-oriented framing uses special bit patterns to indicate the start and end of each frame, such as flag bits. An example of bit-oriented framing is HDLC.
- Clock-based framing uses a fixed time interval to indicate the start and end of each frame, such as one millisecond. An example of clock-based framing is SONET.
- Each framing method has its own advantages and disadvantages, such as efficiency, reliability, complexity, and overhead.
- A mnemonic to remember the three types of framing methods is **C**haracter, **B**it, and **C**lock, or **C**BC.
- A learning trick to understand the difference between character-oriented and bit-oriented framing is to think of them as using different alphabets. Character-oriented framing uses a fixed set of characters, such as ASCII, to encode the data, while bit-oriented framing uses a variable set of bits, such as 0 and 1, to encode the data.