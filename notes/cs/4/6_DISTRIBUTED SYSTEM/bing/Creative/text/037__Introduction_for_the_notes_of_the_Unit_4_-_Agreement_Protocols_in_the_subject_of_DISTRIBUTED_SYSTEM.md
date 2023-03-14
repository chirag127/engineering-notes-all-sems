### Introduction

- In distributed systems, where sites (or processors) often compete as well as cooperate to achieve a common goal, it is often required that sites reach mutual agreement.
- For example, in distributed database systems, data managers at sites must agree on whether to commit or to abort a transaction.
- The formal setting for a distributed agreement protocol is as follows:
  - A set of n processes, each with an initial value, communicate by sending and receiving messages.
  - The processes may be subject to failures, such as crash, omission, or malicious (Byzantine) faults.
  - The messages may be authenticated or non-authenticated, meaning that a process can or cannot verify the authenticity of a received message.
  - The communication may be synchronous or asynchronous, meaning that there are or are not bounds on the message delivery time and the process execution speed.
  - The goal of the protocol is to ensure that all non-faulty processes agree on a common value, which is usually derived from the initial values of the processes.
- There are different types of agreement protocols, depending on the assumptions and the requirements of the problem:
  - Consensus: All non-faulty processes must agree on the same value, and the value must be the initial value of some non-faulty process.
  - Byzantine agreement: Same as consensus, but the protocol must also tolerate malicious faults.
  - Interactive consistency: Same as Byzantine agreement, but the protocol must also ensure that all non-faulty processes know the initial values of all other non-faulty processes.
  - k-set agreement: All non-faulty processes must agree on one of at most k values, and the value must be the initial value of some non-faulty process.
  - Leader election: All non-faulty processes must agree on the same process, which is called the leader, and the leader must be a non-faulty process.
  - Atomic commit: All non-faulty processes must agree on whether to commit or abort a transaction, and the decision must be consistent with the state of the transaction.
- The design and analysis of agreement protocols is a fundamental and challenging topic in distributed systems, as it involves trade-offs between the number of processes, the number of rounds, the number of messages, the type and the number of faults, the type of communication, and the type of messages.
- Agreement protocols have many applications in distributed systems, such as fault-tolerant clock synchronization, atomic commit in distributed database systems, distributed mutual exclusion, distributed shared memory, distributed consensus, and state machine replication.