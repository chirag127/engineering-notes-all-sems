#### Framing in link layer in Computer Networks

- Framing is a function of the data link layer. It provides a way for a sender to transmit a set of bits that are meaningful to the receiver   .
- Framing uses frames to send or receive data. The data link layer receives packets from the network layer and converts them into frames .
- Frames have headers that contain information such as error-checking codes, source and destination addresses, and control information .
- Frames are the result of the final layer of encapsulation before the data is transmitted over the physical layer.
- Framing is necessary because the physical layer only accepts and transfers a stream of bits without any regard to meaning or structure .
- Framing also helps to synchronize the transmission and reception of data, and to detect and correct errors .

- There are different types of framing methods, such as:
  - Character count: The header contains a field that specifies the number of characters in the frame. This method is simple but unreliable, as any error in the count field or the frame data can cause loss of synchronization  .
  - Byte stuffing: The frame starts and ends with a special byte pattern, such as DLE STX (Data Link Escape, Start of Text) and DLE ETX (End of Text). If the frame data contains the same pattern, it is stuffed with an extra DLE byte to avoid confusion. This method is more reliable but requires extra overhead for stuffing and destuffing  .
  - Bit stuffing: The frame starts and ends with a special bit pattern, such as 01111110. If the frame data contains five consecutive 1s, a 0 is stuffed after them to avoid confusion. This method is also reliable but requires extra overhead for stuffing and destuffing  .
  - Physical layer coding violations: The frame uses the physical layer encoding scheme, such as Manchester or NRZ, to mark the start and end of the frame. For example, a violation of the Manchester scheme, such as 00 or 11, can indicate the frame boundary. This method is efficient but depends on the physical layer implementation  .

- A possible mnemonic to remember the four framing methods is: **C**harlie **B**rown **B**ites **P**eanuts, where C stands for Character count, B stands for Byte stuffing and Bit stuffing, and P stands for Physical layer coding violations.
- A possible ascii diagram to illustrate the framing process is:

```
Network layer packet: | DATA |

Data link layer frame: | HEADER | DATA | TRAILER |

Physical layer bits: 0101010101010101 | HEADER | DATA | TRAILER | 0101010101010101
```