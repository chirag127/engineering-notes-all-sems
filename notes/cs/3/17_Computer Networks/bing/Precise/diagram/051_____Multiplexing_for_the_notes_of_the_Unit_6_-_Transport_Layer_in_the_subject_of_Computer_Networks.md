### Multiplexing

Multiplexing is a method used in computer networks to improve transmission efficiency. It is the process of collecting data from multiple application processes of the sender, enveloping that data with headers, and sending them as a whole to the intended receiver . The transport layer uses multiplexing to extend the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts .

There are two ways in which multiplexing can occur:

1. **Upward Multiplexing**: Upward multiplexing means multiple transport layer connections use the same network connection .
2. **Downward Multiplexing**: Downward multiplexing means that a single transport layer connection uses multiple network connections.

Multiplexing and Demultiplexing services are provided in almost every protocol architecture ever designed. UDP and TCP perform the demultiplexing and multiplexing jobs by including two special fields in the segment headers: the source port number field and the destination port number field .