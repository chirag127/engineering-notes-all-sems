### Multiprocessor Systems

- A multiprocessor system is a computer system that has more than one processor, each sharing the same main memory and peripherals, in order to simultaneously process multiple programs or parts of the same program .
- The main objective of a multiprocessor system is to increase the system's execution speed, throughput, reliability, and scalability .
- Multiprocessor systems can be classified into two types based on the memory organization: **shared-memory multiprocessor systems** and **distributed-memory multiprocessor systems** .
- In a shared-memory multiprocessor system, all the processors have direct access to a common physical memory, and can communicate with each other by reading and writing to the shared memory locations . An example of a shared-memory multiprocessor system is a symmetric multiprocessing (SMP) system, in which all the processors are identical and have equal access to the memory and peripherals .
- In a distributed-memory multiprocessor system, each processor has its own local memory, and can communicate with other processors by sending and receiving messages over a network . An example of a distributed-memory multiprocessor system is a cluster system, in which a group of independent computers are connected by a high-speed network and work together as a single system .
- The advantages of multiprocessor systems include:
  - Higher performance and throughput, as multiple processors can execute multiple tasks in parallel .
  - Higher reliability and fault tolerance, as the failure of one processor does not affect the functioning of the rest of the system .
  - Higher scalability, as more processors can be added to the system to increase the processing power .
- The disadvantages of multiprocessor systems include:
  - Higher complexity and cost, as the design and implementation of multiprocessor systems require more hardware and software components, such as memory controllers, interconnection networks, synchronization mechanisms, etc .
  - Higher overhead and contention, as the processors need to coordinate and communicate with each other, and may compete for the shared resources, such as memory and peripherals .
  - Higher difficulty in programming and debugging, as the programmers need to deal with issues such as concurrency, synchronization, data consistency, load balancing, etc .

: Multiprocessor system architecture - Wikipedia
: Multiprocessing - Wikipedia
: Multiprocessor System - an overview | ScienceDirect Topics
: Multiprocessing | Definition & Facts | Britannica
: Multiprocessor Systems - tutorialspoint.com

Some possible mnemonics and learning tricks for the topic are:

- To remember the difference between shared-memory and distributed-memory multiprocessor systems, you can use the acronym **SAD** (Shared-memory, All processors have direct access to memory; Distributed-memory, each processor has its own memory and communicates via network).
- To remember the advantages of multiprocessor systems, you can use the acronym **PARS** (Performance, Availability, Reliability, Scalability).
- To remember the disadvantages of multiprocessor systems, you can use the acronym **COD** (Complexity, Overhead, Difficulty).