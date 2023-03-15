#### ICMP

- ICMP stands for Internet Control Message Protocol.
- ICMP is a network layer protocol that is used by network devices to communicate problems with data transmission.
- ICMP messages are typically used for diagnostic or control purposes or generated in response to errors in IP operations.
- ICMP messages have a header and a payload. The header contains the type, code, and checksum of the message. The payload contains additional information, such as the IP header and the first 8 bytes of the original datagram that caused the error.
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the reachability and round-trip time of a destination.
  - Destination unreachable: used to inform the source that the destination or the route to the destination is unreachable for some reason.
  - Time exceeded: used to inform the source that the datagram has expired in transit due to a hop limit or a reassembly timeout.
  - Parameter problem: used to inform the source that the datagram has an invalid or missing field in the IP header.
  - Source quench: used to inform the source that the destination or an intermediate router is experiencing congestion and requests the source to reduce its sending rate.
  - Redirect: used to inform the source that there is a better route to the destination and suggests the source to use a different gateway.
  - Timestamp request and timestamp reply: used to measure the time difference between the source and the destination.
  - Address mask request and address mask reply: used to obtain the subnet mask of a destination.