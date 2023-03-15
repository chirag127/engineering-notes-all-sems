### Multiprocess Systems

- A multiprocess system is a computer system that has more than one processor or CPU that can work in parallel to execute multiple tasks.  
- A multiprocess system can be classified into two types: symmetric multiprocessing (SMP) and asymmetric multiprocessing (AMP).  
  - In SMP, all the processors are identical and have equal access to the shared resources, such as memory, I/O devices, and buses. The operating system can assign any task to any processor without any preference.  
  - In AMP, the processors are different and have different roles and access to the shared resources. The operating system can assign specific tasks to specific processors according to their capabilities and priorities.  
- The advantages of a multiprocess system are:  
  - It can increase the performance and throughput of the system by dividing the workload among the processors.  
  - It can enhance the reliability and fault tolerance of the system by providing redundancy and backup for the processors.  
  - It can support the scalability and flexibility of the system by allowing the addition or removal of processors as needed.  
- The challenges of a multiprocess system are:  
  - It requires a complex and efficient operating system that can manage the coordination and synchronization of the processors and the shared resources.  
  - It may incur high overhead and cost for the communication and synchronization among the processors and the shared resources.  
  - It may face the issues of load balancing, resource contention, and deadlock among the processors and the shared resources.  

: https://www.tutorialspoint.com/what-is-a-multiprocessing-operating-system
: https://digitalthinkerhelp.com/what-is-multiprocessor-operating-system-and-its-examples/
: https://byjus.com/gate/multiprocessing-operating-system-notes/
: https://en.wikipedia.org/wiki/Multiprocessor_system_architecture