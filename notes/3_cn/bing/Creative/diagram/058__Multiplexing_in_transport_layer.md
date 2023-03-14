Multiplexing in transport layer is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.   The headers include the source port number and the destination port number, which identify the application processes involved in the communication.  

Demultiplexing in transport layer is the process of delivering the received segments to the correct application processes at the receiver side.   The receiver uses the destination port number in the segment header to determine which application process should receive the data.  

The following diagram illustrates the basic architecture of multiplexing and demultiplexing in transport layer:

```
    +-----------------+        +-----------------+
    | Application A   |        | Application A   |
    +-----------------+        +-----------------+
    | Source port: X  |        | Dest. port: X   |
    +-----------------+        +-----------------+
    | Application B   |        | Application B   |
    +-----------------+        +-----------------+
    | Source port: Y  |        | Dest. port: Y   |
    +-----------------+        +-----------------+
    | Application C   |        | Application C   |
    +-----------------+        +-----------------+
    | Source port: Z  |        | Dest. port: Z   |
    +-----------------+        +-----------------+
    | Transport layer |        | Transport layer |
    +-----------------+        +-----------------+
    | Source IP: S    |        | Dest. IP: S     |
    +-----------------+        +-----------------+
    | Dest. IP: D     |        | Source IP: D    |
    +-----------------+        +-----------------+
    | Network layer   |        | Network layer   |
    +-----------------+        +-----------------+
    | Link layer      |        | Link layer      |
    +-----------------+        +-----------------+
    | Physical layer  |        | Physical layer  |
    +-----------------+        +-----------------+
       Sender side                 Receiver side
```