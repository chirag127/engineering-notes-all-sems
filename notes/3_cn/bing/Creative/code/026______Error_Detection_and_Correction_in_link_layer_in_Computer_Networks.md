#### Error Detection and Correction in link layer in Computer Networks

Error detection and correction in link layer is the process of detecting and correcting data frames that have been corrupted or lost during transmission. The link layer uses various error control techniques for this purpose. The basic approach is the use of redundancy, where additional bits are added to facilitate the detection and correction of errors .

There are three main techniques for detecting errors in frames: Parity Check, Checksum and Cyclic Redundancy Check (CRC).

- Parity Check: The parity check is done by adding an extra bit, called parity bit to the data to make a number of 1s either even in case of even parity or odd in case of odd parity. The receiver checks the parity bit and detects a single bit error if the parity does not match. However, this technique cannot detect multiple bit errors or burst errors.

- Checksum: The checksum is a value calculated from the data by applying a simple mathematical function, such as addition or XOR. The sender appends the checksum to the data and sends it to the receiver. The receiver recalculates the checksum from the received data and compares it with the received checksum. If they match, the data is assumed to be error-free, otherwise an error is detected. However, this technique cannot correct errors, only detect them.

- Cyclic Redundancy Check (CRC): The CRC is a more complex and robust technique that uses polynomial division to generate a code from the data. The sender divides the data by a predefined polynomial and appends the remainder, called CRC, to the data. The receiver divides the received data by the same polynomial and compares the remainder with the received CRC. If they match, the data is assumed to be error-free, otherwise an error is detected. The CRC can detect single bit errors, multiple bit errors and burst errors with a high probability.

To correct errors, the link layer can use either forward error correction (FEC) or backward error correction (BEC).

- Forward Error Correction (FEC): The FEC is a technique that adds extra bits, called error correction code, to the data to enable the receiver to correct errors without requesting retransmission. The FEC can use techniques such as Hamming code, Reed-Solomon code or convolutional code to generate and decode the error correction code. The FEC increases the bandwidth and complexity, but reduces the delay and retransmission.

- Backward Error Correction (BEC): The BEC is a technique that uses feedback from the receiver to the sender to request retransmission of corrupted or lost frames. The BEC can use techniques such as stop-and-wait, go-back-N or selective repeat to implement the feedback and retransmission mechanism. The BEC reduces the bandwidth and complexity, but increases the delay and retransmission.