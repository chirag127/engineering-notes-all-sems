### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time. The priority ceiling of a resource is the highest priority of any task that can access that resource.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The ceiling of the system is the highest priority ceiling of all the resources currently locked.
- A task can lock a resource only if its priority is higher than the ceiling of the system. Otherwise, it has to wait until the resource is released.
- This ensures that a task can be blocked by at most one lower priority task, and that task can be blocked by at most one lower priority task, and so on.
- This reduces the blocking time and improves the schedulability of the system.
- An example of using the priority ceiling protocol in a dynamic priority system is shown below :

| Time | Task T1 (2, 0.9) | Task T2 (5, 2.3) | Resource X | Resource Y | System Ceiling |
|------|------------------|------------------|------------|------------|----------------|
| 0    | Ready            | Ready            | Free       | Free       | 0              |
| 1    | Running          | Waiting          | Locked     | Free       | 1              |
| 2    | Running          | Waiting          | Locked     | Free       | 1              |
| 3    | Running          | Waiting          | Locked     | Free       | 1              |
| 4    | Running          | Waiting          | Locked     | Free       | 1              |
| 5    | Running          | Ready            | Free       | Free       | 0              |
| 6    | Running          | Running          | Free       | Locked     | 2              |
| 7    | Running          | Running          | Free       | Locked     | 2              |
| 8    | Running          | Running          | Free       | Locked     | 2              |
| 9    | Running          | Running          | Free       | Locked     | 2              |
| 10   | Running          | Running          | Free       | Locked     | 2              |
| 11   | Running          | Running          | Free       | Locked     | 2              |
| 12   | Running          | Running          | Free       | Locked     | 2              |
| 13   | Running          | Running          | Free       | Locked     | 2              |
| 14   | Running          | Running          | Free       | Locked     | 2              |
| 15   | Running          | Running          | Free       | Locked     | 2              |
| 16   | Running          | Running          | Free       | Locked     | 2              |
| 17   | Running          | Running          | Free       | Locked     | 2              |
| 18   | Running          | Running          | Free       | Locked     | 2              |
| 19   | Running          | Running          | Free       | Locked     | 2              |
| 20   | Running          | Running          | Free       | Locked     | 2              |
| 21   | Running          | Running          | Free       | Locked     | 2              |
| 22   | Running          | Running          | Free       | Locked     | 2              |
| 23   | Running          | Running          | Free       | Locked     | 2              |
| 24   | Running          | Running          | Free       | Locked     | 2              |
| 25   | Running          | Running          | Free       | Locked     | 2              |
| 26   | Running          | Running          | Free       | Locked     | 2              |
|