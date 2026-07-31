Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 3 - Link layer in the subject of Computer Networks. Here is a possible outline for your notes:

### Framing
- Framing is the process of dividing a stream of bits into smaller units called frames for transmission over a link layer.
- Frames are delimited by special bit patterns called frame headers and frame trailers, which contain information such as source and destination addresses, error detection codes, and frame sequence numbers.
- Framing methods can be classified into two categories: character-oriented and bit-oriented.
- Character-oriented framing uses a special character, such as the ASCII code for Start of Header (SOH) or End of Text (ETX), to mark the beginning and end of a frame. This method is simple and easy to implement, but it has some drawbacks, such as:
  - The special characters may appear in the data, which requires escaping or byte stuffing to avoid confusion.
  - The frame size is limited by the maximum length of a character, which may not be optimal for different link layer technologies.
  - The frame header and trailer are not aligned to the bit boundaries, which may cause inefficiency in transmission and processing.
- Bit-oriented framing uses a special bit pattern, such as 01111110, to mark the beginning and end of a frame. This method is more flexible and efficient, but it has some challenges, such as:
  - The special bit pattern may appear in the data, which requires bit stuffing or scrambling to avoid confusion.
  - The frame size is not limited by the character length, but by the maximum transmission unit (MTU) of the link layer, which may vary depending on the technology and the network topology.
  - The frame header and trailer are aligned to the bit boundaries, which may require padding or alignment bits to fill the gaps.