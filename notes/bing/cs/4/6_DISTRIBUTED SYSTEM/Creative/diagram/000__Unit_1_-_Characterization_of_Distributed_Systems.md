## Unit 1 - Characterization of Distributed Systems

A distributed system is a system that consists of multiple components located at different networked computers that communicate and coordinate their actions only by passing messages. Some of the key characteristics of distributed systems are  :

- Scalability: the ability of the system to grow and manage increased demand without affecting the performance or functionality.
- Reliability: the probability that the system will not fail in a given period of time.
- Availability: the time that the system remains operational and able to perform its required functions in a specific period of time.
- Efficiency: the ratio of the output to the input of the system, such as the throughput, latency, or resource utilization.
- Manageability: the ease of monitoring, controlling, and maintaining the system.

The following diagram illustrates the basic architecture of a distributed system using the client-server model, where clients request services from servers and servers provide services to clients. The clients and servers can be located on different machines and communicate through a network.

```
    +--------+       +--------+       +--------+
    | Client |       | Client |       | Client |
    +--------+       +--------+       +--------+
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        +---------------------------------+
        |             Network             |
        +---------------------------------+
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
    +--------+       +--------+       +--------+
    | Server |       | Server |       | Server |
    +--------+       +--------+       +--------+
```