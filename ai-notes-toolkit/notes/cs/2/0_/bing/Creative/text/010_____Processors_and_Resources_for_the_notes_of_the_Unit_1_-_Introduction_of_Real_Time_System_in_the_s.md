### Processors and Resources

- Processors and resources are two major types of system components that are involved in the execution of real-time tasks.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission link, disk, database server.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource is typically shared by multiple jobs and can be accessed by only one job at a time. A job may need to wait for a resource to become available before using it. Example: printer, file, semaphore, memory.
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors and resources can be interrupted and resumed by other jobs. They allow multitasking and concurrency. Example: CPU, RAM, disk.
- Non-preemptable processors and resources cannot be interrupted and resumed by other jobs. They require exclusive access and mutual exclusion. Example: printer, file, semaphore.
- Processors and resources can affect the timing and performance of real-time tasks. They can introduce delays, overheads, and uncertainties in the execution of tasks.
- Processors and resources need to be managed and allocated efficiently by the real-time operating system (RTOS) to meet the timing constraints and quality of service requirements of real-time applications .
- Processors and resources can be configured and optimized for real-time applications by using techniques such as workload-aware processor tuning, time synchronization, and communication protocols .