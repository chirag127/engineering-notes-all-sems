I am Sydney, your AI assistant. I can help you with drawing a detailed ASCII diagram for detection and resolution of distributed deadlock for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

The following diagram illustrates the basic architecture of a distributed deadlock detection and resolution system. It consists of four components: a local deadlock detector (LDD), a global deadlock detector (GDD), a deadlock resolution manager (DRM), and a communication network (CN).

The LDD is responsible for detecting local deadlocks within each site, using a wait-for graph (WFG) or other methods. The LDD also sends and receives messages from the GDD and the DRM.

The GDD is responsible for detecting global deadlocks among different sites, using path-pushing, edge-chasing, diffusion computation, or global state detection algorithms. The GDD also sends and receives messages from the LDDs and the DRM.

The DRM is responsible for resolving the detected deadlocks, by aborting or rolling back some of the deadlocked processes and releasing their resources. The DRM also sends and receives messages from the LDDs and the GDD.

The CN is responsible for providing reliable and efficient communication among the LDDs, the GDD, and the DRM.

The diagram is drawn using ASCII characters, where:

- P represents a process
- R represents a resource
- -> represents a request edge
- <- represents an allocation edge
- | represents a vertical line
- - represents a horizontal line
- + represents a connection point
- / represents a diagonal line
- * represents a message

The diagram is as follows:

```
    LDD1     LDD2     LDD3     LDD4
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     |        |        |        |
     +--------+--------+--------+--------+
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     +--------+--------+--------+--------+
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     +--------+--------+--------+--------+
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     +--------+--------+--------+--------+
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     +--------+--------+--------+--------+
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        | CN
     |        |        |        |        |
     +--------+--------+--------+--------+
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        | GDD
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     |        |        |        |        |
     +--------+--------+--------+--------+