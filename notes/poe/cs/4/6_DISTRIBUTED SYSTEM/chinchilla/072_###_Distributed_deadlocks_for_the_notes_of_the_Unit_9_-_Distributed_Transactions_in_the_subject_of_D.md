### Distributed Deadlocks for the Notes of Unit 9 - Distributed Transactions in the Subject of Distributed System

Distributed deadlocks occur when two or more transactions are waiting for resources that are held by other transactions in a distributed system. Deadlocks can occur in a distributed system due to the following reasons:

- Network delays
- Communication failures
- Different transaction schedules
- Different concurrency control protocols

To prevent distributed deadlocks, various techniques are used in distributed systems, such as:

1. Centralized Deadlock Detection:
In this technique, a centralized deadlock detector is used to detect deadlocks in the distributed system. The deadlock detector maintains a wait-for graph, which is a directed graph that represents the relationships among transactions and the resources they are waiting for. The deadlock detector periodically examines the wait-for graph to detect deadlocks. If a deadlock is detected, the deadlock detector takes appropriate action, such as aborting one or more transactions.

2. Distributed Deadlock Detection:
In this technique, each site in the distributed system maintains a local wait-for graph, which represents the relationships among transactions and the resources they are waiting for. The local wait-for graphs are periodically exchanged between sites so that each site can construct a global wait-for graph. The global wait-for graph is used to detect deadlocks in the distributed system.

3. Deadlock Prevention:
In this technique, the system is designed in such a way that deadlocks cannot occur. This can be achieved by using various techniques such as:

- Resource allocation ordering: Resources are allocated to transactions in a specific order, which prevents circular wait conditions.
- Timeouts: Transactions are aborted if they wait for a resource for too long.
- Two-phase locking: Transactions acquire and release locks on resources in two phases, which prevents deadlocks.

4. Deadlock Avoidance:
In this technique, the system tries to avoid deadlocks by predicting the future resource requirements of transactions. The system checks if granting a resource to a transaction will lead to a deadlock, and if so, the resource is not granted. This technique requires accurate knowledge of the resource requirements of transactions, which may not be possible in all cases.

Mnemonic: "CDPA" - Centralized Deadlock Detection, Distributed Deadlock Detection, Deadlock Prevention, Deadlock Avoidance.

In conclusion, distributed deadlocks can be a challenging problem in a distributed system. Various techniques such as centralized deadlock detection, distributed deadlock detection, deadlock prevention, and deadlock avoidance can be used to prevent or resolve distributed deadlocks. It is important to understand these techniques and their advantages and disadvantages to design an effective distributed system.