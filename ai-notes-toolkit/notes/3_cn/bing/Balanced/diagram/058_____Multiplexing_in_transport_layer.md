Multiplexing in transport layer is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver . The headers contain the source and destination port numbers, which are used to identify the application processes at the end hosts. The transport layer uses these port numbers to multiplex and demultiplex the data segments between the network layer and the application layer.

A possible ASCII diagram for multiplexing in transport layer is:

### Multiplexing in transport layer

```
    +----------------+      +----------------+      +----------------+
    | Application 1  |      | Application 2  |      | Application 3  |
    +----------------+      +----------------+      +----------------+
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             +----------------------+----------------------+-----------------+
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             +----------------------+----------------------+-----------------+
             | Transport layer header (source port, destination port, etc.) |
             +---------------------------------------------------------------+
             | Data from application 1, 2, or 3                               |
             +---------------------------------------------------------------+
             | Transport layer trailer (checksum, etc.)                      |
             +---------------------------------------------------------------+
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             +----------------------+----------------------+-----------------+
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             +----------------------+----------------------+-----------------+
             | Network layer header (source IP, destination IP, etc.)        |
             +---------------------------------------------------------------+
             | Transport layer segment                                        |
             +---------------------------------------------------------------+
             | Network layer trailer (checksum, etc.)                        |
             +---------------------------------------------------------------+
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             +----------------------+----------------------+-----------------+
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             +----------------------+----------------------+-----------------+
             | Link layer header (source MAC, destination MAC, etc.)         |
             +---------------------------------------------------------------+
             | Network layer packet                                          |
             +---------------------------------------------------------------+
             | Link layer trailer (checksum, etc.)                           |
             +---------------------------------------------------------------+
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             +----------------------+----------------------+-----------------+
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             |                      |                      |                 |
             +----------------------+----------------------+-----------------+
             | Physical layer signal (bits, voltage, etc.)                   |
             +---------------------------------------------------------------+
```

The diagram shows how the transport layer collects the data from different application processes, adds a transport layer header and trailer, and passes the segment to the network layer. The network layer adds a network layer header and trailer, and passes the packet to the link layer. The link layer adds a link layer header and trailer, and passes the frame to the physical layer. The physical layer converts the frame into a signal and sends it over the medium. The process is reversed at the receiver side, where the transport layer uses the port numbers to demultiplex the data and deliver it to the correct application