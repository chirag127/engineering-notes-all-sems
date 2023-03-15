# Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. Examples of resources are memory, files, printers, and sensors.
- Processors and resources can be classified into two categories: dedicated and shared.
- Dedicated processors or resources are allocated to a single job or task and cannot be used by any other job or task. Dedicated processors or resources can guarantee predictable and deterministic performance for the assigned job or task.
- Shared processors or resources are accessible by multiple jobs or tasks and can be used by any job or task that needs them. Shared processors or resources can improve the utilization and efficiency of the system, but they can also introduce contention and interference among the competing jobs or tasks.
- Real-time systems need to manage the allocation and scheduling of processors and resources to meet the timing constraints and quality of service requirements of the real-time applications .
- Real-time systems can use different techniques and algorithms to allocate and schedule processors and resources, such as priority-based, deadline-based, rate-monotonic, earliest deadline first, etc.
- Real-time systems can also use different technologies and solutions to optimize the performance and reliability of processors and resources, such as workload-aware processor tuning, time synchronization, and time-sensitive networking .