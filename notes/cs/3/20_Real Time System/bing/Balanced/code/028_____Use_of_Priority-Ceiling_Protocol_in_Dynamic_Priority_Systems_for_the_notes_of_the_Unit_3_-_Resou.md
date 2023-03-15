# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- OCPP works by temporarily raising the priority of a task that accesses a shared resource to the highest priority of any task that may access the same resource.
- ICPP works by raising the priority of a task that accesses a shared resource to the ceiling priority of the resource, which is the highest priority of any task that may access the resource.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- An example of a dynamic system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in deadline driven system is shown below :

| Time | Task | Resource | Priority | Ceiling |
|------|------|----------|----------|---------|
| 0    | T1   | X        | 1        | 1       |
| 1    | T1   | X        | 1        | 1       |
| 2    | T1   | X        | 1        | 1       |
| 3    | T1   | X        | 1        | 1       |
| 4    | T2   | Y        | 2        | 2       |
| 5    | T2   | Y        | 2        | 2       |
| 6    | T2   | Y        | 2        | 2       |
| 7    | T2   | Y        | 2        | 2       |
| 8    | T1   | X        | 1        | 2       |
| 9    | T1   | X        | 1        | 2       |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The priority ceiling of Y is 2 from time 4 to 8 and becomes 1 from time 8 to 9 and so on .
- The ceiling of the system is the maximum of the priority ceilings of all the resources.
- The ceiling of the system is 1 from time 0 to 4 and becomes 2 from time 4 to 8 and so on .
- The priority ceiling protocol ensures that a task can access a resource only if its priority is higher than the ceiling of the system.
- This prevents deadlock and unbounded priority inversion, as well as reduces the blocking time of higher priority tasks .

: Use of Priority Ceiling Protocol in Dynamic Priority Systems: https://benchpartner.com/use-of-priority-ceiling-protocol-in-dynamic-priority-systems
: Use of Priority Ceiling Protocol in Dynamic Priority Systems: http://benchpartner.com/use-of-priority-ceiling-protocol-in-dynamic-priority-systems
: Priority ceiling protocol - Wikipedia: https://en.wikipedia.org/wiki/Priority_ceiling_protocol
: Priority Ceiling Protocol - GeeksforGeeks: https://www.geeksforgeeks.org/priority-ceiling-protocol/