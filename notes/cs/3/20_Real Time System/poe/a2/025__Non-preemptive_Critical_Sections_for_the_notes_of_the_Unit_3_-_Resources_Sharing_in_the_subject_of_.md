 Here is the content in markdown format without any emojis or external links and in formal tone:

### Non-preemptive Critical Sections for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

1. Critical Section: A piece of code which accesses shared resources and which must be executed atomically is called critical section.
2. Non-preemptive Critical Section: In non-preemptive critical sections, once a task enters its critical section, it cannot be preempted until it exits the critical section. This may lead to priority inversion.
3. Priority Inversion: It occurs when a higher priority task is blocked by a lower priority task which is inside its critical section. This leads to unexpected delays in the higher priority task.
4. Problems with Non-preemptive Critical Sections:
- Priority inversion: As discussed above, it may lead to unexpected delays in higher priority tasks.
- Deadlock: When multiple tasks enter their critical sections, they may end up waiting for each other to exit and create a deadlock.

To overcome the drawbacks of non-preemptive critical sections, concepts like priority inheritance protocols and preemptive critical sections are used.

The above content summarizes the key points about non-preemptive critical sections, priority inversion and problems with non-preemptive critical sections in a formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.