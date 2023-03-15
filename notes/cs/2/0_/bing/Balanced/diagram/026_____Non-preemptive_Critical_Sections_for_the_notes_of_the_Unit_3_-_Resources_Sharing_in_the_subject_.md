Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on non-preemptive critical sections for the notes of the unit 3 - resource sharing in the subject of real time system.

### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in a real time system by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job requests a resource, it is always allocated the resource, and no other job can interrupt or preempt it until it releases the resource  .
- When a job holds any resource, it executes at a priority higher than the priorities of all other jobs, so that it can finish its critical section as soon as possible  .
- The advantage of non-preemptive critical sections is that they prevent deadlock, which is a situation where two or more jobs are waiting for each other to release resources, and none of them can proceed  .
- The disadvantage of non-preemptive critical sections is that they can cause blocking, which is a situation where a job with a higher priority is waiting for a job with a lower priority to release a resource, and the higher priority job cannot proceed  .
- Blocking can affect the schedulability and performance of real time systems, especially if the critical sections are long or frequent  .
- To reduce blocking, some techniques are: limiting the number and size of critical sections, using priority inheritance or priority ceiling protocols, or using other synchronization methods such as semaphores, mutexes, or monitors   .