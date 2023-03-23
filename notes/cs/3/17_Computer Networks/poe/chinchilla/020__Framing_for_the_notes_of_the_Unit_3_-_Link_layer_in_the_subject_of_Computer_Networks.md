### Framing for the notes of the Unit 3 - Link layer in the subject of Computer Networks

The link layer is the second layer of the OSI model and is responsible for transferring data between adjacent network nodes. One of the important functions of the link layer is to divide the data into smaller frames before transmitting it over the physical layer. In this section, we will discuss the framing process in detail.

#### What is Framing?

Framing is the process of dividing the data into smaller frames that can be transmitted over the network. The main purpose of framing is to provide a way for the receiver to distinguish between different frames and reassemble them in the correct order.

#### Types of Framing

There are three types of framing techniques:

1. Character-Oriented Framing: In character-oriented framing, each frame is delimited by special characters, such as start-of-frame (SOF) and end-of-frame (EOF) characters. The SOF and EOF characters are added to the beginning and end of each frame, respectively.

2. Bit-Oriented Framing: In bit-oriented framing, each frame is delimited by a special bit pattern, such as the flag sequence 01111110. The flag sequence is added to the beginning and end of each frame, respectively.

3. Byte-Oriented Framing: In byte-oriented framing, each frame is delimited by a special byte, such as the DLE byte (0x10). The DLE byte is added to the beginning and end of each frame, respectively.

#### Framing Process

The framing process involves the following steps:

1. Data Link Layer receives the data from the Network Layer.

2. The data is divided into smaller frames.

3. Each frame is assigned a sequence number.

4. The framing method is applied to each frame to add the necessary delimiters.

5. The frames are transmitted over the physical layer.

6. The receiver receives the frames and uses the sequence numbers to reassemble the data in the correct order.

#### Advantages of Framing

Framing provides several advantages, including:

1. Error Detection: Framing allows for error detection, as each frame has a checksum that can be used to detect transmission errors.

2. Flow Control: Framing allows for flow control, as the receiver can send acknowledgement frames to the sender to indicate that it is ready to receive more data.

3. Addressing: Framing allows for addressing, as each frame can contain the address of the sender and receiver.

4. Reassembly: Framing allows for the reassembly of data at the receiver end, as each frame has a sequence number that can be used to reassemble the data in the correct order.

In conclusion, framing is an important process in the link layer of a computer network. It allows for the division of data into smaller frames, which can be transmitted over the network and reassembled at the receiver end. Framing also provides several advantages, including error detection, flow control, addressing, and reassembly.