# Switching techniques and multiplexing

Switching techniques and multiplexing are two important concepts in computer networks that enable efficient and reliable data transmission over shared communication channels.

## Switching techniques

Switching techniques are methods of connecting multiple devices or nodes in a network and allowing them to communicate with each other. There are three main types of switching techniques: circuit switching, message switching, and packet switching.

### Circuit switching

Circuit switching is a switching technique in which two nodes establish a dedicated communication path or circuit before transmitting any data. The circuit remains active until the communication is terminated by either node. Circuit switching is suitable for real-time applications that require constant and uninterrupted data flow, such as voice calls or video streaming. However, circuit switching also has some disadvantages, such as:

- It requires a lot of resources and bandwidth to maintain the circuit, which may result in wastage if the circuit is idle or underutilized.
- It is not flexible or scalable, as the number of circuits is limited by the physical capacity of the network and the availability of switching nodes.
- It is vulnerable to failures or congestion, as any disruption in the circuit can cause the entire communication to fail.

### Message switching

Message switching is a switching technique in which the whole message is treated as a data unit and stored and forwarded by intermediate nodes until it reaches the destination node. Message switching does not require a dedicated circuit, but rather uses the available network resources on a hop-by-hop basis. Message switching is suitable for applications that do not require real-time or reliable data delivery, such as email or file transfer. However, message switching also has some disadvantages, such as:

- It introduces a lot of delay and overhead, as the message has to be stored, processed, and forwarded by each node along the path.
- It is not efficient for large or long messages, as they may occupy a lot of buffer space and bandwidth at each node.
- It is not compatible with heterogeneous networks, as the message format and size may vary across different nodes and protocols.

### Packet switching

Packet switching is a switching technique that is derived from message switching, where the message is broken down into smaller chunks called packets. Each packet has a header that contains the source and destination addresses, as well as other information such as sequence number, checksum, and payload length. Packets are routed independently by each node based on the destination address and the network conditions. Packet switching is suitable for applications that require high efficiency and flexibility, such as web browsing or online gaming. However, packet switching also has some disadvantages, such as:

- It may cause packet loss, duplication, or reordering, as packets may take different paths or encounter errors or congestion along the way.
- It may cause packet delay or jitter, as packets may experience different waiting times or processing times at each node.
- It may require additional mechanisms or protocols to ensure reliable and ordered data delivery, such as error detection, correction, and acknowledgment.

## Multiplexing

Multiplexing is a technique of combining multiple signals into one signal over a shared medium. Multiplexing allows the efficient utilization of the available bandwidth and reduces the cost and complexity of the network. There are four main types of multiplexing: frequency division multiplexing (FDM), time division multiplexing (TDM), wavelength division multiplexing (WDM), and code division multiplexing (CDM).

### Frequency division multiplexing (FDM)

FDM is a multiplexing technique in which the frequency spectrum of the shared medium is divided into several non-overlapping frequency bands, and each signal is modulated by a different carrier frequency within its assigned band. FDM allows the simultaneous transmission of multiple analog or digital signals over a single medium, such as a coaxial cable or a radio channel. However, FDM also has some disadvantages, such as:

- It requires a lot of bandwidth and filtering, as the frequency bands have to be sufficiently separated and isolated to avoid interference or crosstalk.
- It is not adaptive or dynamic, as the frequency bands are fixed and predetermined, and cannot be changed according to the demand or quality of the signals.

### Time division multiplexing (TDM)

TDM is a multiplexing technique in which the time axis of the shared medium is divided into several equal time slots, and each signal is assigned a different time slot within each cycle. TDM allows the sequential transmission of multiple digital signals over a single medium, such as a twisted pair or an optical fiber. However, TDM also has some disadvantages, such as:

- It requires a lot of synchronization and buffering, as the signals have to be aligned and buffered at