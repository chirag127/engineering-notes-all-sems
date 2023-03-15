### Error Detection and Correction in Link Layer

- Error control in data link layer is the process of detecting and correcting data frames that have been corrupted or lost during transmission  .
- Error detection is the process of identifying errors in the received data frames by using some techniques such as parity checks, checksums, or cyclic redundancy checks (CRC)  .
- Error correction is the process of recovering the original data frames from the received data frames by using some techniques such as retransmission, forward error correction (FEC), or hybrid schemes  .
- Retransmission is the simplest technique of error correction, where the sender re-sends the data frames that have been detected as erroneous by the receiver, after receiving a negative acknowledgment (NAK) or a request for retransmission (RTR)  .
- Forward error correction (FEC) is a technique of error correction, where the sender adds some redundant bits to the data frames before transmission, which can be used by the receiver to correct some errors without requesting retransmission  .
- Hybrid schemes are the techniques of error correction, where the sender combines both retransmission and FEC to achieve a balance between efficiency and reliability  .