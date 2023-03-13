#### Framing in Link Layer in Computer Networks

Framing is a process of dividing a stream of data into manageable units known as frames. In computer networks, framing is done at the link layer, which is the second layer of the OSI model. The primary purpose of framing is to ensure that data is transmitted in a way that can be understood by the receiving device. 

The following are some of the important concepts related to framing in the link layer:

1. **Frame Structure:** A frame consists of a header, data, and a trailer. The header contains information such as the source and destination addresses, frame type, and frame size. The data is the actual payload that is being transmitted. The trailer contains error detection and correction information, such as a cyclic redundancy check (CRC).

2. **Framing Techniques:** There are two framing techniques used in computer networks:

    - **Character-Oriented Framing:** In this technique, each frame is delimited by special characters, such as start and stop bits. The disadvantage of this technique is that it is not efficient for transmitting large amounts of data.

    - **Bit-Oriented Framing:** In this technique, the frame boundaries are identified by bit patterns that do not appear in the data. This technique is more efficient than character-oriented framing and is commonly used in modern networks.

3. **Mnemonic:** A useful mnemonic to remember the framing process is "HASDCT," which stands for Header, Address, Size, Data, Control, and Trailer. This can help in remembering the order of the various components of a frame.

4. **Advantages of Framing:** The following are the advantages of framing in computer networks:

    - Reliable data transmission: Framing ensures that data is transmitted in a reliable manner, with error detection and correction mechanisms in place.

    - Efficient use of network bandwidth: By dividing data into frames, the network can transmit data more efficiently, without wasting bandwidth.

    - Compatibility with different network technologies: Framing is used in many different network technologies, making it a versatile and widely accepted technique.

5. **Disadvantages of Framing:** The following are the disadvantages of framing in computer networks:

    - Overhead: The addition of headers, trailers, and error detection/correction information increases the size of the data being transmitted, which can reduce network efficiency.

    - Complexity: The process of framing and error detection/correction adds complexity to the network, which can increase the likelihood of errors and reduce overall network performance.

6. **Examples:** Ethernet, Token Ring, and FDDI are some examples of network technologies that use framing in the link layer.

In conclusion, framing is an essential process in computer networks that ensures reliable and efficient data transmission. By dividing data into frames, the network can transmit data in a way that can be understood by the receiving device, with error detection and correction mechanisms in place to ensure data integrity.