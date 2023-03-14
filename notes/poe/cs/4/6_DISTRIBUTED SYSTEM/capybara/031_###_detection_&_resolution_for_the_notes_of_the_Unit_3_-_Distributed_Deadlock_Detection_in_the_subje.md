### Detection & Resolution for the notes of Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

Deadlocks are a common problem in distributed systems that can lead to system failure, performance degradation, and resource wastage. To prevent deadlocks, distributed deadlock detection and resolution techniques are used. In this section, we will discuss the detection and resolution techniques used in distributed systems.

#### Distributed Deadlock Detection

Distributed deadlock detection involves identifying if a deadlock has occurred in the system. There are two approaches to distributed deadlock detection:

1. **Centralized Approach:** In this approach, a centralized entity is responsible for detecting deadlocks. The entity maintains a global wait-for graph that consists of nodes representing processes and edges representing resource requests. Whenever a process requests a resource, the entity updates the wait-for graph. If a cycle is detected in the graph, it means that a deadlock has occurred. The entity then uses various algorithms, such as the banker's algorithm, to resolve the deadlock.

2. **Distributed Approach:** In this approach, each node in the system maintains a local wait-for graph. The nodes periodically exchange their wait-for graphs with neighboring nodes to construct a global wait-for graph. If a cycle is detected in the global wait-for graph, it means that a deadlock has occurred. The nodes then use various algorithms, such as the edge chasing algorithm, to resolve the deadlock.

#### Distributed Deadlock Resolution

Distributed deadlock resolution involves breaking the deadlock once it has been detected. There are three approaches to distributed deadlock resolution:

1. **Abort Approach:** In this approach, one or more processes involved in the deadlock are aborted to break the cycle. The aborted processes release all their resources, allowing the remaining processes to continue execution. This approach is simple but can lead to data loss and poor system performance.

2. **Blocking Approach:** In this approach, one or more processes involved in the deadlock are blocked until the deadlock is resolved. The blocked processes wait for the required resources to become available. This approach is more complex than the abort approach but preserves data integrity and system performance.

3. **Combined Approach:** In this approach, a combination of the abort and blocking approaches is used. The system first tries to resolve the deadlock using the blocking approach. If the deadlock cannot be resolved within a specified time, the system uses the abort approach. This approach balances data integrity, system performance, and deadlock resolution time.

#### Learning Tricks and Mnemonics

To remember the different approaches to distributed deadlock detection and resolution, you can use the following mnemonic:

**DDDD - Distributed Deadlock Detection and Disruption**

- DDDD stands for Distributed Deadlock Detection and Disruption
- The first D stands for the two approaches to Distributed Deadlock Detection - Centralized and Distributed
- The second D stands for the three approaches to Distributed Deadlock Resolution - Abort, Blocking, and Combined

You can also use the following diagram to visualize the different approaches to distributed deadlock resolution:

```
                    Abort
                /         \
    Blocking                 Combined
```

In conclusion, distributed deadlock detection and resolution techniques are important in preventing deadlocks in distributed systems. The choice of approach depends on the specific requirements of the system, such as data integrity, system performance, and deadlock resolution time. Remembering the different approaches can be made easy using the mnemonic and diagram mentioned above.