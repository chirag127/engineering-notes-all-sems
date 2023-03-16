### Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion.
- Examples of processors are computers, transmission links, disks, and database servers.
- Processors can be configured and optimized for real-time applications by using workload-aware tuning and optimizations that help bound data access timings.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs or allocated exclusively to one job.
- Examples of resources are memory, files, printers, and sensors.
- Resources can be managed by using different policies and protocols that ensure mutual exclusion, deadlock avoidance, and priority inheritance.
- Real-time systems need to coordinate the access and allocation of processors and resources among multiple jobs that have timing constraints and deadlines.
- Real-time operating systems (RTOS) are specialized operating systems that serve real-time applications that process data without any buffering delay .
- RTOS have features such as preemptive scheduling, fast context switching, interrupt handling, inter-task communication, and time synchronization .
- Examples of RTOS are FreeRTOS, VxWorks, QNX, and RTLinux.