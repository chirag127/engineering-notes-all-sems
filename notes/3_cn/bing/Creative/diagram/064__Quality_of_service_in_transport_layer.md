Quality of service (QoS) in transport layer is the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity. It enables organizations to adjust their overall network traffic by prioritizing specific high-performance applications. QoS is typically applied to networks that carry traffic for resource-intensive systems, such as streaming media, videoconferencing, and Voice over IP (VoIP) .

The transport layer establishes the transport connection by sending a request. For establishing a link, it uses the T-CONNECT service primitives. The transport entity provides the quality of service, requirement, and collect addresses services . The transport layer can also provide reliable data transport, congestion control, and rate control for different types of traffic .

The following diagram illustrates the basic architecture of a QoS-enabled transport layer:

```
+-----------------+   +-----------------+
| Application     |   | Application     |
| Layer           |   | Layer           |
+-----------------+   +-----------------+
| Transport       |   | Transport       |
| Layer           |   | Layer           |
+-----------------+   +-----------------+
| Network         |   | Network         |
| Layer           |   | Layer           |
+-----------------+   +-----------------+
| Data Link       |   | Data Link       |
| Layer           |   | Layer           |
+-----------------+   +-----------------+
| Physical        |   | Physical        |
| Layer           |   | Layer           |
+-----------------+   +-----------------+
|                 |   |                 |
|     Host A      |   |     Host B      |
|                 |   |                 |
+-----------------+   +-----------------+
```

The transport layer uses the network layer to send and receive packets across the network. The transport layer can mark packets to identify service types, then configure routers to create separate virtual queues for each application, based on their priority. As a result, bandwidth is reserved for critical applications or websites that have been assigned priority access . The transport layer can also use different protocols, such as Transmission Control Protocol (TCP) or User Datagram Protocol (UDP), to provide different levels of reliability, ordering, and error control for different types of traffic .