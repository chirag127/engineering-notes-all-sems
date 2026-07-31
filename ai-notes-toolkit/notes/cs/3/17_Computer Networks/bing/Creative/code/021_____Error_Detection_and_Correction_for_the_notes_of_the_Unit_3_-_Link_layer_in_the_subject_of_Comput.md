### Error Detection and Correction in Link Layer

- Error detection and correction in link layer is the process of identifying and retransmitting data frames that have been corrupted or lost during transmission  .
- Errors can occur due to noise, interference, distortion, or bit synchronization problems in the communication channel.
- Errors can be classified into three types: single bit errors, multiple bit errors, and burst errors.
  - Single bit errors occur when only one bit in a data frame is changed from 1 to 0 or vice versa.
  - Multiple bit errors occur when two or more bits in a data frame are changed.
  - Burst errors occur when a sequence of consecutive bits in a data frame are changed.
- Error detection and correction techniques can be divided into two categories: forward error correction (FEC) and backward error correction (BEC) or automatic repeat request (ARQ).
  - FEC involves adding redundant bits to the data frame at the sender and using them to correct errors at the receiver without requesting retransmission.
  - BEC or ARQ involves detecting errors at the receiver and requesting retransmission of the corrupted data frame from the sender.
- Some common error detection and correction techniques are parity checks, checksums, cyclic redundancy check (CRC), and Hamming code  .
  - Parity checks involve adding a single bit to the data frame to make the number of 1s even or odd, depending on the type of parity (even or odd) .
  - Checksums involve dividing the data frame into equal segments and adding them together to form a sum, which is appended to the data frame.
  - CRC involves dividing the data frame by a predefined polynomial and appending the remainder to the data frame .
  - Hamming code involves adding extra bits to the data frame to form a code word that satisfies a certain mathematical property, which can be used to detect and correct errors.