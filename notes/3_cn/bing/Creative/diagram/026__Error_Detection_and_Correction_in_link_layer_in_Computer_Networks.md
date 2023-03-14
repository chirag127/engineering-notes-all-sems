#### Error Detection and Correction in link layer in Computer Networks

The data link layer uses error control techniques to ensure that frames, i.e. bit streams of data, are transmitted from the source to the destination with a certain extent of accuracy. Errors can occur due to noise or other impairments during transmission, which can corrupt or lose some bits in the frames. The data link layer uses various error detection and correction techniques to detect or identify and re-transmit data frames that might be corrupted or lost. The basic approach is the use of redundancy, where additional bits are added to facilitate the detection and correction of errors.

The following diagram illustrates the basic architecture of error detection and correction in link layer in computer networks:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Application   |       |   Application   |       |   Application   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Transport     |       |   Transport     |       |   Transport     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Network       |       |   Network       |       |   Network       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Data Link     |       |   Data Link     |       |   Data Link     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Physical      |       |   Physical      |       |   Physical      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       +-----------------+       +-----------------+       +-----------------+
       |                 |       |                 |       |                 |
       |   Physical      |       |   Physical      |       |   Physical      |
       |                 |       |                 |       |                 |
       +-----------------+       +-----------------+       +-----------------+
       |                 |       |                 |       |                 |
       |   Data Link     |       |   Data Link     |       |   Data Link     |
       |                 |       |                 |       |                 |
       +-----------------+       +-----------------+       +-----------------+
       |                 |       |                 |       |                 |
       |   Network       |       |   Network       |       |   Network       |
       |                 |       |                 |       |                 |
       +-----------------+       +-----------------+       +-----------------+
       |                 |       |                 |       |                 |
       |   Transport     |       |   Transport     |       |   Transport     |
       |                 |       |                 |       |                 |
       +-----------------+       +-----------------+       +-----------------+
       |                 |       |                 |       |                 |
       |   Application   |       |   Application   |       |   Application   |
       |                 |       |                 |       |                 |
       +-----------------+       +-----------------+       +-----------------+
```

The data link layer at the source node adds some additional bits to the data frame, called error control bits, which are calculated based on the data bits using some error detection or correction scheme. The data link layer at the destination node checks the received frame for errors using the same scheme and the error control bits. If no errors are detected, the data link layer at the destination node removes the error control bits and passes the data bits to the upper layer. If errors are detected, the data link layer at the