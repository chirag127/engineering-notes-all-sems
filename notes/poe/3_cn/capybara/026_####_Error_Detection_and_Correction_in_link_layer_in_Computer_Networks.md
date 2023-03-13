#### Error Detection and Correction in link layer in Computer Networks

The link layer is responsible for transferring data between adjacent network nodes over a physical medium. During this transmission, data can be corrupted due to various reasons such as noise, interference, attenuation, etc. To ensure reliable data transfer, error detection and correction techniques are used in the link layer.

**Error Detection Techniques:** 

1. Parity Check: In this technique, an additional bit, called parity bit, is added to the data to make the total number of 1s either even or odd. The receiver checks the parity of the received data and if it does not match with the expected parity, then an error is detected.

2. Checksum: In this technique, a checksum value is calculated by adding all the data bits together. The receiver calculates the checksum of the received data and compares it with the transmitted checksum. If they do not match, then an error is detected.

3. Cyclic Redundancy Check (CRC): In this technique, a polynomial function is used to generate a CRC code, which is appended to the data. The receiver performs the same polynomial function on the received data and compares it with the received CRC code. If they do not match, then an error is detected.

**Error Correction Techniques:**

1. Automatic Repeat Request (ARQ): In this technique, the receiver sends an acknowledgement (ACK) message to the sender when it receives the data. If the sender does not receive the ACK message within a specified time, it assumes that the data has been lost or corrupted and retransmits the data. 

2. Forward Error Correction (FEC): In this technique, redundancy bits are added to the data to allow the receiver to correct errors without requesting retransmission. 

**Mnemonics and Learning Tricks:**

1. For Parity Check, remember the phrase "Even Parity is Nice and Odd Parity is Naughty". This means that even parity checks if the number of 1s in the data is even, and odd parity checks if the number of 1s in the data is odd.

2. For CRC, remember the acronym "Cyclic Redundancy Check Can Really Correct". This means that CRC can correct errors in the data.

Overall, error detection and correction techniques in the link layer are essential for ensuring reliable data transfer over a physical medium. By using these techniques, network nodes can detect and correct errors, which helps in improving the overall performance of the network.