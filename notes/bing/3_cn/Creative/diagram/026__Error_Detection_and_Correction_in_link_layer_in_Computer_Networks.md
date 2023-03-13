#### Error Detection and Correction in link layer in Computer Networks

The data link layer is responsible for ensuring that the data frames transmitted from the source to the destination are free from errors or corrupted bits. To achieve this, the data link layer uses various techniques for error detection and correction.

Error detection is the process of identifying or locating an error in the data frame. Error correction is the process of recovering or correcting the original data frame from the erroneous one.

The basic approach for error detection and correction is the use of redundancy, where additional bits are added to the data frame to facilitate the detection and correction of errors. These additional bits are called error control bits or check bits.

There are three main techniques for error detection and correction in the data link layer:

- Parity check
- Checksum
- Cyclic redundancy check (CRC)

The following diagram illustrates the basic architecture of error detection and correction in the data link layer:

```
+-----------------+       +-----------------+
|                 |       |                 |
|   Data source   |       |   Data sink     |
|                 |       |                 |
+-----------------+       +-----------------+
        |                         ^
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-----------------+       +-----------------+
|                 |       |                 |
|   Data link     |       |   Data link     |
|   layer         |       |   layer         |
|                 |       |                 |
+-----------------+       +-----------------+
        |                         ^
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-----------------+       +-----------------+
|                 |       |                 |
|   Physical      |       |   Physical      |
|   layer         |       |   layer         |
|                 |       |                 |
+-----------------+       +-----------------+
        |                         ^
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|   Transmission  |       |   Transmission  |
|   medium        |       |   medium        |
|                 |       |                 |
+-----------------+       +-----------------+
```

The data source generates the data frames and passes them to the data link layer. The data link layer adds the error control bits to the data frames and sends them to the physical layer. The physical layer converts the data frames into electrical signals and transmits them over the transmission medium. The transmission medium may introduce errors or noise in the signals due to various factors such as interference, attenuation, distortion, etc. The physical layer at the receiver side receives the signals and converts them back into data frames. The data link layer at the receiver side checks the error control bits and detects any errors in the data frames. If the errors are detected, the data link layer may request the sender to retransmit the data frames or attempt to correct the errors using the error control bits. The data link layer then passes the corrected data frames to the data sink. The data sink receives the data frames and processes them.