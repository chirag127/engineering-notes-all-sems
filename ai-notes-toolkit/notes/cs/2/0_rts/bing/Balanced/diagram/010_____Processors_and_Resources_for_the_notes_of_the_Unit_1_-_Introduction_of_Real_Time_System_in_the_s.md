### Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers .
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource is a system component that can be shared by multiple jobs, but only one job can use it at a time. Examples of resources are memory, files, printers, and sensors .
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors or resources can be interrupted and resumed by another job. For example, a CPU can be preempted by a higher priority job and resume the execution of the lower priority job later.
- Non-preemptable processors or resources cannot be interrupted and resumed by another job. For example, a printer cannot be preempted by another job until it finishes printing the current job.
- Processors and resources can also be classified into two categories: dedicated and shared.
- Dedicated processors or resources are assigned to a single job and cannot be used by any other job. For example, a dedicated CPU can only execute one job at a time.
- Shared processors or resources can be used by multiple jobs, but only one job can use them at a time. For example, a shared memory can be accessed by multiple jobs, but only one job can read or write to it at a time.
- Processors and resources can affect the performance and schedulability of real-time systems. Therefore, they need to be managed and allocated efficiently and effectively .
- Some of the challenges and techniques for managing and allocating processors and resources in real-time systems are:
  - Processor scheduling: deciding which job to execute on which processor at any given time .
  - Resource allocation: deciding which job to grant access to which resource at any given time .
  - Processor affinity: assigning a job to a specific processor or a set of processors to reduce the overhead of context switching and cache misses.
  - Processor tuning and optimization: adjusting the processor parameters and settings to improve the performance and predictability of real-time applications .
  - Resource locking and synchronization: preventing concurrent access to shared resources by multiple jobs to avoid data inconsistency and deadlock .
  - Resource reservation: allocating a portion of a resource to a specific job or a class of jobs to guarantee their quality of service.
  - Resource reclaiming: utilizing the unused or underutilized resources by other jobs to improve the system utilization and throughput.