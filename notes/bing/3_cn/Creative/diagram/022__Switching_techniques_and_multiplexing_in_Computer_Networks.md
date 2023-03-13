Switching techniques and multiplexing are two concepts in computer networks that are related to how data is transmitted over a shared medium. Switching techniques are methods of establishing and maintaining a connection between two nodes in a network, while multiplexing is a method of combining multiple signals into one signal over a shared medium.

There are three main types of switching techniques: circuit switching, message switching, and packet switching. Circuit switching is a technique where a dedicated communication path is established between two nodes for the duration of the communication. Message switching is a technique where the whole message is treated as a data unit and stored and forwarded by intermediate nodes until it reaches the destination. Packet switching is a technique where the message is broken down into smaller chunks called packets and routed independently by intermediate nodes until they reach the destination.

Multiplexing can be done in different ways, such as frequency division multiplexing (FDM), time division multiplexing (TDM), and statistical multiplexing. FDM is a technique where the frequency spectrum of the shared medium is divided into several non-overlapping frequency bands, and each signal is modulated by a different carrier frequency. TDM is a technique where the time axis of the shared medium is divided into several time slots, and each signal is assigned a different time slot. Statistical multiplexing is a technique where the shared medium is dynamically allocated to the signals based on their demand and availability.

The following diagram illustrates the basic architecture of a switching technique and a multiplexing technique in computer networks:

```
+--------+     +--------+     +--------+     +--------+
|        |     |        |     |        |     |        |
| Node A +---->+ Switch +---->+ Mux    +---->+ Node B |
|        |     |        |     |        |     |        |
+--------+     +--------+     +--------+     +--------+
                   |              |
                   |              |
                   |              |
                   |              |
                   |              |
                   |              |
                   |              |
                   |              |
+--------+     +--------+     +--------+     +--------+
|        |     |        |     |        |     |        |
| Node C +---->+ Switch +---->+ Mux    +---->+ Node D |
|        |     |        |     |        |     |        |
+--------+     +--------+     +--------+     +--------+
```

In this diagram, Node A and Node C are sending data to Node B and Node D, respectively. The switch is responsible for establishing and maintaining a connection between the nodes, using one of the switching techniques. The mux is responsible for combining the data from the switch into one signal, using one of the multiplexing techniques. The signal is then transmitted over the shared medium to the destination node, where it is demultiplexed and delivered to the receiver.