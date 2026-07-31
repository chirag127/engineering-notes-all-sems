### Priority Driven Approach

- Priority driven approach is a class of scheduling algorithms that never leave any resource idle intentionally.
- A resource becomes idle only when no job requiring the resource is ready for execution.
- It is an event driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur.
- Priority driven approach is useful for more dynamic real-time systems with a mix of time-based and event-based activities, where the system must adapt to changing conditions and events.
- Priority driven approach assigns a priority level to each job and executes the jobs in the order of their priority.
- Higher-priority jobs are executed before lower-priority jobs and can preempt lower-priority jobs if they arrive while the lower-priority jobs are running.
- Priority driven approach can improve the real-time performance and predictability of real-time systems by reducing the response time and deadline misses of critical jobs.
- Priority driven approach can be implemented using different priority assignment schemes, such as fixed priority, dynamic priority, or hybrid priority.
- Priority driven approach can also be classified into preemptive or non-preemptive, depending on whether a job can be interrupted by a higher-priority job or not.
- Priority driven approach has some challenges, such as priority inversion, blocking, and resource contention, which need to be addressed by using appropriate protocols and mechanisms.