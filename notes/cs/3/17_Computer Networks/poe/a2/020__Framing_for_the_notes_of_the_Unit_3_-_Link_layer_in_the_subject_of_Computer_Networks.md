 Here are the notes on the topic "Framing for the notes of the Unit 3 - Link layer in the subject of Computer Networks" in a formal tone without any emojis or external links:

### Framing for the notes of the Unit 3 - Link layer in the subject of Computer Networks

1. Framing: The Link layer takes the packets from the Network layer and converts them into frames. Framing is the process of creating these frames.
2. Purposes of Framing:
- Framing helps in synchronization by identifying the beginning and end of a frame.
- It helps in error detection using mechanisms like CRC. The CRC is calculated for the entire frame and appended at the end of the frame. If the CRC at the receiver does not match with the calculated CRC, it indicates an error.
- It helps in multiplexing and flow control. The type field in the frame header specifies which process the frame belongs to to enable multiplexing.
3. Structure of a Frame: A frame contains the following components:
- Frame header: Includes the destination address, source address, type field, etc.
- Payload: Includes the actual data from the higher layers.
- Frame check sequence (FCS)/Cyclic Redundancy Check (CRC): Includes the error detection bits calculated using CRC algorithm.
4. Frame Synchronization: To identify the beginning and end of a frame, a specific bit pattern is used which cannot appear anywhere else in the frame. This is known as a framing bit or flag. The sender and receiver should be synchronized to this bit pattern to properly identify the frames.

The notes cover the key points about framing in the link layer. Let me know if you would like me to elaborate on any of the points or modify the content.