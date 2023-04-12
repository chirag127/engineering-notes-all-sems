Multiplexing in transport layer is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver . The headers contain the source and destination port numbers, which are used to identify the application processes at the end hosts. The transport layer uses the host-to-host delivery service provided by the network layer to send the segments to the receiver.

Demultiplexing in transport layer is the reverse process of multiplexing. It is the process of delivering the data in each segment to the correct application process at the receiver . The transport layer uses the port numbers in the headers to determine which application process should receive the data. The transport layer can also perform error detection and correction, flow control, congestion control, and reliability services depending on the protocol used .

A diagram for multiplexing and demultiplexing in transport layer is shown below  . The diagram assumes that the transport layer protocol is TCP, which uses a connection-oriented service. The diagram also shows the network layer protocol as IP, which uses a connectionless service.

### Multiplexing in transport layer

```
    +----------------+    +----------------+    +----------------+
    | Application 1  |    | Application 2  |    | Application 3  |
    +----------------+    +----------------+    +----------------+
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             +---------------------+---------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
    +----------------+    +----------------+    +----------------+
    | Transport      |    | Transport      |    | Transport      |
    | Layer          |    | Layer          |    | Layer          |
    | (TCP)          |    | (TCP)          |    | (TCP)          |
    +----------------+    +----------------+    +----------------+
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             +---------------------+---------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
    +----------------+    +----------------+    +----------------+
    | Network        |    | Network        |    | Network        |
    | Layer          |    | Layer          |    | Layer          |
    | (IP)           |    | (IP)           |    | (IP)           |
    +----------------+    +----------------+    +----------------+
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             +---------------------+---------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
    +----------------+    +----------------+    +----------------+
    | Data Link      |    | Data Link      |    | Data Link      |
    | Layer          |    | Layer          |    | Layer          |
    +----------------+    +----------------+    +----------------+
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |

```
