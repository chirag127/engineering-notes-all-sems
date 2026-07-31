#### Error Detection and Correction in Link Layer in Computer Networks

- The link layer is the layer in the network stack that is responsible for transferring data frames between adjacent nodes in a network.
- Error detection and correction are the processes of identifying and correcting errors that may occur during the transmission of data frames.
- Errors can be caused by various factors, such as noise, interference, distortion, or bit flips in the physical medium.
- Errors can result in corrupted or lost data frames, which can affect the reliability and performance of the network communication.
- Error detection and correction techniques use redundancy, which is the addition of extra bits or symbols to the data frames, to enable the detection and correction of errors.
- There are two main types of error control techniques: forward error correction (FEC) and automatic repeat request (ARQ).
  - FEC involves adding error correction codes to the data frames, which allow the receiver to correct some errors without requesting retransmission from the sender.
  - ARQ involves adding error detection codes to the data frames, which allow the receiver to detect errors and request retransmission from the sender if needed.
- There are three common methods for error detection: parity check, checksum, and cyclic redundancy check (CRC).
  - Parity check involves adding a single bit, called the parity bit, to the data frame, such that the number of 1s in the frame is either even or odd, depending on the parity scheme used. The receiver checks the parity bit and detects an error if the parity does not match.
  - Checksum involves adding a fixed-length value, called the checksum, to the data frame, such that the sum of all the bits in the frame is equal to the checksum. The receiver computes the checksum and detects an error if the checksum does not match.
  - CRC involves adding a fixed-length value, called the CRC, to the data frame, such that the remainder of dividing the frame by a predefined polynomial is equal to the CRC. The receiver performs the same division and detects an error if the CRC does not match.
- There are different types of error correction codes, such as Hamming code, Reed-Solomon code, and convolutional code, which use different mathematical techniques to encode and decode the data frames and correct errors.