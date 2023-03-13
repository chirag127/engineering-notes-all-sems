
### Etransmission in Transport Layer

Etransmission (Error Transmission) is a mechanism used in the Transport Layer of the OSI Model to ensure reliable delivery of data over a network. It is responsible for detecting and correcting errors that may occur during transmission.

The most common technique used for error transmission is the use of checksums. A checksum is a numerical value computed from the data being sent, and is sent along with the data. The receiver then computes the checksum from the received data and compares it with the one sent by the sender. If the two values match, then the data was received without any errors; if not, then the data was corrupted in transit and must be resent.

Other techniques include the use of parity bits, cyclic redundancy check (CRC), and forward error correction (FEC). Parity bits are single bits added to the data that can be used to detect errors. CRC is a more sophisticated form of checksum that can detect a greater number of errors. FEC is a technique used to correct errors that have occurred during transmission.

In conclusion, Etransmission is an important mechanism in the Transport Layer used to ensure reliable delivery of data over a network. It uses techniques such as checksums, parity bits, CRC, and FEC to detect and correct errors that may occur during transmission.