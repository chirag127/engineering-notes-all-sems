### Multiplexing in transport layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver .
- Multiplexing extends the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts .
- Multiplexing takes a parallelized source of information and turns it into a serialized format.
- Multiplexing is done by adding a transport layer header to each data segment, which contains the source and destination port numbers that identify the corresponding application processes .
- The port numbers are 16-bit integers that range from 0 to 65535. Some port numbers are reserved for well-known services, such as HTTP (80), FTP (21), SMTP (25), etc .
- The transport layer header also contains other fields, such as sequence number, acknowledgment number, checksum, etc., depending on the protocol used (TCP or UDP) .
- The transport layer header and the data segment together form a transport layer segment, which is then passed to the network layer for further processing .
- An example of multiplexing in transport layer is shown below:

```
Application layer data from process A: Hello
Application layer data from process B: World
Transport layer header for process A: Source port = 1000, Destination port = 2000
Transport layer header for process B: Source port = 1001, Destination port = 2001
Transport layer segment for process A: 1000 2000 Hello
Transport layer segment for process B: 1001 2001 World
```

- A mnemonic to remember the concept of multiplexing in transport layer is: **M**any **P**rocesses **S**end **D**ata **S**egments (MPSDS).
- A learning trick to understand the concept of multiplexing in transport layer is to imagine a post office that collects letters from different senders, adds the addresses of the recipients, and sends them as a single package to another post office.