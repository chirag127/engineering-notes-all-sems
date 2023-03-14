#### Error Detection and Correction in link layer in Computer Networks

- Error detection and correction are techniques that allow data to be sent and received reliably over a noisy communication channel.
- Error detection is the process of detecting if the data has been corrupted or altered during transmission or storage.
- Error correction is the process of recovering the original data from the corrupted data, or requesting a retransmission if recovery is not possible.
- Error detection and correction are performed by adding some extra bits, called redundancy bits, to the data before transmission. These bits are calculated based on some mathematical function, called error detection or correction code, that depends on the data bits.
- The receiver applies the same function to the received data and compares the result with the received redundancy bits. If they match, the data is assumed to be error-free. If they do not match, the data is assumed to be corrupted and error correction or retransmission is performed.
- There are different types of error detection and correction codes, such as parity check, checksum, cyclic redundancy check (CRC), Hamming code, Reed-Solomon code, etc. Each code has different properties, such as error detection capability, error correction capability, complexity, overhead, etc.
- Some codes can only detect errors, but not correct them. These codes are called error detecting codes. Examples are parity check, checksum, and CRC.
- Some codes can detect and correct a limited number of errors. These codes are called error correcting codes. Examples are Hamming code and Reed-Solomon code.
- Some codes can detect and correct errors, as well as request retransmission if the errors are too many to correct. These codes are called hybrid codes. Examples are automatic repeat request (ARQ) protocols, such as stop-and-wait ARQ, go-back-N ARQ, and selective repeat ARQ.
- Error detection and correction are important for reliable data communication, especially in wireless networks, where the channel is prone to noise, interference, fading, etc. They can also improve the efficiency and performance of the network, by reducing the number of retransmissions and increasing the throughput.
- Error detection and correction are also used in other applications, such as data storage, cryptography, digital audio and video, etc.