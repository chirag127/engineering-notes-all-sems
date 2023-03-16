```markdown
## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can be handled by three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention and avoidance are impractical in distributed systems because they require global knowledge and coordination.
- Deadlock detection in distributed systems entails two basic issues: detecting existing deadlocks and resolving detected deadlocks.
- Deadlock detection requires examining the status of process-resource interactions for the presence of cyclic wait.
- Deadlock detection in distributed systems can be done by two methods: global wait-for graph (WFG) and edge chasing.
- A global WFG is a directed graph that represents the waiting relationships among processes and resources in the system.
- A global WFG can be constructed from local WFGs at each site by a centralized or distributed algorithm.
- A deadlock exists in the system if and only if the global WFG contains a cycle.
- Edge chasing is a technique that detects cycles in the global WFG without constructing it explicitly.
- Edge chasing involves sending probe messages along the edges of the local WFGs and detecting cycles when a probe returns to its origin.
- Edge chasing can be implemented by various algorithms, such as the Chandy-Misra-Haas algorithm, the Ho-Ramamoorthy algorithm, and the Huang algorithm.
- Deadlock resolution involves selecting and aborting one or more processes involved in the deadlock to break the cycle.
- Deadlock resolution can be done by a centralized or distributed algorithm, depending on the deadlock detection method.
- Deadlock resolution can be based on various criteria, such as the number of resources held, the number of resources requested, the process priority, the process seniority, or the process rollback cost.
```