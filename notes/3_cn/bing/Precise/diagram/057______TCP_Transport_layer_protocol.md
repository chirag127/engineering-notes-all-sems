#### TCP Transport layer protocol

```
  +---------------------+
  |  Application Layer  |
  +---------------------+
           |
           |
           V
  +---------------------+
  |    Transport Layer  |
  +---------------------+
  |                     |
  |    +----------+     |
  |    |   TCP    |     |
  |    +----------+     |
  |                     |
  +---------------------+
           |
           |
           V
  +---------------------+
  |   Network Layer     |
  +---------------------+
           |
           |
           V
  +---------------------+
  |   Data Link Layer   |
  +---------------------+
           |
           |
           V
  +---------------------+
  |   Physical Layer    |
  +---------------------+
```

TCP (Transmission Control Protocol) is one of the main protocols in the Transport Layer of the OSI model. It provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating via an IP network. Major internet applications such as the World Wide Web, email, remote administration, and file transfer rely on TCP.