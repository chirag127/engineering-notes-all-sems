### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- In distributed systems, where sites (or processors) often compete as well as cooperate to achieve a common goal, it is often required that sites reach mutual agreement.
- Examples of agreement problems are:
  - In distributed database systems, data managers at sites must agree on whether to commit or to abort a transaction.
  - In distributed clock synchronization, processes must agree on a common time reference.
  - In distributed leader election, processes must agree on a unique leader among them.
- The formal setting for a distributed agreement protocol is as follows:
  - There are n processes in the system, each with a unique identifier.
  - Each process has an initial value, which is either 0 or 1.
  - Each process must decide on a final value, which is also either 0 or 1.
  - The protocol must satisfy the following properties:
    - **Termination**: Every non-faulty process eventually decides on a value.
    - **Agreement**: All non-faulty processes decide on the same value.
    - **Validity**: If all non-faulty processes have the same initial value, then they all decide on that value.
- The difficulty of solving the agreement problem depends on the following factors:
  - The type of communication: synchronous or asynchronous.
  - The type of failures: crash, omission, or malicious (Byzantine).
  - The type of messages: authenticated or non-authenticated.
- Depending on these factors, different algorithms and lower bounds can be derived for the agreement problem.
- Some of the well-known algorithms for the agreement problem are:
  - The Oral Messages (OM) algorithm, which solves the agreement problem in a synchronous system with authenticated messages and crash failures.
  - The Byzantine Generals (BG) algorithm, which solves the agreement problem in a synchronous system with authenticated messages and malicious failures.
  - The Dolev et al.'s algorithm, which solves the agreement problem in an asynchronous system with authenticated messages and malicious failures.
  - The Paxos algorithm, which solves the agreement problem in an asynchronous system with non-authenticated messages and crash failures.
- Some of the applications of agreement protocols are:
  - Fault-tolerant clock synchronization, where processes use agreement protocols to synchronize their clocks despite the presence of faulty processes or messages.
  - Atomic commit in distributed database systems, where processes use agreement protocols to ensure that either all or none of the sites commit a transaction.
  - Consensus in distributed systems, where processes use agreement protocols to agree on a common state or value for replicated data or services.

: Ch. 9 Agreement Protocols - Indian Institute of Information Technology ...
: Parameterized Verification and Synthesis for Distributed Agreement ...