
### Absence of Global Clock for the Notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

* In distributed systems, there is no single global clock that can be used to coordinate the activities of all the components. 
* Instead, the system must rely on the local clocks of each component and the messages sent between them to coordinate its activities.
* This lack of a global clock can be a source of problems, as it makes it difficult to synchronize the activities of the components.
* One of the most common problems is the "clock skew" problem, where the local clocks of the components are not synchronized with each other. This can lead to problems when components need to coordinate their activities.
* To address this problem, distributed systems use techniques such as clock synchronization algorithms, logical clocks, and distributed timestamping to help synchronize the activities of the components.
* Clock synchronization algorithms are used to ensure that the local clocks of the components are synchronized with each other. 
* Logical clocks are used to provide a global view of time, even without a global clock. 
* Distributed timestamping is used to record the order in which events occur in a distributed system.

* Mnemonic: CLoDDS - Clock synchronization, Logical clocks, Distributed timestamping.