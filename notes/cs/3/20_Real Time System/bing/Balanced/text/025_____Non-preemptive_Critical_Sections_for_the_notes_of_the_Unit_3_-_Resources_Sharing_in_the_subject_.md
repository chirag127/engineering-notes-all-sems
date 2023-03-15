### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job requests a resource, it is always allocated the resource, and no other job can interrupt or preempt it until it releases the resource  .
- When a job holds any resource, it executes at a priority higher than the priorities of all other jobs, so that it can finish its critical section as soon as possible  .
- The advantage of non-preemptive critical sections is that they prevent deadlock, which is a situation where two or more jobs are waiting for each other to release resources, and none of them can proceed  .
- The disadvantage of non-preemptive critical sections is that they can cause priority inversion, which is a situation where a high-priority job is blocked by a low-priority job that holds a resource, and the low-priority job cannot be preempted by a medium-priority job that does not need the resource  .
- Non-preemptive critical sections can also cause long blocking times, which is the amount of time that a job has to wait for a resource to become available, and this can affect the schedulability and performance of real-time systems  .
- Non-preemptive critical sections are suitable for systems that have low resource contention, short critical sections, and low blocking times  .