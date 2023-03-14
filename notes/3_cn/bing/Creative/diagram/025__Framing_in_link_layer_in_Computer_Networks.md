Framing is a function of the data link layer that divides the data into frames, which are units of digital transmission. Frames have headers that contain information such as source and destination addresses, error-checking codes, and protocols. Different data link layer technologies have different frame structures and methods of framing. Some of the common methods of framing are:

- Fixed size: The frame is of fixed size and there is no need to provide boundaries to the frame, the length of the frame itself acts as a delimiter. This method suffers from internal fragmentation if the data size is less than the frame size, which can be solved by padding.
- Variable size: The frame is of variable size and there is a need to define the end of the frame as well as the beginning of the next frame to distinguish. This can be done in two ways:
  - Length field: A length field in the frame header indicates the length of the frame. This method is used in Ethernet (802.3). The problem with this method is that sometimes the length field might get corrupted.
  - End delimiter: A special bit pattern marks the end of the frame. This method is used in Token Ring. The problem with this method is that the end delimiter can occur in the data. This can be solved by:
    - Character stuffing: If the data contains the end delimiter, a special escape character is inserted before it to differentiate it from the actual end delimiter. This method is used when frames consist of characters.
    - Bit stuffing: If the data contains a sequence of bits that matches the end delimiter, an extra bit is inserted after every five consecutive 1s or 0s to break the pattern. This method is used when frames consist of bits.

The following diagram illustrates the basic architecture of a frame in the data link layer:

```
+----------------+----------------+----------------+----------------+
| Frame Header   | Data           | Frame Trailer  | Interframe Gap |
+----------------+----------------+----------------+----------------+
| Source Address |                | Error Checking |                |
| Destination    |                | Code           |                |
| Address        |                |                |                |
| Protocol       |                |                |                |
| Length/End     |                |                |                |
| Delimiter      |                |                |                |
+----------------+----------------+----------------+----------------+
```

The frame header contains the source and destination addresses, the protocol, and the length or end delimiter of the frame. The data is the payload of the frame, which can be variable or fixed in size. The frame trailer contains the error checking code, which can be a checksum or a cyclic redundancy check (CRC). The interframe gap is the minimum time interval between two consecutive frames, which allows the receiver to process the incoming frame and prepare for the next one.