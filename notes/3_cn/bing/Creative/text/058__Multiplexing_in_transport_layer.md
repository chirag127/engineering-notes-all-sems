### Multiplexing in transport layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver. 
- Multiplexing extends the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts. 
- Multiplexing is done by including two special fields in the segment headers: the source port number field and the destination port number field. These fields identify the application processes that are sending and receiving the data. 
- There are two types of multiplexing in transport layer: connectionless multiplexing and connection-oriented multiplexing. 
- Connectionless multiplexing is used by UDP, which does not establish a connection before sending data. UDP segments are directed to the destination port number specified in the header, and the source port number is used for reply. 
- Connection-oriented multiplexing is used by TCP, which establishes a connection before sending data. TCP segments are directed to the destination port number specified in the header, and the source port number is used to identify the connection. TCP also uses sequence numbers and acknowledgment numbers to ensure reliable and ordered delivery of data. 
- Multiplexing allows multiple applications to share the same network resources and communicate with each other efficiently and reliably. 

: https://en.wikipedia.org/wiki/Transport_layer
: https://www.geeksforgeeks.org/multiplexing-and-demultiplexing-in-transport-layer/
: https://www.tutorialspoint.com/multiplexing-and-demultiplexing-in-transport-layer
: https://electronicspost.com/multiplexing-and-demultiplexing-in-transport-layer/
: https://www.alpharithms.com/multiplexing-demultiplexing-251217/