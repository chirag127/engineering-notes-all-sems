### Framing for the notes of the Unit 3 - Link layer in the subject of Computer Networks

- Framing is the process of dividing a stream of bits into smaller units called frames at the link layer.
- Frames are the basic units of data transmission in the link layer.
- Framing is necessary because the link layer does not have a fixed or predefined length for the data it sends or receives.
- Framing allows the link layer to detect and correct errors, synchronize the sender and receiver, and delimit the boundaries of the frames.
- There are different methods of framing, such as character count, flag bytes, bit stuffing, and physical layer coding violations.
- Character count method uses a field in the header of the frame to indicate the number of characters in the frame. This method is simple but unreliable, as any error in the count field or the frame data can cause the loss of synchronization.
- Flag bytes method uses a special byte pattern, such as 01111110, to mark the beginning and end of each frame. This method is more reliable than character count, but it requires that the flag pattern does not appear in the frame data. To avoid this, a technique called bit stuffing is used, which inserts an extra 0 bit after every five consecutive 1 bits in the frame data.
- Bit stuffing method is a variation of flag bytes method that uses bit stuffing to prevent the flag pattern from appearing in the frame data. This method is more efficient than character count, as it does not waste bits for the count field. However, it requires that the sender and receiver agree on the flag pattern and the bit stuffing rule.
- Physical layer coding violations method uses the properties of the physical layer encoding scheme, such as Manchester encoding, to indicate the frame boundaries. This method does not require any extra bits or fields in the frame, but it depends on the specific physical layer technology.