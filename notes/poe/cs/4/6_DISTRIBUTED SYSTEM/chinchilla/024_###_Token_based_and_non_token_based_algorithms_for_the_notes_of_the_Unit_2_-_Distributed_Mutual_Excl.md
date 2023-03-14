### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

Distributed Mutual Exclusion is an important problem that arises in distributed systems where multiple processes need to access a shared resource in a mutually exclusive manner. To solve this problem, various algorithms have been proposed, including Token-based and Non-Token-based algorithms.

#### Token-based Algorithms:

Token-based algorithms are based on the concept of a token, which is a special message that is passed between processes to grant permission to access a shared resource. The token is passed in a predetermined order among the processes, and only the process holding the token can access the shared resource.

Some popular token-based algorithms are:

1. Ricart-Agrawala Algorithm:
   - Each process maintains a queue of pending requests for the shared resource.
   - When a process wants to access the resource, it sends a request message to all other processes.
   - A process grants permission to access the resource only if it is not currently holding the token and has no pending requests of its own.
   - When a process releases the resource, it passes the token to the next process in the queue.

2. Maekawa's Algorithm:
   - Processes are divided into mutually exclusive groups, and each group elects a leader.
   - Each process maintains a set of processes that it needs to communicate with to access the shared resource.
   - When a process wants to access the resource, it sends a request message to all the processes in its set.
   - A process grants permission to access the resource only if it is not currently holding the token and has received requests from all the processes in its set.
   - When a process releases the resource, it passes the token to the next process in the group.

#### Non-Token-based Algorithms:

Non-token-based algorithms are based on the concept of a distributed lock, which is a mechanism that allows processes to request and release locks on a shared resource. A process can access the shared resource only if it acquires the lock.

Some popular non-token-based algorithms are:

1. Centralized Algorithm:
   - There is a single process called the coordinator that maintains a list of processes requesting access to the shared resource.
   - When a process wants to access the resource, it sends a request message to the coordinator.
   - The coordinator grants permission to access the resource based on some predefined policy.
   - When a process releases the resource, it sends a release message to the coordinator.

2. Distributed Algorithm:
   - Each process maintains a list of processes requesting access to the shared resource.
   - When a process wants to access the resource, it sends a request message to all other processes.
   - A process grants permission to access the resource only if it is not currently holding the lock and has no pending requests of its own.
   - When a process releases the resource, it sends a release message to all other processes.

Mnemonics and learning tricks:
- For token-based algorithms, remember that a token is like a physical object that is passed between processes to grant permission to access the shared resource.
- For non-token-based algorithms, remember that a distributed lock is like a key that processes need to acquire to access the shared resource.