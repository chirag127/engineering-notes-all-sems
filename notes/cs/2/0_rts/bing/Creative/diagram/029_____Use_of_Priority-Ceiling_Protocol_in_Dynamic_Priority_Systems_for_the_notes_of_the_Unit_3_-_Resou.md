Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the use of priority-ceiling protocol in dynamic priority systems for the notes of the unit 3 - resource sharing in the subject of real time system.

### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The priority ceiling protocol is a synchronization technique that prevents deadlock and unbounded priority inversion by temporarily raising the priorities of tasks that access shared resources .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- The difference between OCPP and ICPP is that OCPP raises the priority of a task only when it locks a resource, while ICPP raises the priority of a task as soon as it becomes ready to execute.
- The worst-case behaviour of the two ceiling schemes is identical from a scheduling viewpoint.
- Both variants work by temporarily raising the priorities of tasks that access shared resources above the system ceiling, which is the highest priority ceiling of all the resources currently locked .
- A task can lock a resource only if its priority is higher than the system ceiling, otherwise it has to wait until the system ceiling drops below its priority .
- This ensures that no task can be blocked by a lower priority task, and that no circular wait can occur among tasks .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This can be done by using a priority queue to store the ready tasks and their priorities, and by using a priority table to store the priority ceilings of the resources and the tasks that access them .
- An example of a dynamic system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline driven system is shown below :

| Time | T1 | T2 | Resource X | Resource Y | System Ceiling |
|------|----|----|------------|------------|----------------|
| 0    | 1  | 2  | -          | -          | -              |
| 1    | 1  | 2  | T1         | -          | 1              |
| 2    | 1  | 2  | T1         | -          | 1              |
| 3    | 1  | 2  | T1         | -          | 1              |
| 4    | 2  | 1  | T1         | T2         | 2              |
| 5    | 2  | 1  | T1         | T2         | 2              |
| 6    | 2  | 1  | T1         | T2         | 2              |
| 7    | 2  | 1  | T1         | T2         | 2              |
| 8    | 2  | 1  | -          | T2         | 1              |
| 9    | 2  | 1  | -          | T2         | 1              |
| 10   | 2  | 1  | -          | T2         | 1              |
| 11   | 2  | 1  | -          | T2         | 1              |
| 12   | 2  | 1  | -          | -          | -              |
| 13   | 2  | 1  | -          | -          | -              |
| 14   | 2  | 1  | -          | -          | -              |
| 15   | 2  | 1  | -          | -          |