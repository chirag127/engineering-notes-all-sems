### Error Detection and Correction

Error detection and correction are techniques used in the link layer of computer networks to ensure the integrity of data transmitted over a communication channel. These techniques are used to detect and correct errors that may occur during transmission due to noise, interference, or other factors.

There are several methods used for error detection and correction, including:

1. **Parity Checking:** This method involves adding an extra bit, called a parity bit, to the data being transmitted. The parity bit is set to 1 or 0 depending on whether the number of 1s in the data is even or odd. The receiver checks the parity of the received data and if it does not match the expected parity, an error is detected.

2. **Checksum:** This method involves calculating a checksum value for the data being transmitted and sending it along with the data. The receiver recalculates the checksum for the received data and compares it with the received checksum. If the two values do not match, an error is detected.

3. **Cyclic Redundancy Check (CRC):** This method involves dividing the data by a predetermined polynomial and sending the remainder along with the data. The receiver performs the same division and compares the remainder with the received value. If the two values do not match, an error is detected.

4. **Forward Error Correction (FEC):** This method involves adding redundant information to the data being transmitted, allowing the receiver to detect and correct errors without the need for retransmission. FEC is commonly used in applications where retransmission is not feasible, such as satellite communication.

These are some of the common methods used for error detection and correction in the link layer of computer networks. The choice of method depends on factors such as the reliability of the communication channel, the amount of data being transmitted, and the acceptable error rate.