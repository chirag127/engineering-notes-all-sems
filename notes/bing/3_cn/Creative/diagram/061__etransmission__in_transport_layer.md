The transport layer is responsible for providing reliable and efficient communication between end-to-end applications. One of the functions of the transport layer is to ensure that the data is transmitted without any error, loss, duplication or corruption. This is achieved by using error control mechanisms such as retransmission, segmentation, acknowledgement and checksum  .

Etransmission is a term that refers to the process of retransmitting a packet that was lost, delayed or corrupted during the transmission. The transport layer uses a retransmission timer to determine when to resend a packet. The retransmission timer is set based on the round-trip time (RTT) of the packet, which is the time it takes for a packet to travel from the sender to the receiver and back. The retransmission timer is usually a multiple of the RTT, such as 2*RTT or 3*RTT. If the sender does not receive an acknowledgement (ACK) from the receiver before the retransmission timer expires, it assumes that the packet was lost and resends it.

The following diagram illustrates the basic process of etransmission in the transport layer using the Transmission Control Protocol (TCP) as an example :

```
Sender                          Receiver
|                               |
|  Segment 1 (Seq=1, ACK=0)     |
|------------------------------>|  Segment 1 received, checksum OK
|                               |  ACK 1 (Seq=0, ACK=1)
|<------------------------------|  ACK 1 sent
|  ACK 1 received               |
|                               |
|  Segment 2 (Seq=2, ACK=1)     |
|------------------------------>|  Segment 2 received, checksum OK
|                               |  ACK 2 (Seq=1, ACK=2)
|<------------------------------|  ACK 2 sent
|  ACK 2 received               |
|                               |
|  Segment 3 (Seq=3, ACK=2)     |
|------------------------------>|  Segment 3 lost or corrupted
|                               |  No ACK 3 sent
|  Segment 4 (Seq=4, ACK=2)     |
|------------------------------>|  Segment 4 received, checksum OK
|                               |  ACK 2 (Seq=2, ACK=2)
|<------------------------------|  ACK 2 resent (duplicate ACK)
|  ACK 2 received (duplicate)   |
|                               |
|  Segment 5 (Seq=5, ACK=2)     |
|------------------------------>|  Segment 5 received, checksum OK
|                               |  ACK 2 (Seq=3, ACK=2)
|<------------------------------|  ACK 2 resent (duplicate ACK)
|  ACK 2 received (duplicate)   |
|                               |
|  Segment 6 (Seq=6, ACK=2)     |
|------------------------------>|  Segment 6 received, checksum OK
|                               |  ACK 2 (Seq=4, ACK=2)
|<------------------------------|  ACK 2 resent (duplicate ACK)
|  ACK 2 received (duplicate)   |
|                               |
|  Retransmission timer expires |
|                               |
|  Segment 3 (Seq=3, ACK=2)     |
|------------------------------>|  Segment 3 received, checksum OK
|                               |  ACK 6 (Seq=5, ACK=6)
|<------------------------------|  ACK 6 sent (cumulative ACK)
|  ACK 6 received               |
|                               |
|  Segment 7 (Seq=7, ACK=6)     |
|------------------------------>|  Segment 7 received, checksum OK
|                               |  ACK 7 (Seq=6, ACK=7)
|<------------------------------|  ACK 7 sent
|  ACK 7 received               |
|                               |
```