# Switching techniques and multiplexing

Switching techniques and multiplexing are two important concepts in computer networks that enable efficient and reliable data transmission over shared communication channels.

## Switching techniques

Switching techniques are methods of establishing and maintaining a connection between two or more nodes in a network. There are three main types of switching techniques: circuit switching, message switching, and packet switching.

### Circuit switching

Circuit switching is a switching technique in which two nodes communicate with each other over a dedicated communication path. The path is established before the data transmission begins and remains active until the transmission ends. The path consists of a series of physical links and switches that are reserved exclusively for the two nodes. Circuit switching is commonly used for voice communication, such as telephone calls.

Some advantages of circuit switching are:

- It guarantees a fixed and constant bandwidth for the duration of the connection.
- It provides low and predictable latency and jitter for the data transmission.
- It avoids congestion and packet loss, as no other nodes can use the reserved path.

Some disadvantages of circuit switching are:

- It wastes bandwidth, as the path remains idle when no data is transmitted.
- It is inefficient for bursty or variable data, as the bandwidth cannot be adjusted dynamically.
- It is costly and complex to establish and maintain the connection.

### Message switching

Message switching is a switching technique in which the whole message is treated as a data unit. The message is stored and forwarded by each intermediate node along the path until it reaches the destination node. The path is not predetermined or reserved, but chosen dynamically based on the availability and capacity of the links and switches. Message switching is suitable for non-real-time and asynchronous communication, such as email.

Some advantages of message switching are:

- It utilizes the bandwidth efficiently, as the links and switches are shared by multiple nodes.
- It adapts to the network conditions, as the path can be changed or rerouted in case of congestion or failure.
- It is simple and flexible, as no connection setup or teardown is required.

Some disadvantages of message switching are:

- It introduces variable and unpredictable latency and jitter for the data transmission, as the message may be delayed or queued at each node.
- It may cause duplication or loss of messages, as the nodes may not have enough storage or buffer space.
- It is not suitable for real-time or synchronous communication, as the message delivery is not guaranteed.

### Packet switching

Packet switching is a switching technique that is derived from message switching, where the message is broken down into smaller chunks called packets. The packets are transmitted independently and may follow different paths to reach the destination node. The packets are reassembled and ordered at the destination node based on the information in their headers. Packet switching is widely used for data communication over the internet.

Some advantages of packet switching are:

- It optimizes the bandwidth utilization, as the packets can fill the gaps and use the available capacity of the links and switches.
- It enhances the reliability and robustness of the network, as the packets can avoid or recover from congestion or failure by taking alternative paths.
- It supports variable and dynamic data, as the packets can be adjusted in size and frequency according to the data rate and quality.

Some disadvantages of packet switching are:

- It introduces overhead and complexity, as the packets need to be encapsulated, routed, and reassembled at each node.
- It may cause packet loss, delay, or reordering, as the packets may encounter congestion, errors, or out-of-sequence delivery.
- It may require additional mechanisms or protocols to ensure the quality of service, such as error detection, flow control, or congestion control.

## Multiplexing

Multiplexing is a technique of combining multiple signals into one signal over a shared medium. Multiplexing allows the simultaneous transmission of multiple signals across a single data link, which increases the efficiency and reduces the cost of the network. There are different types of multiplexing techniques, such as frequency division multiplexing (FDM), time division multiplexing (TDM), and statistical multiplexing.

### Frequency division multiplexing (FDM)

Frequency division multiplexing (FDM) is a multiplexing technique that assigns a different frequency band to each signal. The signals are modulated by their respective frequencies and then added together to form a composite signal. The composite signal is transmitted over a single channel that has a bandwidth equal to the sum of the individual bandwidths. The signals are demodulated and separated by using filters at the receiver end.

Some advantages of FDM are:

- It is simple and easy to implement, as no synchronization or coordination is required between the signals.
-