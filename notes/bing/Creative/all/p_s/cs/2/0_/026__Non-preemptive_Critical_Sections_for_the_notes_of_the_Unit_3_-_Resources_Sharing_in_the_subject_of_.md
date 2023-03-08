### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access of shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively  .
- A critical section is a segment of code that accesses a shared resource and must be executed atomically, i.e., without interruption by other tasks or interrupts.
- In NPCS, when a task requests a resource, it is always allocated the resource. When a task holds any resource, it executes at a priority higher than the priorities of all other tasks  .
- This protocol ensures that no task is ever preempted when it holds any resource, thus avoiding deadlock and priority inversion problems  .
- However, NPCS also has some disadvantages, such as:
  - It may cause long blocking times for tasks that need to access the same resource as a lower-priority task that is executing its critical section .
  - It may cause unnecessary preemptions for tasks that do not need to access any resource but have lower priority than a task that is requesting a resource .
  - It may cause resource underutilization, as a task that holds a resource may not use it for the entire duration of its critical section .
  - It may not be applicable for some types of resources, such as message queues or semaphores, that require synchronization mechanisms other than priority-based scheduling .
- An example of NPCS is shown in the following figure, where three tasks T1, T2, and T3 share a resource R. The arrows indicate the requests and releases of the resource, and the shaded areas indicate the critical sections. The numbers indicate the priority levels of the tasks, with 1 being the highest and 3 being the lowest.

```
    T1 (1) |----->|-----|<-----|----->|-----|<-----|----->|-----|<-----|----->|-----|<-----|----->|
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
    T2 (2) |----->|-----|<-----|----->|-----|<-----|----->|-----|<-----|----->|-----|<-----|----->|
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
    T3 (3) |----->|-----|<-----|----->|-----|<-----|----->|-----|<-----|----->|-----|<-----|----->|
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
    R      |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |      |     |      |      |     |      |      |     |      |      |     |      |      |
           |

I'm not sure what topic you are referring to, but I can try to help you find some good mnemonics and learning tricks if you tell me more. Mnemonics and learning tricks can be very helpful for remembering information, especially if they are catchy, funny, or related to something you already know. Do you have a specific subject or area that you want to learn more about?