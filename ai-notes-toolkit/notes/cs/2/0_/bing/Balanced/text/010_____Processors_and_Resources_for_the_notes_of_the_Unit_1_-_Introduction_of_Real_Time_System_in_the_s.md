### Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job or a task. A job or a task must have one or more processors in order to execute and proceed towards completion.
- Examples of processors are computers, transmission links, disks, and database servers.
- Processors can be configured and optimized to meet the real-time requirements of the applications, such as bounded data access timings and precise time synchronization .
- Resources are also called passive resources. They are not essential for the execution of a job or a task, but they may be required by some jobs or tasks during their execution. A job or a task may or may not require a resource during its execution.
- Examples of resources are memory, files, printers, and sensors.
- Resources can be shared or exclusive among different jobs or tasks. Shared resources can be accessed by multiple jobs or tasks concurrently, while exclusive resources can be accessed by only one job or task at a time.
- Resources can cause contention or blocking among different jobs or tasks. Contention occurs when multiple jobs or tasks try to access the same resource at the same time, and blocking occurs when a job or a task has to wait for a resource that is occupied by another job or task.
- Resources can be managed by different policies or protocols, such as priority inheritance, priority ceiling, and deadlock avoidance. These policies or protocols aim to reduce the contention or blocking among different jobs or tasks, and to ensure the correctness and timeliness of the real-time system.