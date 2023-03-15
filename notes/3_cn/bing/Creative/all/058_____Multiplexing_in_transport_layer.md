# Multiplexing in transport layer

Multiplexing in transport layer is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver. Multiplexing in transport layer extends the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts.

Some points to remember about multiplexing in transport layer are:

- Multiplexing in transport layer requires that sockets have unique identifiers, and each segment have special fields that indicate the sockets to which the segment is to be delivered.
- Multiplexing in transport layer can be connectionless or connection-oriented, depending on the transport protocol used.
- Connectionless multiplexing uses port numbers to identify the sockets, and includes the source and destination port numbers in the segment header.
- Connection-oriented multiplexing uses a combination of port numbers and socket numbers to identify the sockets, and includes the source and destination socket numbers in the segment header.
- Multiplexing in transport layer allows multiple applications to share the same network resources and communicate with different destinations simultaneously.
- Multiplexing in transport layer is performed by the transport layer protocols, such as UDP and TCP.