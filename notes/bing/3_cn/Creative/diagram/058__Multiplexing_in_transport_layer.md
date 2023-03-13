Multiplexing in transport layer is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver . The transport layer uses port numbers to identify the source and destination processes of the data. The port numbers are added to the transport layer header along with other information such as sequence number, acknowledgement number, checksum, etc. The transport layer header is then encapsulated with the network layer header and sent to the network layer for transmission.

Demultiplexing in transport layer is the reverse process of multiplexing. It is the process of delivering the data to the correct application process at the receiver side . The transport layer uses the port numbers in the transport layer header to identify the destination process of the data. The transport layer removes the transport layer header and passes the data to the corresponding socket.

The following diagram illustrates the basic architecture of multiplexing and demultiplexing in transport layer:

```
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 1       |       | Process 1       |
    +-----------------+       +-----------------+
    | Socket 1        |       | Socket 1        |
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 2       |       | Process 2       |
    +-----------------+       +-----------------+
    | Socket 2        |       | Socket 2        |
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 3       |       | Process 3       |
    +-----------------+       +-----------------+
    | Socket 3        |       | Socket 3        |
    +-----------------+       +-----------------+
    | Transport Layer |       | Transport Layer |
    +-----------------+       +-----------------+
    | Network Layer   |       | Network Layer   |
    +-----------------+       +-----------------+
    | Link Layer      |       | Link Layer      |
    +-----------------+       +-----------------+
    | Physical Layer  |       | Physical Layer  |
    +-----------------+       +-----------------+
    |                 |       |                 |
    |     Sender      |       |    Receiver     |
    |                 |       |                 |
    +-----------------+       +-----------------+
```

The transport layer at the sender side performs multiplexing by collecting the data from different sockets and adding port numbers and other information to the transport layer header. The transport layer at the receiver side performs demultiplexing by extracting the port numbers from the transport layer header and delivering the data to the appropriate socket.

### Multiplexing in transport layer

```
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 1       |       | Process 1       |
    +-----------------+       +-----------------+
    | Socket 1        |       | Socket 1        |
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 2       |       | Process 2       |
    +-----------------+       +-----------------+
    | Socket 2        |       | Socket 2        |
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 3       |       | Process 3       |
    +-----------------+       +-----------------+
    | Socket 3        |       | Socket 3        |
    +-----------------+       +-----------------+
    | Transport Layer |       | Transport Layer |
    +-----------------+       +-----------------+
    | Network Layer   |       | Network Layer   |
    +-----------------+       +-----------------+
    | Link Layer      |       | Link Layer      |
    +-----------------+       +-----------------+
    | Physical Layer  |       | Physical Layer  |
    +-----------------+       +-----------------+
    |                 |       |                 |
    |     Sender      |       |    Receiver     |
    |                 |       |                 |
    +-----------------+       +-----------------+
          |  |  |                   |  |  |
          |  |  |                   |  |  |
          |  |  |                   |  |  |
          |  |  |                   |