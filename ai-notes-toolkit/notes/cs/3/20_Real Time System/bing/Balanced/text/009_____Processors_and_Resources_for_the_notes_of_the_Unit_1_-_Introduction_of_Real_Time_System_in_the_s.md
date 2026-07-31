### Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. Examples of resources are memory, files, printers, and sensors.
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors or resources can be interrupted and resumed by another job. For example, a CPU can be preempted by a higher priority job and resume the execution of the lower priority job later.
- Non-preemptable processors or resources cannot be interrupted and resumed by another job. For example, a printer cannot be preempted by another job until it finishes printing the current job.
- Processors and resources can also be classified into two categories: dedicated and shared.
- Dedicated processors or resources are assigned to a single job and cannot be used by any other job. For example, a dedicated CPU can only execute one job at a time.
- Shared processors or resources can be used by multiple jobs, but only one job can access them at a time. For example, a shared memory can be accessed by multiple jobs, but only one job can read or write to it at a time.
- Processors and resources can affect the performance and correctness of real-time systems. Therefore, they need to be managed and scheduled carefully to meet the timing constraints and quality of service requirements of the real-time applications  .