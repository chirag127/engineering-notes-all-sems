 Here is the content in Markdown format without any emojis or external links:

### Error Detection and Correction for the notes of the Unit 3 - Link layer in the subject of Computer Networks.

1. Error Detection
- Checksum: Simple arithmetic sum of data. If data is changed, checksum will not match.
- CRC: Cyclic Redundancy Check. More complex method. Calculation based on polynomial division. Remainder is sent with data. Receiver calculates CRC again and checks for match.

2. Error Correction
- Forward Error Correction: Adds redundant data that can be used to recover from errors.
- Retransmission: If error is detected, transmitter sends data again. Can be inefficient if error rate is high.

3. Hamming Code
- Detects and corrects single-bit errors.
- Uses a set of extra parity bits that makes valid codewords be a certain distance apart. If the codeword changes due to a single-bit error, it moves to a different valid codeword (the nearest one), so the change can be detected and corrected.
- For every 4 data bits, 3 parity bits are added, so it has some redundancy/ overhead. But it enables error correction.

The above content is written in a formal tone with points and without any emojis or external links as requested. The Markdown format is used and the content is written as study material to learn the topic of Error Detection and Correction in Unit 3 - Link layer of Computer Networks. Please let me know if you would like me to modify or expand the content.