### Error Detection and Correction in Link Layer

- Error detection and correction in link layer is the process of identifying and re-transmitting data frames that have been corrupted or lost during transmission  .
- Error detection is the mechanism of detecting errors in the received data frames by using techniques such as parity checks, checksums, and cyclic redundancy checks (CRC) .
- Error correction is the mechanism of recovering the original data frames from the corrupted or lost ones by using techniques such as retransmission, forward error correction (FEC), and automatic repeat request (ARQ) .
- Error control in link layer can be classified into two types: stop-and-wait and sliding window .
- Stop-and-wait is a simple technique where the sender sends one frame at a time and waits for an acknowledgment (ACK) or a negative acknowledgment (NAK) from the receiver before sending the next frame .
- Sliding window is a more efficient technique where the sender can send multiple frames without waiting for acknowledgments, but within a specified window size that limits the number of outstanding frames .
- Error control in link layer can also be classified into two types: error detection with retransmission and error detection with correction .
- Error detection with retransmission is a technique where the receiver detects errors in the received frames and requests the sender to retransmit the corrupted or lost frames .
- Error detection with correction is a technique where the receiver corrects the errors in the received frames by using additional information such as parity bits, checksums, or CRC codes that are appended to the frames by the sender .