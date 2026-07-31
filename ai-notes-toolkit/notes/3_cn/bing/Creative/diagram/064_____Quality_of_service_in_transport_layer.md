Quality of service (QoS) in transport layer is the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity. It enables organizations to adjust their overall network traffic by prioritizing specific high-performance applications.

The transport layer establishes the transport connection by sending a request. For establishing a link, it uses the T-CONNECT service primitives. The transport entity provides the quality of service, requirement, and collect addresses services. In the internet, these end points are pairs of IP addresses and port numbers.

A possible ASCII diagram for quality of service in transport layer is:

### Quality of service in transport layer

```
+----------------+      +----------------+      +----------------+
| Application    |      | Application    |      | Application    |
| Layer          |      | Layer          |      | Layer          |
+----------------+      +----------------+      +----------------+
| Transport      |      | Transport      |      | Transport      |
| Layer          |      | Layer          |      | Layer          |
+----------------+      +----------------+      +----------------+
| Network        |      | Network        |      | Network        |
| Layer          |      | Layer          |      | Layer          |
+----------------+      +----------------+      +----------------+
| Data Link      |      | Data Link      |      | Data Link      |
| Layer          |      | Layer          |      | Layer          |
+----------------+      +----------------+      +----------------+
| Physical       |      | Physical       |      | Physical       |
| Layer          |      | Layer          |      | Layer          |
+----------------+      +----------------+      +----------------+

    ^                      ^                      ^
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    |                      |                      |
    v                      v                      v

+----------------+      +----------------+      +----------------+
| IP Address     |      | IP Address     |      | IP Address     |
| and Port       |      | and Port       |      | and Port       |
| Number         |      | Number         |      | Number         |
+----------------+      +----------------+      +----------------+
| T-CONNECT      |      | T-CONNECT      |      | T-CONNECT      |
| Service        |      | Service        |      | Service        |
| Primitive      |      | Primitive      |      | Primitive      |
+----------------+      +----------------+      +----------------+
| QoS            |      | QoS            |      | QoS            |
| Requirement    |      | Requirement    |      | Requirement    |
+----------------+      +----------------+      +----------------+
| QoS            |      | QoS            |      | QoS            |
| Mechanism      |      | Mechanism      |      | Mechanism      |
+----------------+      +----------------+      +----------------+
```