 Here is the content in markdown format for the topic ### Non-preemptive Critical Sections for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System:

## Non-preemptive Critical Sections

A non-preemptive critical section is a segment of code that must be executed atomically by only one task at a time, and where preemption is disabled for the duration of the critical section. This means that once a task enters a critical section, it cannot be interrupted by a higher priority task until it exits the critical section.

**Advantages:**

- Simplicity: Critical sections are easy to implement as they just disable interrupts.
- Determinism: The order of access to shared resources is well-defined.

**Disadvantages:**

- Priority inversion: A high priority task may have to wait for a lower priority task to exit a critical section. This could lead to deadlock.
- Unbounded delays: There is no guarantee on how long a critical section may last. This could impact the timing constraints of high priority tasks.

**Example:**

```
Critical_Section {
    /* Shared resource access code */
}
```

 tasks inside the critical section cannot be preempted. Only one task at a time can access the shared resource.

**Applications:** Non-preemptive critical sections are commonly used to protect shared resources in embedded systems with a small number of tasks and simple resource sharing patterns. They can be suitable for controlling access to peripheral devices or other resources with short access times.

**Conclusion:** Non-preemptive critical sections provide a simple mechanism to control concurrency and protect shared resources. However, they can suffer from priority inversion and unbounded delays, and may not be suitable for systems with complex resource sharing patterns or tight timing constraints.