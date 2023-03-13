Framing is a function of the data link layer that provides a way for a sender to transmit a set of bits that are meaningful to the receiver. Frames are the result of the final layer of encapsulation before the data is transmitted over the physical layer. Frames have headers that contain information such as error-checking codes, source and destination addresses, and protocols.

There are different types of framing methods used in data link layer, such as character-oriented, bit-oriented, and clock-based. Each method has its own advantages and disadvantages, and uses different techniques to mark the boundaries of frames, such as special characters, bit patterns, or timing signals.

#### Framing in link layer in Computer Networks

The following diagram illustrates the basic architecture of a framing in link layer in computer networks:

```
+----------------+----------------+----------------+----------------+
| Physical layer | Physical layer | Physical layer | Physical layer |
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Data link layer| Data link layer| Data link layer| Data link layer|
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Network layer  | Network layer  | Network layer  | Network layer  |
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Transport layer| Transport layer| Transport layer| Transport layer|
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Application    | Application    | Application    | Application    |
| layer          | layer          | layer          | layer          |
+----------------+----------------+----------------+----------------+

```

The diagram shows four nodes (A, B, C, and D) connected by a physical medium (such as a cable or a wireless channel). Each node has four layers of protocols: application, transport, network, and data link. The data link layer is responsible for framing the data packets received from the network layer and sending them to the physical layer. The physical layer is responsible for transmitting the bits of the frames over the medium.

The data link layer can use different framing methods depending on the type of the physical layer and the network requirements. For example, character-oriented framing uses special characters (such as STX and ETX) to mark the start and end of a frame. Bit-oriented framing uses special bit patterns (such as 01111110) to mark the frame boundaries. Clock-based framing uses timing signals (such as a clock pulse) to synchronize the sender and receiver.

The framing method also determines how the data link layer handles errors, flow control, and addressing. For example, character-oriented framing uses parity bits or checksums to detect errors, and ACK or NAK characters to control the flow. Bit-oriented framing uses CRC or checksum to detect errors, and sliding window or stop-and-wait to control the flow. Clock-based framing uses error-correcting codes or retransmission to handle errors, and feedback or rate control to control the flow.

The framing method also affects the efficiency and reliability of the data transmission. For example, character-oriented framing is simple and easy to implement, but it wastes bandwidth and may cause framing errors if the data contains the special characters. Bit-oriented