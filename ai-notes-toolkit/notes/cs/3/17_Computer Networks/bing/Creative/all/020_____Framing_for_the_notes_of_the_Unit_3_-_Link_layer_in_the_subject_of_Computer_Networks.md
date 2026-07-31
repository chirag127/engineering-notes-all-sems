Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Framing for the Unit 3 - Link layer in the subject of Computer Networks. Here is the content in markdown format:

# Framing
- Framing is the process of dividing a stream of bits into smaller units called frames for transmission over a link layer.
- Frames are the basic units of data exchange in the link layer, and they contain a header, a payload, and a trailer.
- The header contains information such as the source and destination addresses, the frame type, and the error detection code.
- The payload contains the actual data to be transmitted, such as a packet from the network layer or an application message.
- The trailer contains a special sequence of bits that marks the end of the frame and helps in error detection.
- Framing is necessary because the link layer does not have a fixed or predefined length for the data units, and it needs to identify the boundaries of each frame in the bit stream.
- Framing also helps in error detection and correction, as each frame can be checked for errors independently and retransmitted if necessary.
- There are two main methods of framing: character-oriented and bit-oriented.

## Character-oriented framing
- Character-oriented framing uses a special character, such as a flag or a delimiter, to mark the beginning and the end of each frame.
- The flag character is usually a unique pattern of bits, such as 01111110, that is unlikely to appear in the payload data.
- The flag character is also used to separate consecutive frames in the bit stream.
- A problem with character-oriented framing is that the flag character may appear in the payload data by chance, which can cause confusion and errors in the framing process.
- To avoid this problem, a technique called byte stuffing or character stuffing is used, which involves inserting an escape character before the flag character if it appears in the payload data.
- The escape character is another special character, such as 01111101, that indicates that the following character is part of the payload data and not a flag character.
- The receiver can then remove the escape character and restore the original payload data.
- An example of character-oriented framing with byte stuffing is shown below:

![Character-oriented framing with byte stuffing](https://i.imgur.com/6f0jxZT.png)

## Bit-oriented framing
- Bit-oriented framing uses a special bit pattern, such as 01111110, to mark the beginning and the end of each frame.
- The bit pattern is also used to separate consecutive frames in the bit stream.
- A problem with bit-oriented framing is that the bit pattern may appear in the payload data by chance, which can cause confusion and errors in the framing process.
- To avoid this problem, a technique called bit stuffing or zero insertion is used, which involves inserting a 0 bit after five consecutive 1 bits in the payload data.
- The receiver can then remove the 0 bit and restore the original payload data.
- An example of bit-oriented framing with bit stuffing is shown below:

![Bit-oriented framing with bit stuffing](https://i.imgur.com/1gqfQZL.png)
