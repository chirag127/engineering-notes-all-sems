# System Models for Distributed Systems

A system model is a simplified representation of a distributed system that captures its essential properties and design choices. System models can help us understand, analyze, and reason about the behavior and performance of distributed systems. System models can be classified into three types:

- **Physical models**: capture the hardware composition of a system in terms of computers and other devices and their interconnecting network;
- **Interaction models**: capture the communication and coordination mechanisms between the components of a system, such as message passing, remote procedure calls, or shared memory;
- **Fault models**: capture the possible failures and errors that can occur in a system, such as node crashes, network partitions, or message losses.

Different system models can have different assumptions and guarantees about the properties of a distributed system, such as:

- **Network behavior**: how reliable, fast, and secure is the network that connects the components of a system;
- **Node behavior**: how reliable, fast, and secure are the nodes that run the components of a system;
- **Timing behavior**: how synchronized, accurate, and predictable are the clocks and timers of the nodes and the network;
- **Consensus behavior**: how easy or hard is it for the components of a system to agree on a common value or decision.

Some examples of system models for distributed systems are:

- **Synchronous model**: assumes that the network is reliable, the nodes are reliable, the clocks are synchronized, and the message delays and node speeds are bounded. This model simplifies the design and analysis of distributed algorithms, but it is unrealistic and impractical for most real-world systems.
- **Asynchronous model**: assumes that the network is unreliable, the nodes are unreliable, the clocks are unsynchronized, and the message delays and node speeds are unbounded. This model is more realistic and general for most real-world systems, but it makes the design and analysis of distributed algorithms more difficult and complex.
- **Partially synchronous model**: assumes that the network and the nodes are unreliable, but there are some bounds on the message delays and node speeds that hold eventually or with high probability. This model is a compromise between the synchronous and asynchronous models, and it is often used for consensus algorithms, such as Paxos and Raft.
- **Crash-stop model**: assumes that the nodes can only fail by crashing (halting) and never recover. This model simplifies the fault tolerance and recovery mechanisms of distributed systems, but it is not applicable for systems that need to handle node restarts or repairs.
- **Crash-recovery model**: assumes that the nodes can fail by crashing, but they can also recover and resume their operation. This model requires the nodes to have persistent storage and recovery protocols to handle node restarts or repairs, and it is more applicable for systems that need to maintain availability and durability.
- **Byzantine model**: assumes that the nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, or colluding with other faulty nodes. This model requires the nodes to have cryptographic techniques and fault tolerance protocols to handle node misbehavior, and it is more applicable for systems that need to maintain security and integrity.