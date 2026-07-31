### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis.
- System models can be classified into three types: network models, node models, and timing models .
- Network models capture the behavior and characteristics of the communication network, such as the topology, latency, bandwidth, reliability, and ordering of messages .
- Node models capture the behavior and characteristics of the nodes (computers or devices) that participate in the distributed system, such as the availability, failure modes, processing power, and memory capacity .
- Timing models capture the behavior and characteristics of the clocks and timers that are used to measure and synchronize time in the distributed system, such as the accuracy, drift, and synchronization of clocks .
- System models can also be classified into two categories: synchronous and asynchronous .
- A synchronous system model assumes that there are known bounds on the network latency, node processing speed, and clock drift . This simplifies the design and analysis of distributed algorithms, but it is often unrealistic in practice .
- An asynchronous system model assumes that there are no known bounds on the network latency, node processing speed, and clock drift . This reflects the reality of most distributed systems, but it makes the design and analysis of distributed algorithms more challenging .
- A partially synchronous system model is a compromise between the synchronous and asynchronous models, where some bounds are known or hold eventually, but not always . This captures the dynamic and unpredictable nature of distributed systems, but it also allows for some guarantees and optimizations .
- Consensus system models are a special type of system models that describe the assumptions and requirements for solving the consensus problem in distributed systems .
- The consensus problem is the problem of reaching agreement among a set of nodes on a common value, despite the presence of failures and uncertainties .
- The consensus system model specifies the number and type of nodes, the number and type of failures, the type and order of messages, and the type and accuracy of clocks .
- Popular consensus algorithms, such as Paxos and Raft, assume partially synchronous and crash-recovery system models, where nodes can fail by crashing and restarting, messages can be delayed or lost, and clocks can drift or be inaccurate .
- Other consensus algorithms, such as Byzantine fault tolerance and blockchain, assume asynchronous and Byzantine system models, where nodes can fail by behaving arbitrarily, messages can be forged or tampered, and clocks can be manipulated or inconsistent .

: https://inelpandzic.com/articles/system-models-distributed-systems/
: https://www.uio.no/studier/emner/matnat/ifi/INF5040/h11/lectures/SystemModels.pdf
: https://rashmininayanathara.medium.com/system-models-for-distributed-and-cloud-computing-c1d994970682
: https://knowledgeburrow.com/what-are-the-different-system-models-of-distributed-system/
: https://www.baeldung.com/cs/distributed-systems-guide
: https://www.splunk.com/en_us/data-insider/what-are-distributed-systems.html