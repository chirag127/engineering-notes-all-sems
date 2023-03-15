### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- OCPP works by temporarily raising the priority of a task that accesses a shared resource to the highest priority of any task that may access the same resource.
- ICPP works by raising the priority of a task that accesses a shared resource to the ceiling priority of the resource, which is the highest priority of any task that may access the resource.
- In a dynamic priority system, the priorities of the tasks may change over time, but the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may also change over time, depending on the current priorities of the tasks that may access them .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses, provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- An example of a dynamic priority system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline-driven system is shown below :

```
|<--T1-->|<--T2-->|<--T1-->|<--T2-->|<--T1-->|<--T2-->|
0        2        4        5        7        9        11
```

- Suppose the tasks share a resource X, and T1 accesses X from time 1 to 2, and T2 accesses X from time 6 to 7 .
- The priority ceiling of X is 1 from time 0 to 4, and becomes 2 from time 4 to 5, and so on .
- Using OCPP, T1 will raise its priority to 1 when it accesses X, and T2 will raise its priority to 2 when it accesses X .
- Using ICPP, T1 will raise its priority to the ceiling priority of X, which is 1 from time 0 to 4, and 2 from time 4 to 5, and so on .
- In both cases, no deadlock or priority inversion will occur, as the tasks will always access the resource in priority order .