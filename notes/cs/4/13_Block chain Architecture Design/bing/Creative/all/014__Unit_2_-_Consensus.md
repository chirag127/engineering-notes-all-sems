## Unit 2 - Consensus

- Consensus is an agreement on a single data value among distributed processes or systems  
- Consensus is a fundamental problem in distributed computing and multi-agent systems, as it enables reliability and coordination in the presence of faults and failures 
- Consensus algorithms are the processes or protocols that help the distributed processes or systems to reach consensus 
- Consensus algorithms have to satisfy certain properties, such as termination, agreement, integrity, and fault-tolerance 
- Consensus algorithms can be classified into different categories based on the models of computation, such as communication channels, inputs and outputs, failure types, timing assumptions, and permission models 
- Some of the classical consensus algorithms are Paxos, Raft, and Two-Phase Commit 
- Some of the modern consensus algorithms are Proof-of-Work, Proof-of-Stake, and Practical Byzantine Fault Tolerance
- Consensus algorithms have various applications, such as database replication, state machine replication, atomic broadcast, blockchain, and clock synchronization 

### Mnemonics and learning tricks

- A possible mnemonic to remember the properties of consensus algorithms is **TAIF** (Termination, Agreement, Integrity, Fault-tolerance)
- A possible learning trick to understand the difference between synchronous and asynchronous systems is to think of them as **clocks** and **messages**. In a synchronous system, all processes have clocks that are synchronized and can send and receive messages within a known time bound. In an asynchronous system, there are no clocks or time bounds, and processes can only rely on the order of messages they receive.
- A possible learning trick to understand the difference between permissioned and permissionless consensus is to think of them as **clubs** and **parties**. In a permissioned consensus, only the members of the club can participate in the consensus process, and they have to follow the rules of the club. In a permissionless consensus, anyone can join the party and participate in the consensus process, but they have to pay a cost or prove their stake.