# Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are two protocols belonging to the priority inheritance protocols class. Both protocols are used for job task synchronization in real-time systems and are used to solve the uncontrolled priority inversion problem .

## Priority-Inheritance Protocol
The basic priority inheritance protocol is a synchronization protocol that allows a higher priority task to inherit the priority of a lower priority task that holds a shared resource. This prevents a higher priority task from being blocked by a lower priority task for an unbounded amount of time.

## Priority-Ceiling Protocol
The priority ceiling protocol is another synchronization protocol for shared resources that is used to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections . This protocol reduces the worst-case task-blocking time to at most the duration of execution of a single critical section of a lower-priority task . It also prevents the formation of deadlocks .

In contrast to the priority inheritance protocol, the priority ceiling protocol is not greedy. The allocation rule of the priority ceiling protocol may deny a job its requested resource even when the resource is free at the time .

## Comparison
The priority ceiling protocol is considered to be better than the priority inheritance protocol in many ways . It provides a more efficient solution to the uncontrolled priority inversion problem and also prevents the formation of deadlocks .