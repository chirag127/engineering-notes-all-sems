

### Framing for the notes of the Unit 3 - Link layer in the subject of Computer Networks

The link layer is responsible for transferring data between adjacent network nodes. The data is transmitted in the form of frames. Framing is the process of dividing a stream of data into smaller units for transmission over the network. In this unit, we will learn about the different framing methods used in computer networks.

Here are some important points to keep in mind while studying framing in the link layer:

- Framing is essential to ensure that data is transmitted reliably over the network. It helps to distinguish the start and end of a frame and also detects errors during transmission.
- There are two main types of framing methods: character-oriented and bit-oriented. Character-oriented framing uses a special character to mark the start and end of a frame, whereas bit-oriented framing uses a combination of bits to delimit the frame.
- In character-oriented framing, the start and end flag characters are used to mark the beginning and end of a frame. The flag characters are chosen in such a way that they cannot appear in the data itself. The flag characters are usually a sequence of 0111110.
- Bit-oriented framing uses a combination of bits to mark the start and end of a frame. One common method is to use a special bit sequence called a "bit-stuffing" sequence. The bit-stuffing sequence is inserted into the data stream whenever a predefined bit pattern occurs. This ensures that the receiver can always identify the start and end of a frame.
- In addition to start and end markers, a frame also includes other fields such as a header, payload, and checksum. The header contains information such as the source and destination addresses, while the payload contains the actual data being transmitted. The checksum is used to detect errors during transmission.
- One common framing protocol used in Ethernet networks is the Ethernet II framing format. This format uses a preamble, start frame delimiter, header, payload, and checksum. The preamble and start frame delimiter are used to indicate the start of a frame, while the header contains information such as source and destination addresses. The payload contains the actual data being transmitted, while the checksum is used to detect errors.
- Another important aspect of framing is flow control. Flow control is used to regulate the pace of data transmission to ensure that the receiver can handle the incoming data. One common flow control mechanism used in computer networks is called the sliding window protocol.

In conclusion, framing is an essential aspect of the link layer in computer networks. By dividing data into smaller units for transmission, framing helps to ensure reliable data transfer and error detection. Understanding the different framing methods and protocols is crucial for anyone studying computer networks.