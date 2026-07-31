Error detection and correction in link layer in computer networks is the process of ensuring that the data frames transmitted from the sender to the receiver are accurate and complete. The link layer uses various techniques to add redundancy bits to the data frames and check them for errors at the receiver side. If errors are detected, the receiver can either discard the corrupted frames or request the sender to retransmit them. Some of the common techniques for error detection and correction are parity check, checksum and cyclic redundancy check (CRC)  .

The following is a simplified ASCII diagram of how error detection and correction works in link layer in computer networks:

```
Sender                          Receiver
|                              |
| Data frame: 10101010         |
| Parity bit: 0 (even parity)  |
|------------------------------|----> Data frame: 10101010
|                              |     Parity bit: 0 (even parity)
|                              |     No error detected
|                              |
| Data frame: 11001100         |
| Parity bit: 0 (even parity)  |
|------------------------------|----> Data frame: 11001100
|                              |     Parity bit: 0 (even parity)
|                              |     No error detected
|                              |
| Data frame: 10011001         |
| Parity bit: 0 (even parity)  |
|------------------------------|----> Data frame: 10011001
|                              |     Parity bit: 1 (odd parity)
|                              |     Error detected, discard frame or request retransmission
|                              |
```