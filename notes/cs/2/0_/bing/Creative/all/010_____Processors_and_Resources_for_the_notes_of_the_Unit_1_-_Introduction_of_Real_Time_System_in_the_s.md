# Processors and Resources

- Processors and resources are two major types of system components that are involved in the execution of real-time tasks.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission link, disk, database server.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. A job may need to acquire and release a resource multiple times during its execution. Example: memory, file, printer, semaphore.
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors or resources can be interrupted and resumed by another job without affecting their functionality or state. Example: CPU, memory.
- Non-preemptable processors or resources cannot be interrupted and resumed by another job without affecting their functionality or state. Example: disk, printer, network.
- Processors and resources can also be classified into two categories: dedicated and shared.
- Dedicated processors or resources are assigned to a single job and cannot be used by any other job. Example: private memory, dedicated CPU core.
- Shared processors or resources can be used by multiple jobs, but only one job can use them at a time. Example: public memory, shared CPU core.
- Processors and resources can affect the performance and schedulability of real-time tasks. Therefore, they need to be managed and allocated efficiently by the real-time operating system (RTOS).
- A RTOS is an operating system that serves real-time applications that process data without any buffering delay. It has to meet the timing constraints and deadlines of the real-time tasks.
- A RTOS typically consists of the following components:
  - Task scheduler: It decides which task to execute next based on the priority, deadline, and resource requirements of the tasks.
  - Task dispatcher: It switches the context between the tasks and assigns the processor to the selected task.
  - Resource manager: It manages the allocation and deallocation of the resources to the tasks and handles the resource conflicts and contention.
  - Interrupt handler: It handles the external and internal interrupts that may occur during the execution of the tasks and invokes the appropriate routines.
  - Clock and timer: It provides the time reference and the timing services for the tasks and the RTOS.
  - Communication and synchronization: It provides the mechanisms for the tasks to communicate and synchronize with each other and with the external devices.