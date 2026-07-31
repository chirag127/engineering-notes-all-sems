### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure is an event that causes a deviation from the expected behavior of the system.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc .
- A checkpoint is a snapshot of the system state at a certain point in time, which can be used to resume the execution after a failure.
- Obtaining consistent checkpoints is a challenge in distributed systems, because the system consists of multiple processes that may communicate and synchronize with each other.
- A consistent checkpoint is a set of checkpoints from different processes that reflects a global state of the system that could have occurred during the normal execution.
- A consistent checkpoint should satisfy the following properties:
  - No orphan message: A message is orphan if it is sent by a process before its checkpoint, but received by another process after its checkpoint.
  - No lost message: A message is lost if it is sent by a process after its checkpoint, but received by another process before its checkpoint.
- There are different techniques to obtain consistent checkpoints, such as coordinated checkpointing, uncoordinated checkpointing, and communication-induced checkpointing .
- Coordinated checkpointing is a technique where all the processes in the system agree on a global checkpoint and take their local checkpoints simultaneously.
- Coordinated checkpointing has the advantages of simplicity, no orphan messages, and easy recovery, but it has the disadvantages of high overhead, blocking, and domino effect.
- Domino effect is the phenomenon where a failure of one process may cause the rollback of other processes that depend on it, potentially to the initial state.
- Uncoordinated checkpointing is a technique where each process takes its local checkpoint independently, without any coordination with other processes.
- Uncoordinated checkpointing has the advantages of low overhead, non-blocking, and no domino effect, but it has the disadvantages of complexity, orphan messages, and difficult recovery.
- Communication-induced checkpointing is a technique where each process takes its local checkpoint based on the information piggybacked on the messages it sends or receives.
- Communication-induced checkpointing has the advantages of low overhead, non-blocking, and no domino effect, but it has the disadvantages of complexity, dependency tracking, and potential useless checkpoints.
- To obtain consistent checkpoints, the system should also have a stable storage, which is a storage device that can resist major disasters and preserve the checkpoints.

: Failure Recovery in Distributed Systems - 1000 Projects
: Recovery in Distributed Systems - GeeksforGeeks
: 1 Zorro: Zero-Cost Reactive Failure Recovery in ...
: Various Failures in Distributed Systems - tutorialspoint.com
: Handling Failure in Distributed System - GeeksforGeeks