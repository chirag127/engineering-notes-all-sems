# Multiprocess Systems

- A multiprocess system is a computer system that has two or more central processing units (CPUs) that work in parallel to perform the required operations.  
- The multiple CPUs are in communication with each other and share the same computer bus, memory, and other peripheral devices.  
- These systems are referred to as tightly coupled systems.  
- The main objective of using a multiprocess system is to consume high computing power and increase the execution speed of the system.  
- A multiprocess system is a special type of operating system that is used to manage the multiple CPUs and allocate tasks between them.  
- There are two different types of multiprocess systems applied for various environments:  
  - Symmetric multiprocessing (SMP): In this type, each CPU has equal access to the shared resources and performs the same functions. The operating system can assign any task to any CPU. This type is simpler and cheaper to implement, but it may suffer from resource contention and scalability issues.   
  - Asymmetric multiprocessing (AMP): In this type, each CPU has a specific role and performs different functions. The operating system assigns tasks to CPUs according to their roles. This type is more complex and expensive to implement, but it may offer better performance and fault tolerance.   
- Some advantages of multiprocess systems are:  
  - They can increase the throughput and efficiency of the system by executing multiple tasks simultaneously.
  - They can improve the reliability and availability of the system by providing redundancy and fault tolerance.
  - They can enhance the scalability and modularity of the system by allowing the addition or removal of CPUs as needed.
- Some disadvantages of multiprocess systems are:  
  - They require more hardware and software resources and complexity to implement and maintain.
  - They may introduce synchronization and communication overhead and challenges among the CPUs and the shared resources.
  - They may face performance degradation and bottlenecks due to resource contention and load imbalance.