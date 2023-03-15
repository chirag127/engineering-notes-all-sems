#### Framing in link layer in Computer Networks

- Framing is a function of the data link layer. It provides a way for a sender to transmit a set of bits that are meaningful to the receiver.
- Frames are the result of the final layer of encapsulation before the data is transmitted over the physical layer. A frame consists of a link layer header followed by a packet.
- The link layer header contains information such as source and destination addresses, error-checking codes, and protocol identifiers.
- Framing uses frames to send or receive data. The data link layer receives packets from the network layer and converts them into frames.
- Framing also involves dividing the data stream into frames of fixed or variable size, adding delimiters to mark the boundaries of each frame, and applying techniques to detect and correct errors.
- There are various kinds of framing methods, such as character count, character stuffing, bit stuffing, and flag bytes.
- Character count framing uses a field in the header to indicate the number of characters in the frame. This method is simple but vulnerable to errors if the count is corrupted or the frame is lost.
- Character stuffing framing uses a special character, such as ESC, to mark the start and end of each frame. If the data contains the same character, it is preceded by another ESC to avoid confusion. This method is more robust but requires more overhead.
- Bit stuffing framing uses a special bit pattern, such as 01111110, to mark the start and end of each frame. If the data contains five consecutive 1s, a 0 is inserted after them to avoid confusion. This method is efficient and reliable but requires bit-level processing.
- Flag byte framing uses a special byte, such as 7E, to mark the start and end of each frame. If the data contains the same byte, it is replaced by a different byte, such as 7D, and the original byte is appended after it. This method is simple and flexible but requires byte-level processing.