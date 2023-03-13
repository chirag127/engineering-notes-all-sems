### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis.
- System models can be classified into three types: network models, node models, and timing models .
- Network models capture the behavior and characteristics of the communication network, such as the reliability, latency, bandwidth, and topology of the links .
- Node models capture the behavior and characteristics of the nodes (computers or devices) that participate in the distributed system, such as the reliability, availability, processing power, and memory capacity of the nodes .
- Timing models capture the behavior and characteristics of the clocks and timers that are used to measure and synchronize time in the distributed system, such as the accuracy, precision, drift, and skew of the clocks and timers .
- Depending on the assumptions and guarantees of the system model, different design choices and trade-offs can be made for the distributed system .
- For example, a system model that assumes reliable and synchronous network and nodes can use simpler and faster algorithms for achieving agreement protocols, such as consensus, atomic broadcast, or leader election .
- However, a system model that assumes unreliable and asynchronous network and nodes may need more complex and robust algorithms for achieving agreement protocols, such as Paxos, Raft, or Zab .
- A system model can also be used to evaluate the correctness, performance, and scalability of a distributed system, by comparing the expected and observed behavior of the system under different scenarios and workloads .
- A system model can also be used to compare and contrast different distributed systems, by identifying their similarities and differences in terms of their properties and assumptions .
- Some examples of distributed systems that use different system models are telecommunications networks, graphical and video-rendering systems, scientific computing, airline and hotel reservation systems, multiuser online games, and cloud computing .

#### Mnemonics and learning tricks

- A possible mnemonic to remember the three types of system models is **N**o **N**eed **T**o **M**odel, where **N** stands for **N**etwork, **N** stands for **N**ode, and **T** stands for **T**iming.
- A possible learning trick to understand the trade-offs between different system models is to use the CAP theorem, which states that a distributed system can only guarantee two out of the following three properties: **C**onsistency, **A**vailability, and **P**artition tolerance.
- Consistency means that all nodes see the same data at the same time.
- Availability means that every request receives a response, whether it was successful or not.
- Partition tolerance means that the system continues to operate despite network failures or partitions.
- For example, a system model that assumes reliable and synchronous network and nodes can guarantee consistency and availability, but not partition tolerance.
- A system model that assumes unreliable and asynchronous network and nodes can guarantee availability and partition tolerance, but not consistency.
- A system model that assumes partially reliable and partially synchronous network and nodes can guarantee consistency and partition tolerance, but not availability.