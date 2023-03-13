#### Framing in link layer in Computer Networks

- Framing is a function of the data link layer that provides a way for a sender to transmit a set of bits that are meaningful to the receiver   .
- Framing uses frames to send or receive data. A frame is the unit of transmission in a link layer protocol, and consists of a link layer header followed by a packet.
- The data link layer receives packets from the network layer and converts them into frames. The frames have headers that contain information such as error-checking codes, source and destination addresses, and control information  .
- Framing is necessary because the physical layer only accepts and transfers a stream of bits without any regard to meaning or structure. The frames help the receiver to identify the start and end of each packet, and to detect and correct any errors that may occur during transmission .
- There are various kinds of framing methods used in data link layer, such as character count, byte stuffing, bit stuffing, and physical layer coding violations. Each method has its own advantages and disadvantages, and is suitable for different types of data and transmission media.