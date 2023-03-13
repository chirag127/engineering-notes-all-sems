 Here is the content written in Markdown format on the topic #### Error Detection and Correction in link layer in Computer Networks:

#### Error Detection and Correction in link layer in Computer Networks

The Link layer is responsible for transferring data between neighbouring network devices. While transmitting data, there are chances of errors creeping in. The Link layer employs techniques to detect and correct these errors. This ensures integrity and reliability of data.

The key techniques used are:

- Error Detection using Parity: Parity bit is added to each byte of data which is used to detect odd/even number of 1's. If the parity calculated from the received data does not match, it indicates error. The drawback is that it can only detect and not correct errors.
- Cyclic Redundancy Check (CRC): A code is appended to the data based on polynomial division of the data. The receiver recalculates the CRC and matches it. If mismatch occurs, error is detected. CRC can detect burst errors and is more powerful than parity checks. But it also cannot correct errors.
- Forward Error Correction (FEC): Extra data in the form of redundant bits are added to the data which can be used by the receiver to detect and correct errors. The receiver uses the redundant bits to reconstruct the corrupted data. FEC is more reliable but overhead on bandwidth is more compared to error detection alone.
- Automatic Repeat Request (ARQ): If error is detected in the received packet, the receiver requests the sender to retransmit the packet. This is done repeatedly till a correct packet is received or maximum retransmissions are reached. This is a reliable method but introduces delay.

Combinations of the above techniques are used in practice to get optimal performance in terms of error detection and correction capabilities as well as overhead on bandwidth and latency.

Mnemonics:
- 'Detect Parity, Correct CRC' can be used to remember that Parity can detect while CRC can detect and correct errors.
- 'Overhead FEC, Delay ARQ' can be used to remember the trade-offs in the two error correction techniques.

[Diagrams and examples can be added if required to explain the concepts]