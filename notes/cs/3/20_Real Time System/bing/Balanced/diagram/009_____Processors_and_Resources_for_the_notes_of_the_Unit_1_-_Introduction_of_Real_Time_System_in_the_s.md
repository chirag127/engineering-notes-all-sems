### Processors and Resources for Real Time System

- A real time system is a system that must respond to events or inputs within a specified time window, often with strict deadlines and constraints.
- A real time system consists of hardware and software components that work together to process, analyze, and act on the incoming data in real time.
- Processors and resources are two important components of a real time system that affect its performance, reliability, and functionality.

#### Processors

- Processors are also known as active resources. They are essential for the execution of a job. A job is a unit of work that must be completed by a real time system.
- A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission links.
- Processors can be classified into two types: single-processor and multiprocessor systems.
- Single-processor systems have only one processor that executes all the jobs in the system. They are simpler, cheaper, and easier to program than multiprocessor systems. However, they have limited processing power and may not be able to handle complex or concurrent jobs.
- Multiprocessor systems have two or more processors that can execute jobs in parallel or distributed manner. They are more powerful, scalable, and flexible than single-processor systems. However, they are more expensive, complex, and challenging to program and coordinate than single-processor systems.
- Processors can also be classified into two types: general-purpose and dedicated processors.
- General-purpose processors are multipurpose and can serve a wide range of use cases, which include data crunching in the cloud and data centers, gaming and media PCs, office laptop, and devices at the edge. They have more compute within the allotted time window.
- Dedicated processors are specialized and optimized for specific real time applications, such as industrial control, automotive, robotics, and aerospace. They have more predictable and deterministic behavior and can meet strict timing and performance requirements.
- Intel® Time Coordinated Computing (Intel® TCC) enabled processors are examples of dedicated processors that deliver optimal compute and time performance for real time applications. They can pair with Intel® Ethernet Controllers featuring IEEE 802.1 Time-Sensitive Networking (TSN), or with any number of other popular networking devices to power complex real time systems .

#### Resources

- Resources are also known as passive resources. A job may or may not require a resource during its execution. A resource is a shared entity that can be used by one or more jobs at a time. Example: memory, disk, printer, sensor, actuator.
- Resources can be classified into two types: preemptable and non-preemptable resources.
- Preemptable resources can be taken away from a job before it finishes using them. They can be allocated and deallocated dynamically based on the priority and demand of the jobs. Example: memory, disk, processor.
- Non-preemptable resources cannot be taken away from a job before it finishes using them. They can be allocated and deallocated only at the beginning and end of the job. Example: printer, sensor, actuator.
- Resources can also be classified into two types: consumable and reusable resources.
- Consumable resources are depleted after being used by a job. They can be replenished or regenerated after some time or by some external action. Example: battery, fuel, ink.
- Reusable resources are not depleted after being used by a job. They can be used again by another job without any delay or intervention. Example: memory, disk, processor.
- Resources can also be classified into two types: local and global resources.
- Local resources are accessible only by the jobs running on the same processor or node. They have lower access time and overhead than global resources. Example: cache, register, local memory.
- Global resources are accessible by the jobs running on any processor or node in the system. They have higher access time and overhead than local resources. Example: disk, network, shared memory.