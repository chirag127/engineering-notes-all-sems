Transport layer protocols are methods that provide end-to-end communication services for applications over a network. The most common transport layer protocols in the Internet protocol suite are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). TCP provides reliable, ordered, and error-checked delivery of data, while UDP provides fast and efficient delivery of data, but without any guarantee of reliability or order. Both TCP and UDP use port numbers to identify the source and destination applications of the data.

### Transport layer protocols

```
+-----------------+-----------------+-----------------+
| Application     | Application     | Application     |
+-----------------+-----------------+-----------------+
| TCP             | UDP             | Other           |
+-----------------+-----------------+-----------------+
| IP              | IP              | IP              |
+-----------------+-----------------+-----------------+
| Data link layer | Data link layer | Data link layer |
+-----------------+-----------------+-----------------+
| Physical layer  | Physical layer  | Physical layer  |
+-----------------+-----------------+-----------------+
```