#### Framing in Link Layer in Computer Networks

Framing is the process of dividing a long data stream into smaller, manageable data units for transmission over a communication channel. In computer networks, framing is performed at the Link Layer of the OSI model. The Link Layer is responsible for providing a reliable and error-free communication between two adjacent nodes in a network. Framing is one of the major functions of the Link Layer.

The primary purpose of framing is to provide a way to distinguish the start and end of a data unit in a stream of bits. This is achieved by adding a header and a trailer to the data unit. The header contains information such as the source and destination addresses and the type of data being transmitted. The trailer contains a checksum or a cyclic redundancy check (CRC) to detect any errors in the data unit.

Mnemonics and Learning Tricks:
- One mnemonic to remember the purpose of framing is "Start and Stop for every Hop". This means that framing helps in identifying the start and end of a data unit for every hop or transmission from one node to another in a network.

There are various techniques used for framing in computer networks. Some of the commonly used techniques are:

1. Character Count:
In this technique, a fixed number of characters are used to define the length of a data unit. For example, if the length of a data unit is 10 characters, then the first two characters in the header may be used to represent the length, and the remaining eight characters may represent the data.

2. Byte Stuffing:
In this technique, a special character is used to indicate the start and end of a data unit. If the special character appears within the data, it is replaced by a sequence of two characters. For example, if the special character is "X" and it appears within the data, it is replaced by "XY" in the transmitted data, and "X" is used to indicate the start and end of the data unit.

3. Bit Stuffing:
In this technique, a special bit pattern is used to indicate the start and end of a data unit. If the bit pattern appears within the data, a bit is inserted after it to ensure that it does not get confused with the start and end of the data unit.

Advantages of Framing:
- Framing provides a way to identify the start and end of a data unit in a stream of bits.
- Framing helps in detecting errors in the data unit using checksum or CRC.

Disadvantages of Framing:
- Framing adds overhead to the data transmission, as it requires additional bits to be added to the data unit.
- Different framing techniques may be required for different types of data, which can lead to complexity in the network.

Overall, framing is an important function of the Link Layer in computer networks. It helps in providing reliable and error-free communication between two adjacent nodes in a network.