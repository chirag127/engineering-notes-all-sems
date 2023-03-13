Quality of service (QoS) in transport layer is the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity. It enables organizations to adjust their overall network traffic by prioritizing specific high-performance applications.

The transport layer establishes the transport connection by sending a request. For establishing a link, it uses the T-CONNECT service primitives. The transport entity provides the quality of service, requirement, and collect addresses services.

The following diagram illustrates the basic architecture of a QoS-enabled transport layer using the TCP/IP model:

```
+-----------------+-----------------+-----------------+
| Application     | Application     | Application     |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Transport    |    Transport    |    Transport    |
|    (TCP/UDP)    |    (TCP/UDP)    |    (TCP/UDP)    |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Internet     |    Internet     |    Internet     |
|    (IP)         |    (IP)         |    (IP)         |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Network      |    Network      |    Network      |
|    Access       |    Access       |    Access       |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Physical     |    Physical     |    Physical     |
+-----------------+-----------------+-----------------+
```

The transport layer can provide QoS by using different protocols, such as TCP or UDP, or by using different mechanisms, such as congestion control, rate control, or reliable data transport. The transport layer can also use QoS parameters, such as delay, jitter, throughput, or packet loss, to measure and adjust the performance of the network .