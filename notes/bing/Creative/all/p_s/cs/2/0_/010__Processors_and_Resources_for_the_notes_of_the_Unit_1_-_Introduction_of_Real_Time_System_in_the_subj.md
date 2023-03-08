### Processors and Resources

- Processors and resources are two important components of real time systems that affect their performance, reliability and cost.
- Processors are also known as active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission links.
- Resources are also known as passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can use it at a time. Example: printer, disk, memory.
- Processors and resources can be classified into two types: dedicated and shared.
  - Dedicated processors and resources are allocated to a single job or task and cannot be used by any other job or task. They provide high performance and predictability, but also increase the cost and complexity of the system. Example: a processor that runs only one real time application, a disk that stores only one file.
  - Shared processors and resources are available to multiple jobs or tasks and can be used by them according to some scheduling policy. They provide flexibility and efficiency, but also introduce uncertainty and contention. Example: a processor that runs multiple real time applications, a disk that stores multiple files.
- Processors and resources can also be classified into two types: preemptive and non-preemptive.
  - Preemptive processors and resources can be taken away from a job or task before it finishes its execution, and given to another job or task with higher priority or urgency. They allow the system to respond quickly to dynamic events and deadlines, but also increase the overhead and complexity of the system. Example: a processor that can switch between different real time applications, a printer that can print different documents.
  - Non-preemptive processors and resources cannot be taken away from a job or task before it finishes its execution, and must be released by the job or task voluntarily. They ensure the atomicity and consistency of the job or task, but also delay the execution of other jobs or tasks that may have higher priority or urgency. Example: a processor that runs only one real time application until it completes, a disk that locks a file until it is written.
- Processors and resources can also be classified into two types: local and global.
  - Local processors and resources are accessible only by the jobs or tasks that run on the same processor or node. They reduce the communication and synchronization overhead, but also limit the scalability and fault tolerance of the system. Example: a processor that runs only local real time applications, a memory that stores only local data.
  - Global processors and resources are accessible by the jobs or tasks that run on different processors or nodes. They increase the communication and synchronization overhead, but also enable the scalability and fault tolerance of the system. Example: a processor that runs global real time applications, a disk that stores global data.
- Processors and resources can also be classified into two types: static and dynamic.
  - Static processors and resources are allocated to the jobs or tasks at the design time or compile time, and cannot be changed at the run time. They simplify the analysis and verification of the system, but also reduce the adaptability and robustness of the system. Example: a processor that runs a fixed set of real time applications, a memory that allocates a fixed amount of space for each application.
  - Dynamic processors and resources are allocated to the jobs or tasks at the run time, and can be changed according to the system state and environment. They complicate the analysis and verification of the system, but also increase the adaptability and robustness of the system. Example: a processor that runs a variable set of real time applications, a memory that allocates a variable amount of space for each application.

Some possible mnemonics and learning tricks for the topic are:

- To remember the types of processors and resources, use the acronym DSPN LGSD: Dedicated, Shared, Preemptive, Non-preemptive, Local, Global, Static, Dynamic.
- To remember the advantages and disadvantages of each type, use the following table:

| Type | Advantage | Disadvantage |
| --- | --- | --- |
| Dedicated | High performance and predictability | High cost and complexity |
| Shared | Flexibility and efficiency | Uncertainty and contention |
| Preemptive | Quick response to dynamic events and deadlines | High overhead and complexity |
| Non-preemptive | Atomicity and consistency | Delay of other jobs or tasks |
| Local | Low communication and synchronization overhead | Low scalability and fault tolerance |
| Global | High scalability and fault tolerance | High communication and synchronization overhead |
| Static | Simple analysis and verification | Low adaptability and robustness |
| Dynamic | High adaptability and robustness | Complex analysis and verification |

- To remember the examples of each type, use the following associations:

| Type | Example |
| --- | --- |
| Dedicated | A processor that runs only one real time application, a disk that stores only one file |
| Shared | A processor that runs multiple real time applications, a disk that stores multiple files |
| Preemptive | A processor that can switch between different real time applications, a printer that can print different documents |
| Non-preemptive | A processor that runs only one real time application until it completes, a disk that locks a file until it is written |
| Local | A processor that runs only local real time applications, a memory that stores only local data |
| Global | A processor that runs global real time applications, a disk that stores global data |
| Static | A processor that runs a fixed set of real time applications, a memory that allocates a fixed amount of space for each application |
| Dynamic | A processor that runs a variable set of real time applications, a memory that allocates a variable amount of space for each application |