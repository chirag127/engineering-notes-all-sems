# Framing for the notes of the Unit 3 - Link layer in the subject of Computer Networks

- Framing is the process of dividing a stream of bits into smaller units called frames at the link layer.
- Frames are the basic units of data transmission in the link layer.
- Framing is necessary because the link layer does not have any information about the boundaries of the packets or messages sent by the upper layers.
- Framing also provides error detection and correction mechanisms to ensure reliable data transmission over the link.
- There are two main types of framing methods: character-oriented and bit-oriented.
- Character-oriented framing uses special characters to mark the beginning and end of a frame, such as STX (start of text) and ETX (end of text).
- Character-oriented framing is simple and easy to implement, but it has some drawbacks, such as:
  - It requires that the data does not contain any special characters, or they have to be escaped or encoded in some way.
  - It wastes bandwidth by sending extra characters for framing.
  - It cannot handle variable-length frames efficiently.
- Bit-oriented framing uses a special bit pattern to mark the beginning and end of a frame, such as 01111110.
- Bit-oriented framing is more efficient and flexible than character-oriented framing, but it has some challenges, such as:
  - It requires that the data does not contain the special bit pattern, or it has to be modified or stuffed with extra bits to avoid confusion.
  - It requires synchronization between the sender and receiver to correctly identify the frames.
  - It may introduce errors due to bit flips or noise in the transmission medium.
- Some examples of bit-oriented framing protocols are HDLC (High-level Data Link Control) and PPP (Point-to-Point Protocol).