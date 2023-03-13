#### Switching techniques and multiplexing in Computer Networks

Switching techniques are methods of connecting multiple devices in a network and transferring data between them. Multiplexing is a technique of combining multiple signals into one signal over a shared medium. Switching and multiplexing are essential for efficient and reliable communication in computer networks.

There are three main types of switching techniques: circuit switching, message switching, and packet switching. Each of them has its own advantages and disadvantages, depending on the application and the network requirements.

- **Circuit switching**: In circuit switching, two nodes communicate with each other over a dedicated communication path. The path is established before the data transmission and remains active until the communication is over. The path consists of a series of physical links and switches that connect the source and the destination nodes. Circuit switching is suitable for real-time and continuous data transmission, such as voice and video calls. However, it has some drawbacks, such as high setup time, low bandwidth utilization, and vulnerability to link failures.

- **Message switching**: In message switching, the whole message is treated as a data unit. The message is stored and forwarded by intermediate nodes until it reaches the destination node. The message may take different paths and arrive out of order. The destination node is responsible for reassembling the message and checking for errors. Message switching is suitable for non-real-time and asynchronous data transmission, such as email and file transfer. However, it has some drawbacks, such as high delay, high storage requirement, and variable delivery time.

- **Packet switching**: The packet switching technique is derived from message switching, where the message is broken down into smaller chunks called packets. Each packet has a header that contains the source and destination addresses, the sequence number, and other information. The packets are routed independently by intermediate nodes based on the network conditions and the routing algorithms. Packet switching is suitable for both real-time and non-real-time data transmission, such as web browsing and streaming. However, it has some drawbacks, such as packet loss, packet delay, and packet reordering.

Multiplexing can be applied to any of the switching techniques to increase the efficiency and capacity of the network. There are different types of multiplexing techniques, such as frequency division multiplexing (FDM), time division multiplexing (TDM), and statistical multiplexing.

- **Frequency division multiplexing (FDM)**: In FDM, the available bandwidth of the medium is divided into several frequency bands. Each band is assigned to a different signal. The signals are modulated by different carrier frequencies and combined into one composite signal. The composite signal is transmitted over the medium and demodulated by the receiver. FDM is suitable for analog signals and constant bandwidth applications, such as radio and television broadcasting. However, it has some drawbacks, such as interference, crosstalk, and wastage of bandwidth.

- **Time division multiplexing (TDM)**: In TDM, the available time of the medium is divided into several time slots. Each slot is assigned to a different signal. The signals are sampled and multiplexed into one composite signal. The composite signal is transmitted over the medium and demultiplexed by the receiver. TDM is suitable for digital signals and synchronous applications, such as telephone and data networks. However, it has some drawbacks, such as synchronization, overhead, and fixed bandwidth allocation.

- **Statistical multiplexing**: Statistical multiplexing is a communication link sharing technique, which is used in packet switching. The shared linking is variable in statistical multiplexing, whereas it is fixed in TDM or FDM. This is a strategic application for maximizing the utilization of bandwidth. This can increase the efficiency of the network, as well. Statistical multiplexing is suitable for bursty and asynchronous applications, such as internet and multimedia. However, it has some drawbacks, such as congestion, queuing, and variable delay.

Some mnemonics and learning tricks for the switching techniques and multiplexing are:

- Circuit switching: **C**onstant and **C**ontinuous
- Message switching: **M**essage and **M**emory
- Packet switching: **P**acket and **P**ath
- Frequency division multiplexing: **F**requency and **F**ixed
- Time division multiplexing: **T**ime and **T**imed
- Statistical multiplexing: **S**tatistical and **S**hared

An example of a detailed ASCII diagram for packet switching is:

```
  Source Node                        Intermediate Node                        Destination Node
+--------------+                  +---------------------+                  +----------------+