### Centralized Deadlock Detection for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- Centralized deadlock detection is a technique used in distributed systems to handle deadlock detection by choosing one site as a control site that is responsible for deadlock detection  .
- The control site has access to all the resources of the system and maintains a global wait-for graph that represents the processes and the resources they are waiting for or holding  .
- The control site periodically checks the global wait-for graph for cycles, which indicate the presence of deadlocks  .
- If a cycle is detected, the control site can initiate a recovery action, such as aborting one or more processes involved in the deadlock  .
- The advantages of centralized deadlock detection are that it is simple and easy to implement, and it can detect all the deadlocks in the system  .
- The disadvantages of centralized deadlock detection are that it imposes a high workload on the control site, it creates a single point of failure, and it may detect false or phantom deadlocks due to the delay in message transmission  .
- A false or phantom deadlock is a situation where a cycle is detected in the global wait-for graph, but it does not actually exist in the system, because some processes or resources have changed their state in the meantime  .
- To reduce the possibility of false or phantom deadlocks, some variations of the centralized deadlock detection algorithm have been proposed, such as the Ho Ramamurthy algorithm.
- The Ho Ramamurthy algorithm uses a resource status table and a process table to store the information about the resources and processes in the system.
- The algorithm has two phases: the first phase checks for cycles in the resource status table, and the second phase verifies the cycles in the process table.
- If a cycle is detected in both tables, then the system is declared as deadlock.
- The Ho Ramamurthy algorithm reduces the time consumption of the deadlock detection, but increases the space complexity.
- A mnemonic to remember the name of the algorithm is: **HO**w **RA**re is **M**urthy's **A**lgorithm?
- A possible example of the global wait-for graph and the resource status table for a distributed system with four sites and four resources is shown below:

```
Global wait-for graph:

P1 -> R1 -> P2 -> R2 -> P3 -> R3 -> P4 -> R4 -> P1

Resource status table:

Resource | Site | Status | Requesting Process
R1       | S1   | Held   | P2
R2       | S2   | Held   | P3
R3       | S3   | Held   | P4
R4       | S4   | Held   | P1
```

- In this example, there is a cycle in the global wait-for graph and the resource status table, which indicates a deadlock involving processes P1, P2, P3, and P4.