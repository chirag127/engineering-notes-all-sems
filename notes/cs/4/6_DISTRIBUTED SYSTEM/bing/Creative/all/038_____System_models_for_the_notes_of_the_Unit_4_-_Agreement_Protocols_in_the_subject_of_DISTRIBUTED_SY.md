# System Models for Distributed Systems

A system model is a simplified representation of a distributed system that captures its essential properties and design choices. System models help us to reason about the behavior, performance, and correctness of distributed systems. There are different types of system models that focus on different aspects of distributed systems, such as:

- Network behavior: how reliable, fast, and secure are the communication links between the nodes?
- Node behavior: how reliable, fast, and secure are the nodes themselves?
- Timing behavior: how synchronized are the clocks of the nodes and how predictable are the delays in the system?
- Consensus behavior: how do the nodes agree on a common value or action in the presence of failures and asynchrony?

Some of the common system models for distributed systems are:

- Synchronous model: assumes that there are known bounds on the network delay, the node speed, and the clock drift. This model simplifies the design and analysis of distributed algorithms, but it is unrealistic in practice.
- Asynchronous model: assumes that there are no bounds on the network delay, the node speed, and the clock drift. This model is more realistic and general, but it makes the design and analysis of distributed algorithms more difficult and sometimes impossible.
- Partially synchronous model: assumes that there are bounds on the network delay, the node speed, and the clock drift, but they are unknown or may change over time. This model is a compromise between the synchronous and asynchronous models, and it captures the behavior of many real-world distributed systems.
- Crash-stop model: assumes that nodes can only fail by crashing (stopping to execute) and that crashed nodes do not recover. This model simplifies the design and analysis of fault-tolerant distributed algorithms, but it does not account for other types of failures or recoveries.
- Crash-recovery model: assumes that nodes can fail by crashing and that crashed nodes can recover after some time. This model is more realistic and general, but it requires the use of persistent storage and recovery mechanisms to ensure consistency and progress.
- Byzantine model: assumes that nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, or colluding with other faulty nodes. This model is the most pessimistic and challenging, but it captures the worst-case scenarios of distributed systems.

Some of the popular consensus algorithms for distributed systems, such as Paxos and Raft, assume a partially synchronous and crash-recovery system model, meaning that they can tolerate network delays and node crashes, but not Byzantine failures. They also require a majority of nodes to be correct and reachable to achieve consensus.