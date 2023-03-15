Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on non-preemptive critical sections for the notes of the unit 3 - resource sharing in the subject of real time system.

### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in a real time system by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job requests a resource, it is always allocated the resource, and no other job can interrupt or preempt it until it releases the resource  .
- When a job holds any resource, it executes at a priority higher than the priorities of all other jobs, so that it can finish its critical section as soon as possible  .
- The advantages of non-preemptive critical sections are:
  - They are simple to implement and understand .
  - They prevent deadlock, since no job is ever blocked or waiting for a resource held by another job  .
- The disadvantages of non-preemptive critical sections are:
  - They can cause priority inversion, which means that a high priority job may be delayed by a low priority job that holds a resource .
  - They can reduce the schedulability and utilization of the system, since a job may have to wait for a long time before it can access a resource .
  - They can violate the temporal isolation principle, which means that a job may be affected by the behavior of other jobs that share the same resource .