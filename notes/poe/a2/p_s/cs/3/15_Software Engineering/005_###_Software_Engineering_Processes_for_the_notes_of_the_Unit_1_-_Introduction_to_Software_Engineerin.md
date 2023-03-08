 Here is the content in markdown format for the given topic:

#### Error Detection and Correction in link layer in Computer Networks

The link layer is responsible for handling errors in the transmission between two nodes connected over a physical medium. The following are the methods used for error detection and correction in the link layer:

1. Error Detection
- Parity bit: Adds an extra parity bit to the transmitted frame such that the total number of 1s becomes even/odd. If the receiver gets a different parity, it detects an error.
- Checksum: Calculates a numeric value from the contents of the frame and appends it to the frame. If the checksum calculated by the receiver is different, it detects an error.

2. Error Correction
- Hamming code: Adds extra parity bits to detect and correct single-bit errors. Allows the receiver to detect and correct the error.
- CRC code: Calculates a cyclic redundancy check (CRC) value and appends it to the frame. The receiver recalculates the CRC and checks for error. If the values mismatch, it requests retransmission of the corrupted frame.

Advantages:
- Errors are detected and corrected, ensuring data integrity.
- Single bit errors can be corrected without retransmission, reducing latency.

Disadvantages:
- Additional overhead bits are added to the frame, reducing the effective throughput.
- Only limited number of errors can be detected and corrected. Burst errors cannot be handled.

Applications:
- Ethernet uses CRC for error detection.
- Memory devices and storage media use Hamming code for error correction.

[Detailed diagrams and code examples can be added here for more clarity.]