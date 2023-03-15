 Here is the content in Markdown format with formal tone and without any emojis or external links:

#### Error Detection and Correction in link layer in Computer Networks.

1. Error Detection
- The link layer receives the packets from the network layer and transmits them to the receiving device. During transmission, errors can creep in the packets due to noise, interference, etc. So, the link layer uses methods to detect the errors in the received packets.
- The most common techniques for error detection are:
-- Parity Bit - Appends a parity bit to the packet which makes the total number of 1's even or odd. If the parity of the received packet is incorrect, it indicates an error.
-- Checksum - Appends a checksum value to the packet calculated from the bits of the packet. The receiver calculates the checksum again and compares it with the appended checksum. If different, it indicates an error.

2. Error Correction
- The link layer not only detects the errors but also corrects the errors if possible. This is done using the following techniques:
-- Single Parity Check - Uses an extra parity bit with odd parity. The position of the bit with error can be identified and flipped to correct the error.
-- Hamming Code - Uses multiple parity bits to identify and correct single-bit errors. More powerful than single parity check but the overhead is more.
-- Forward Error Correction (FEC) - The sender adds redundant data to the packet which is used by the receiver to recover the corrupted bits and correct the errors. Stronger than parity checks and hamming code but has more overhead.

The content summarizes the key concepts of error detection and correction methods used in the link layer of computer networks. The points are written in a formal tone with no external links or emojis. Please let me know if you would like me to modify or expand the content.