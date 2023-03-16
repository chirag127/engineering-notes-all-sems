# System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior and limitations of a distributed system, and guide us in choosing appropriate algorithms and protocols for achieving certain goals.

There are different types of system models that capture different aspects of a distributed system, such as:

- **Network behavior**: how reliable, fast, and secure are the communication links between the nodes of the system?
- **Node behavior**: how reliable, fast, and secure are the nodes of the system, and what are their capabilities and resources?
- **Timing behavior**: how synchronized are the clocks of the nodes of the system, and how predictable are the delays and durations of events and messages?
- **Consensus behavior**: how can the nodes of the system reach agreement on a common value or action, despite the presence of failures and uncertainties?

Some examples of system models for distributed systems are:

- **Synchronous system model**: a system model that assumes bounded network delays, bounded node processing speeds, and bounded clock drifts. This model simplifies the design and analysis of distributed algorithms, but it is unrealistic for most practical systems.
- **Asynchronous system model**: a system model that assumes no bounds on network delays, node processing speeds, or clock drifts. This model is more realistic for most practical systems, but it makes the design and analysis of distributed algorithms more challenging and complex.
- **Partially synchronous system model**: a system model that assumes some bounds on network delays, node processing speeds, or clock drifts, but not all of them. This model is a compromise between the synchronous and asynchronous models, and it tries to capture the realistic behavior of most practical systems.
- **Crash-stop system model**: a system model that assumes nodes can only fail by crashing (stopping to function), and they cannot recover from failures. This model simplifies the design and analysis of fault-tolerant distributed algorithms, but it is unrealistic for most practical systems.
- **Crash-recovery system model**: a system model that assumes nodes can fail by crashing, but they can also recover from failures and resume their operation. This model is more realistic for most practical systems, but it makes the design and analysis of fault-tolerant distributed algorithms more challenging and complex.
- **Byzantine system model**: a system model that assumes nodes can fail in arbitrary ways, including behaving maliciously or inconsistently. This model is the most general and realistic for most practical systems, but it also makes the design and analysis of fault-tolerant distributed algorithms the most difficult and complex.
- **Leader-based system model**: a system model that assumes there is a special node in the system, called the leader, that coordinates the actions and decisions of the other nodes. This model simplifies the design and analysis of distributed algorithms, but it also introduces a single point of failure and a bottleneck in the system.
- **Peer-to-peer system model**: a system model that assumes there is no special node in the system, and all nodes are equal and cooperate with each other. This model is more robust and scalable than the leader-based model, but it also makes the design and analysis of distributed algorithms more challenging and complex.