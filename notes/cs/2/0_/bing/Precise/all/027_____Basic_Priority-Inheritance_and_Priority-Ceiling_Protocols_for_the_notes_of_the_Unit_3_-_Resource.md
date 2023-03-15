# Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are two protocols belonging to the priority inheritance protocols class. Both protocols solve the uncontrolled priority inversion problem.

## Priority-Inheritance Protocol

The basic priority inheritance protocol is a synchronization protocol for shared resources in real-time systems. It is used to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.

## Priority-Ceiling Protocol

The priority ceiling protocol is another synchronization protocol for shared resources in real-time systems. It is better than the priority inheritance protocol in many ways. It reduces the worst-case task-blocking time to at most the duration of execution of a single critical section of a lower-priority task. This protocol also prevents the formation of deadlocks.

The allocation rule of priority ceiling protocol is different from that of priority inheritance protocol. In the case of priority ceiling protocol, a job may be denied its requested resource even when the resource is free at the time.

## Comparison

Priority Inheritance protocols are greedy while Priority Ceiling protocols are not. The priority ceiling protocol is better than the priority inheritance protocol in many ways.

## References

: Priority inheritance protocols: an approach to real-time synchronization | IEEE Journals & Magazine | IEEE Xplore
: Priority Ceiling Protocol - GeeksforGeeks
: Priority ceiling protocol - Wikipedia
: Difference between Priority Inheritance and Priority Ceiling Protocols - Benchpartner