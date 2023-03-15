# Switching techniques and multiplexing

Switching techniques and multiplexing are two important concepts in computer networks that enable efficient and reliable data transmission over shared communication channels.

## Switching techniques

Switching techniques are methods of establishing and maintaining a connection between two or more nodes in a network. There are three main types of switching techniques: circuit switching, message switching, and packet switching.

### Circuit switching

Circuit switching is a switching technique in which two nodes communicate with each other over a dedicated communication path. The path is established before the data transmission begins and remains active until the communication is terminated. The path consists of a series of physical links and switches that are reserved exclusively for the two nodes. Circuit switching is commonly used for voice communication, such as telephone calls.

Some advantages of circuit switching are:

- It guarantees a fixed and constant bandwidth for the duration of the communication.
- It provides low and predictable latency and jitter, as there is no queuing or buffering of data.
- It ensures high quality and reliability of data transmission, as there is no interference or congestion from other nodes.

Some disadvantages of circuit switching are:

- It wastes bandwidth, as the reserved path is not used by other nodes when there is no data to transmit.
- It is inefficient for bursty or variable data, as the bandwidth cannot be adjusted according to the data rate.
- It is expensive and complex to establish and maintain the dedicated path, as it requires coordination and signaling among the switches.

### Message switching

Message switching is a switching technique in which the whole message is treated as a data unit. The message is stored and forwarded by each switch along the path from the source to the destination. The message is divided into fixed-length blocks, each with a header containing the destination address and other information. The switches use the header to route the message to the next switch, until it reaches the destination. Message switching is suitable for non-real-time applications, such as email.

Some advantages of message switching are:

- It does not require a dedicated path or a prior connection between the nodes, which reduces the overhead and complexity of the switching process.
- It utilizes the bandwidth efficiently, as the switches can buffer the messages and transmit them when the channel is available.
- It is robust and fault-tolerant, as the switches can store the messages and retransmit them in case of link failures or congestion.

Some disadvantages of message switching are:

- It introduces variable and unpredictable latency and jitter, as the messages may be delayed or reordered by the switches due to queuing or buffering.
- It consumes more storage and processing resources at the switches, as the messages have to be stored and forwarded by each switch.
- It may cause duplication or loss of messages, as the switches may not have enough buffer space or may discard the messages due to errors or timeouts.

### Packet switching

Packet switching is a switching technique that is derived from message switching, where the message is broken down into smaller chunks called packets. The packets are transmitted independently and asynchronously over the network, without requiring a dedicated path or a prior connection between the nodes. The packets may follow different routes and arrive at different times at the destination, where they are reassembled into the original message. Packet switching is widely used for data communication, such as the Internet.

Some advantages of packet switching are:

- It is more efficient and flexible than circuit switching, as it can adapt to the dynamic and variable nature of data traffic.
- It can support multiple applications and services over the same network, as it can multiplex and demultiplex different types of packets based on their headers.
- It can provide better performance and reliability than message switching, as it can use error detection and correction techniques, flow control and congestion control mechanisms, and routing algorithms to optimize the data transmission.

Some disadvantages of packet switching are:

- It may cause variable and unpredictable latency and jitter, as the packets may be delayed or reordered by the network due to queuing, buffering, or routing.
- It may cause overhead and fragmentation, as the packets have to be encapsulated and decapsulated with headers and trailers, and may have to be split and reassembled due to size limitations.
- It may cause security and privacy issues, as the packets may be intercepted, modified, or spoofed by malicious nodes or attackers.

## Multiplexing

Multiplexing is a technique of combining multiple signals into one signal over a shared medium. The signals may be analog or digital, and may have different frequencies, data rates, or formats. The multiplexer (MUX) is the device that performs the multiplexing function at the source end, and the demultiplexer (DEMUX) is the device