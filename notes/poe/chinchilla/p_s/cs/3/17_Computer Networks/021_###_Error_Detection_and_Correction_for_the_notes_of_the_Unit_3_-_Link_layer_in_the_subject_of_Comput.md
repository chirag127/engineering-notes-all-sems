### Error Detection and Correction for the notes of the Unit 3 - Link layer in the subject of Computer Networks

Errors can occur in the transmission of data due to various reasons such as noise, interference, and weak signals. Error detection and correction techniques are used in computer networks to identify and correct errors that occur during the transmission of data. In this section, we will discuss the various error detection and correction techniques used in the link layer of computer networks.

#### Error Detection Techniques

Error detection techniques are used to identify errors that occur during the transmission of data. The following are some of the commonly used error detection techniques:

1. **Parity Check**: The parity check technique is used to detect errors in the transmission of data. In this technique, an extra bit called the parity bit is added to the data. The parity bit is set to 1 or 0 such that the total number of 1s in the data and the parity bit is always even or odd. If an error occurs during the transmission of data, the parity check fails and the receiver detects the error.

2. **Checksum**: The checksum technique is used to detect errors in the transmission of data. In this technique, a sum is calculated over the data and an extra field called the checksum is added to the data. The receiver calculates the checksum over the received data and compares it with the checksum sent by the sender. If the checksums do not match, the receiver detects the error.

3. **Cyclic Redundancy Check (CRC)**: The CRC technique is a more powerful error detection technique than the parity check and checksum techniques. In this technique, a polynomial code is used to generate a checksum over the data. The receiver calculates the checksum over the received data using the same polynomial code and compares it with the checksum sent by the sender. If the checksums do not match, the receiver detects the error.

#### Error Correction Techniques

Error correction techniques are used to correct errors that occur during the transmission of data. The following are some of the commonly used error correction techniques:

1. **Automatic Repeat reQuest (ARQ)**: The ARQ technique is a feedback-based error correction technique. In this technique, the sender sends the data to the receiver and waits for an acknowledgment (ACK) from the receiver. If the sender does not receive an ACK within a specified time period, it assumes that an error has occurred and retransmits the data. The receiver sends a negative acknowledgment (NAK) to the sender if it detects an error in the received data. The sender retransmits the data in response to the NAK.

2. **Forward Error Correction (FEC)**: The FEC technique is a non-feedback-based error correction technique. In this technique, extra bits are added to the data before transmission such that the receiver can correct errors without the need for retransmission. The redundant bits are generated using mathematical algorithms and are used to correct errors that occur during the transmission of data.

#### Advantages and Disadvantages

1. Parity check is a simple and easy-to-implement error detection technique. However, it can only detect odd numbers of errors.

2. Checksum is a more powerful error detection technique than the parity check technique. However, it cannot detect all types of errors.

3. CRC is a very powerful error detection technique that can detect most types of errors. However, it is more complex and requires more processing power than the parity check and checksum techniques.

4. ARQ is a very effective error correction technique. However, it requires feedback from the receiver and can result in increased latency and overhead.

5. FEC is a more efficient error correction technique than ARQ as it does not require feedback from the receiver. However, it requires more bandwidth to transmit the redundant bits.

#### Examples and Applications

1. Parity check is commonly used in memory systems to detect errors in the stored data.

2. Checksum and CRC techniques are used in network protocols such as TCP and UDP to ensure reliable transmission of data.

3. ARQ is used in wireless communication systems to improve the reliability of data transmission.

4. FEC is used in satellite communication systems to improve the reliability of data transmission over long distances.

In conclusion, error detection and correction techniques are essential for ensuring reliable transmission of data in computer networks. Different techniques have their advantages and disadvantages, and their choice depends on the specific requirements of the network.