### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

Distributed systems are systems that are composed of multiple independent components that collaborate to provide a unified service to users. In distributed systems, it is important to ensure that all the components agree on some decision or value. This is where agreement protocols come into play.

Agreement protocols are a set of rules and procedures that enable distributed components to reach an agreement on some value or decision. They are used to ensure fault tolerance, consistency, and reliability in distributed systems. In this unit, we will study the different types of agreement protocols and their implementation.

#### Types of Agreement Protocols

1. Two-Phase Commit Protocol (2PC)
2. Three-Phase Commit Protocol (3PC)
3. Paxos Protocol
4. Raft Protocol

#### Two-Phase Commit Protocol (2PC)

The Two-Phase Commit Protocol is a widely used agreement protocol that ensures that all distributed components commit to a transaction in a distributed database. It works by selecting a coordinator that is responsible for coordinating the transaction. The coordinator sends a prepare message to all the participants, and if all participants are ready to commit, it sends a commit message. If any of the participants cannot commit, the coordinator sends an abort message.

#### Three-Phase Commit Protocol (3PC)

The Three-Phase Commit Protocol is an improvement over the Two-Phase Commit Protocol. It adds a third phase to the protocol to handle the case where the coordinator fails. In the Three-Phase Commit Protocol, the coordinator sends a precommit message to all the participants. If any of the participants cannot commit, they send a nack message. If all the participants can commit, the coordinator sends a commit message. If the coordinator fails during the precommit phase, a new coordinator is selected to complete the transaction.

#### Paxos Protocol

The Paxos Protocol is a consensus protocol that enables a group of distributed components to agree on a value or decision. It works by electing a leader that proposes a value. The other components can either accept or reject the proposed value. If the value is accepted by a majority of the components, it is considered the agreed value.

#### Raft Protocol

The Raft Protocol is another consensus protocol that is similar to the Paxos Protocol. It works by electing a leader that sends out heartbeats to all the components to maintain its leadership status. The leader can propose a value, and if it is accepted by a majority of the components, it is considered the agreed value.

#### Advantages of Agreement Protocols

1. Fault tolerance: Agreement protocols ensure that the system is fault-tolerant and can continue to operate even if some components fail.
2. Consistency: Agreement protocols ensure that all components agree on some value or decision, ensuring consistency in the system.
3. Reliability: Agreement protocols ensure that the system is reliable and can provide a consistent service to users.

#### Disadvantages of Agreement Protocols

1. Complexity: Agreement protocols can be complex and difficult to implement.
2. Overhead: Agreement protocols can introduce overhead in the system, as multiple messages need to be exchanged to reach an agreement.
3. Scalability: Some agreement protocols may not scale well with a large number of components.

In conclusion, agreement protocols are crucial in ensuring fault tolerance, consistency, and reliability in distributed systems. Understanding the different types of agreement protocols and their implementation is essential for building robust and reliable distributed systems.