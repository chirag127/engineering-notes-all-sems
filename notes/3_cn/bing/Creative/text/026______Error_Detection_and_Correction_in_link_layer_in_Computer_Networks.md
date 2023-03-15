#### Error Detection and Correction in link layer in Computer Networks

- Error detection and correction in link layer is the process of identifying and re-transmitting data frames that have been corrupted or lost during transmission  .
- Error detection and correction techniques are essential for reliable and efficient data communication over noisy and unreliable channels.
- Some of the common types of errors that can occur in data transmission are:
  - Single bit errors: A single bit in a data frame is changed from 0 to 1 or vice versa.
  - Multiple bit errors: Two or more bits in a data frame are changed from 0 to 1 or vice versa.
  - Burst errors: A sequence of consecutive bits in a data frame are changed from 0 to 1 or vice versa.
- Some of the common techniques for error detection and correction in link layer are:
  - Parity checks: A parity bit is added to the data frame to make the number of 1s in the frame even or odd. The receiver checks the parity bit and detects a single bit error if the parity does not match .
  - Checksums: A checksum is a value calculated from the data frame using a simple arithmetic operation such as addition or XOR. The sender appends the checksum to the frame and the receiver verifies it by recalculating the checksum from the received frame. A mismatch in the checksum indicates an error in the frame .
  - Cyclic redundancy check (CRC): A CRC is a value computed from the data frame using a polynomial division. The sender appends the CRC to the frame and the receiver verifies it by performing the same polynomial division on the received frame. A nonzero remainder indicates an error in the frame .
- Error detection techniques can only detect the presence of errors in the data frame, but not correct them. Error correction techniques can both detect and correct errors in the data frame.
- Some of the common techniques for error correction in link layer are:
  - Automatic repeat request (ARQ): ARQ is a protocol that uses acknowledgments and timeouts to ensure reliable data delivery. The sender re-transmits the data frame if it does not receive an acknowledgment from the receiver within a specified time or if it receives a negative acknowledgment indicating an error in the frame .
  - Forward error correction (FEC): FEC is a technique that adds redundant bits to the data frame to enable the receiver to correct errors without requesting re-transmission. The sender encodes the data frame using an error-correcting code such as Hamming code or Reed-Solomon code and the receiver decodes the received frame using the same code .