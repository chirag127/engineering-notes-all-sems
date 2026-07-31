Hello, I am Sydney, your AI assistant. I can help you with your query.

Framing is a function of the data link layer that provides a way for a sender to transmit a set of bits that are meaningful to the receiver. Framing uses frames to send or receive data. The data link layer receives packets from the network layer and converts them into frames. Frames have headers that contain information such as error-checking codes, source and destination addresses, and protocols.

There are different types of framing methods used in data link layer, such as:

- Character count: This method uses a field in the header to specify the number of characters in the frame. The receiver counts the characters and knows where the frame ends. This method is simple but not reliable, as any error in the count field or the data can cause framing errors.

- Byte stuffing: This method uses a special byte sequence, such as DLE STX (Data Link Escape, Start of Text) to mark the beginning of the frame, and DLE ETX (Data Link Escape, End of Text) to mark the end of the frame. If the data contains the same byte sequence, it is replaced by another sequence, such as DLE DLE, to avoid confusion. The receiver reverses the process and recovers the original data. This method is more reliable but requires extra bytes to be inserted and removed.

- Bit stuffing: This method uses a special bit pattern, such as 01111110, to mark the beginning and end of the frame. If the data contains five consecutive 1s, a 0 is inserted after them to avoid confusion. The receiver reverses the process and recovers the original data. This method is also reliable but requires extra bits to be inserted and removed.

- Physical layer coding violation: This method uses the properties of the physical layer to mark the beginning and end of the frame. For example, in Manchester encoding, a transition from high to low voltage represents a 1, and a transition from low to high voltage represents a 0. A violation of this rule, such as a high to high or low to low transition, can be used to indicate the start or end of a frame. This method does not require extra bits or bytes, but depends on the physical layer encoding scheme.

#### Framing in link layer in Computer Networks

```
+----------------+----------------+----------------+----------------+
| Frame header   | Data           | Frame trailer  | Interframe gap |
+----------------+----------------+----------------+----------------+
| Source address | Network packet | Error checking | Idle time      |
| Destination    |                | code           |                |
| address        |                |                |                |
| Protocol       |                |                |                |
| Count or flag  |                |                |                |
+----------------+----------------+----------------+----------------+
```