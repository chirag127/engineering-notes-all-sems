#### Framing in link layer in Computer Networks

Framing is the process of encapsulating data into a frame for transmission over a link layer in computer networks. The frame includes the data, as well as control information such as the source and destination addresses, error detection and correction codes, and other information necessary for the transmission and reception of the data.

Here is an ASCII diagram of a typical frame in the link layer of a computer network:

```
+-----------------+-----------------+-----------------+-----------------+
|  Preamble  |  Destination  |  Source  |  Type  |  Data  |  CRC  |
+-----------------+-----------------+-----------------+-----------------+
```

The preamble is a sequence of bits used to synchronize the receiver's clock with the sender's clock. The destination and source fields contain the addresses of the destination and source nodes, respectively. The type field indicates the type of data contained in the frame. The data field contains the actual data being transmitted. The CRC (Cyclic Redundancy Check) field contains an error-detecting code used to detect errors in the transmission of the frame.
