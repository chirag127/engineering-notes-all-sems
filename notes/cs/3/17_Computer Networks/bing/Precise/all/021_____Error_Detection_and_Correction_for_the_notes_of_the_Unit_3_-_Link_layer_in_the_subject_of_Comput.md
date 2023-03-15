# Error Detection and Correction

Error detection and correction are techniques used in the link layer of computer networks to ensure the integrity of data transmitted over a communication channel. These techniques are used to detect and correct errors that may occur during transmission due to noise, interference, or other factors.

Some common error detection techniques include:

1. **Parity Check:** A parity bit is added to the data to ensure that the number of 1s in the data is even or odd, depending on the type of parity used. The receiver checks the parity of the received data and if it does not match, an error is detected.

2. **Checksum:** A checksum is calculated by adding the data and taking the complement of the result. The checksum is transmitted along with the data and the receiver recalculates the checksum to verify if the data was received correctly.

3. **Cyclic Redundancy Check (CRC):** A CRC is calculated by dividing the data by a predetermined polynomial and the remainder is transmitted along with the data. The receiver performs the same calculation and if the remainder does not match, an error is detected.

Error correction techniques are used to correct errors that are detected. Some common error correction techniques include:

1. **Forward Error Correction (FEC):** FEC involves transmitting additional redundant information along with the data, which can be used by the receiver to correct errors without the need for retransmission.

2. **Automatic Repeat Request (ARQ):** ARQ involves the receiver sending a negative acknowledgement (NAK) to the sender if an error is detected, requesting the sender to retransmit the data.

These techniques are used in various combinations to ensure the integrity of data transmitted over a communication channel. The choice of technique depends on factors such as the error rate of the channel, the importance of the data, and the cost of retransmission.