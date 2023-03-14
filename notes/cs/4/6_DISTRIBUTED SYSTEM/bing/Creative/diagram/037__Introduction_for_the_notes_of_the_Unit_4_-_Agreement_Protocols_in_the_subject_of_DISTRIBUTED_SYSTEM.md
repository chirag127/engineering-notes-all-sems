### Introduction

Agreement protocols are a class of distributed algorithms that aim to achieve a common goal among a set of processes in a network, despite the possibility of failures or malicious behavior. Some examples of agreement problems are:

- **Consensus**: All processes have to agree on a single value proposed by one or more processes.
- **Leader election**: All processes have to agree on a single process that acts as a leader or coordinator.
- **Atomic commit**: All processes have to agree on whether to commit or abort a transaction in a distributed database system.

Agreement protocols are challenging to design and verify because of the inherent uncertainty and asynchrony in distributed systems. Processes may not have a global view of the system state, may not receive messages in a timely manner, or may not be able to distinguish between crashed and slow processes. Moreover, some processes may behave arbitrarily or maliciously, sending forged or inconsistent messages to other processes.

To cope with these difficulties, agreement protocols often rely on some assumptions about the system model, such as:

- **Synchrony vs. asynchrony**: A synchronous system is one where processes and messages have bounded delays, while an asynchronous system is one where there are no such bounds. Synchronous systems are easier to reason about, but less realistic than asynchronous systems.
- **Failure model**: A failure model specifies the types and number of failures that can occur in the system. Some common failure models are:
  - **Crash failures**: A process stops functioning and never resumes operation.
  - **Omission failures**: A process fails to send or receive some messages.
  - **Byzantine failures**: A process behaves arbitrarily or maliciously, sending forged or inconsistent messages.
- **Communication model**: A communication model specifies the types and properties of messages that can be exchanged in the system. Some common communication models are:
  - **Authenticated vs. non-authenticated**: An authenticated message system is one where a process can verify the authenticity and integrity of a received message, while a non-authenticated message system is one where a process cannot do so.
  - **Broadcast vs. point-to-point**: A broadcast message system is one where a process can send a message to all other processes in one step, while a point-to-point message system is one where a process can only send a message to one other process at a time.

The following diagram illustrates the basic architecture of a distributed system with n processes that communicate using point-to-point messages. Each process has a local state and can send and receive messages to and from other processes. An agreement protocol is a set of rules that specify how the processes should behave and interact in order to reach a common goal.

```
+-----------------+      +-----------------+      +-----------------+
| Process 1       |      | Process 2       |      | Process n       |
|                 |      |                 |      |                 |
| Local state     |      | Local state     |      | Local state     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
      |  ^                  |  ^                  |  ^
      |  |                  |  |                  |  |
      v  |                  v  |                  v  |
+-----------------+      +-----------------+      +-----------------+
| Message queue 1 |      | Message queue 2 |      | Message queue n |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
      |  ^                  |  ^                  |  ^
      |  |                  |  |                  |  |
      v  |                  v  |                  v  |
+-----------------+      +-----------------+      +-----------------+
| Network         |<---->| Network         |<---->| Network         |
|                 |----->|                 |----->|                 |
+-----------------+      +-----------------+      +-----------------+
```