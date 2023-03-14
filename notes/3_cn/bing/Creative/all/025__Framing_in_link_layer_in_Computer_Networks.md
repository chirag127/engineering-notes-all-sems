#### Framing in link layer in Computer Networks

Framing is a function of the data link layer that provides a way for a sender to transmit a set of bits that are meaningful to the receiver. Framing uses frames to send or receive data. The data link layer receives packets from the network layer and converts them into frames. Frames have headers that contain information such as error-checking codes, source and destination addresses, and control information. Frames are the units of digital transmission, particularly in computer networks and telecommunications. Frames are comparable to the packets of energy called photons in the case of light energy. Frame is continuously used in Time Division Multiplexing process.

Framing is an important aspect of data link layer protocol design because it allows the transmission of data to be organized and controlled, ensuring that the data is delivered accurately and efficiently. Framing also helps to identify the boundaries of the frames and to distinguish them from the stream of bits in the physical layer. 

There are two types of framing: fixed size and variable size.

- Fixed size framing: The frame is of fixed size and there is no need to provide boundaries to the frame, the length of the frame itself acts as a delimiter. The advantage of this type of framing is that it is simple and easy to implement. The disadvantage is that it suffers from internal fragmentation if the data size is less than the frame size. This can be solved by padding the data with extra bits to fill the frame.
- Variable size framing: In this type of framing, there is a need to define the end of the frame as well as the beginning of the next frame to distinguish them. This can be done in two ways: length field and end delimiter.
  - Length field: We can introduce a length field in the frame to indicate the length of the frame. This is used in Ethernet (802.3). The advantage of this method is that it avoids internal fragmentation and allows variable size data. The disadvantage is that sometimes the length field might get corrupted and cause errors in framing.
  - End delimiter: We can introduce an end delimiter (pattern) to indicate the end of the frame. This is used in Token Ring. The advantage of this method is that it allows variable size data and avoids internal fragmentation. The disadvantage is that the end delimiter can occur in the data and cause confusion. This can be solved by using character stuffing or bit stuffing.
    - Character stuffing: This is used when frames consist of characters. If the data contains the end delimiter, then a special character (escape character) is inserted before the end delimiter to differentiate it from the actual end delimiter. The receiver removes the escape character and keeps the data. This is also known as byte stuffing or character-oriented framing.
    - Bit stuffing: This is used when frames consist of bits. If the data contains a sequence of bits that matches the end delimiter, then an extra bit (usually 0) is inserted after the sequence to differentiate it from the actual end delimiter. The receiver removes the extra bit and keeps the data. This is also known as bit-oriented framing.

The following diagram shows an example of variable size framing with end delimiter and bit stuffing:

```
+-----------------+-----------------+-----------------+-----------------+
| Start delimiter | Data            | End delimiter   | Start delimiter |
+-----------------+-----------------+-----------------+-----------------+
| 01111110        | 101010101111110 | 01111110        | 01111110        |
+-----------------+-----------------+-----------------+-----------------+
                  |                 |                 |
                  |                 |                 +---> Extra bit inserted
                  |                 +---> End delimiter
                  +---> Data
```

Some mnemonics and learning tricks for framing in link layer are:

- Remember that framing is a function of the data link layer that provides a way to transmit meaningful bits to the receiver.
- Remember that there are two types of framing: fixed size and variable size.
- Remember that fixed size framing is simple but suffers from internal fragmentation, while variable size framing avoids internal fragmentation but needs to define the boundaries of the frames.
- Remember that variable size framing can use length field or end delimiter to define the boundaries of the frames.
- Remember that length field is used in Ethernet and end delimiter is used in Token Ring.
- Remember that character stuffing and bit stuffing are used to avoid confusion when the data contains the end delimiter.