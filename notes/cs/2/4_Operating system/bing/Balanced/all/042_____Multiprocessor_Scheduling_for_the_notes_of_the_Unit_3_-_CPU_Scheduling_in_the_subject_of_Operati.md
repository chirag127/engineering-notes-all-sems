# Multiprocessor Scheduling

- Multiprocessor scheduling is the process of allocating processes or threads to multiple processors in a system that has more than one processor but shares the same memory, bus, and input/output devices  .
- Multiprocessor scheduling aims to achieve load balancing, high throughput, low response time, and efficient utilization of resources .
- Multiprocessor scheduling is more complex than single processor scheduling because of the following challenges  :
  - Process migration: the movement of processes from one processor to another for load balancing or other reasons.
  - Process synchronization: the coordination of processes that share data or resources across processors.
  - Cache coherence: the consistency of data stored in different processors' caches.
  - Memory access latency: the delay in accessing data from memory due to contention or distance.
- There are two main approaches to multiprocessor scheduling :
  - Symmetric multiprocessing (SMP): each processor is self-scheduling and can run any process in the system. Processes may be in a common ready queue or in separate queues for each processor. SMP is simple and flexible, but may cause contention for the shared queue or imbalance in the processor load.
  - Asymmetric multiprocessing (AMP): one processor is designated as the master and is responsible for scheduling processes to other processors. Processes are in a single ready queue and are assigned to processors by the master. AMP avoids contention and imbalance, but may cause overhead and bottleneck in the master processor.
- There are also different algorithms or policies for multiprocessor scheduling, such as :
  - Gang scheduling: a group of related processes or threads are scheduled together on a set of processors at the same time. This ensures synchronization and communication among the processes or threads, but may cause fragmentation and underutilization of processors.
  - Processor affinity: a process or thread is preferred to run on the same processor where it ran previously. This exploits the locality of data and reduces cache misses, but may cause imbalance and starvation of processors.
  - Load sharing: a process or thread is assigned to the processor with the least load or the shortest queue. This distributes the workload evenly among the processors, but may cause migration and synchronization overhead.