 Here is the content in markdown format without any emojis or external links:

### Non-preemptive Critical Sections for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

1. A critical section is a piece of code that accesses a shared resource (like shared data) which must be executed atomically. This means that once a process enters its critical section, no other process should be allowed to enter its critical section until the first process exits its critical section.
2. In non-preemptive critical sections, once a process enters its critical section, it cannot be preempted by the scheduler until it exits the critical section. This ensures mutual exclusion but can lead to priority inversion and deadlock.
3. To implement non-preemptive critical sections, disable interrupts before entering the critical section and enable interrupts after exiting the critical section. This prevents the currently running process from being preempted.
4. The disadvantages of non-preemptive critical sections are:
- Priority inversion: A high priority process can be blocked by a low priority process in its critical section.
- Deadlock: Two or more processes can get stuck in their critical sections and deadlock the system.
- Performance: Disabling and enabling interrupts leads to additional overhead.

The content is written in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.