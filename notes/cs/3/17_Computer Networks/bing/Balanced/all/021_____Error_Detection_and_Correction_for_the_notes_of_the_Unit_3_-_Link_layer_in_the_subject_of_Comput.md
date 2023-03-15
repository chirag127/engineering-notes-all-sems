# Error Detection and Correction in Link Layer

- Error detection and correction in link layer is the process of identifying and retransmitting data frames that have been corrupted or lost during transmission  .
- Error detection and correction techniques are essential for reliable and efficient data communication over noisy channels.
- Errors can occur due to various reasons, such as noise, interference, distortion, attenuation, crosstalk, etc.
- Errors can be classified into three types, namely single bit errors, multiple bit errors, and burst errors.
  - Single bit errors occur when only one bit in a data frame is changed from 1 to 0 or vice versa.
  - Multiple bit errors occur when two or more bits in a data frame are changed.
  - Burst errors occur when a sequence of consecutive bits in a data frame are changed.
- Error detection techniques are used to detect the presence of errors in a data frame and inform the sender or the receiver about them.
- Error detection techniques include parity checks, checksums, and cyclic redundancy checks (CRC) .
  - Parity checks add an extra bit to a data frame to make the number of 1s in the frame even or odd, depending on the type of parity (even or odd) .
  - Checksums add the sum of all the bits in a data frame and append it to the end of the frame .
  - CRCs use a polynomial function to generate a code that is appended to the end of the frame .
- Error correction techniques are used to correct the errors in a data frame without requiring retransmission.
- Error correction techniques include Hamming code, Reed-Solomon code, and convolutional code.
  - Hamming code adds extra bits to a data frame to form a code word that can detect and correct single bit errors.
  - Reed-Solomon code adds extra symbols to a data frame to form a code word that can detect and correct multiple bit errors and burst errors.
  - Convolutional code adds extra bits to a data frame to form a code word that can detect and correct errors using a decoding algorithm.