Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 3 - Link layer in the subject of Computer Networks. Here are some notes on the topic of framing:

### Framing

- Framing is the process of dividing a stream of bits into smaller units called frames for transmission over a link layer.
- Frames are the basic units of data exchange in the link layer, and they contain a header, a payload, and a trailer.
- The header contains information such as the source and destination addresses, the frame type, and the error detection code.
- The payload contains the actual data to be transmitted, such as a packet from the network layer or an application message.
- The trailer contains a special sequence of bits that marks the end of the frame and helps in error detection.
- Framing is necessary because the link layer does not have a fixed or predefined length for the data units, and it needs to identify the boundaries of each frame in the bit stream.
- Framing also helps in error detection and correction, as each frame can be checked for errors independently and retransmitted if necessary.
- There are different methods of framing, such as character-oriented framing, bit-oriented framing, and clock-based framing.
- Character-oriented framing uses a special character, such as a flag or a delimiter, to mark the beginning and the end of each frame. The drawback of this method is that the special character may appear in the payload, and it needs to be escaped or encoded to avoid confusion.
- Bit-oriented framing uses a special bit pattern, such as 01111110, to mark the beginning and the end of each frame. The drawback of this method is that the bit pattern may appear in the payload, and it needs to be modified or stuffed with extra bits to avoid confusion.
- Clock-based framing uses a synchronized clock signal to determine the boundaries of each frame. The drawback of this method is that it requires a separate channel for the clock signal, and it may be affected by noise or synchronization errors.