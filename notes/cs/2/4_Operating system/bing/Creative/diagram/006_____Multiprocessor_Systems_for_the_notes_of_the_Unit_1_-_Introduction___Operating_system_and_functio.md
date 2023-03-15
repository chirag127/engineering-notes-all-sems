### Multiprocessor Systems

- A multiprocessor system is a computer system that has two or more central processing units (CPUs) that work in parallel to perform the required operations .
- The multiple CPUs are connected with physical memory, computer buses, clocks, and peripheral devices. These systems are referred to as tightly coupled systems.
- The main objective of using a multiprocessor system is to increase the execution speed of the programs and improve the system throughput.
- There are two main types of multiprocessor systems: asymmetric multiprocessing system and symmetric multiprocessing system .

#### Asymmetric multiprocessing system

- In this type of system, one processor behaves as a master and the other processors behave as slaves .
- The master processor is responsible for scheduling, managing, and allocating tasks to the slave processors .
- The slave processors execute the tasks assigned by the master processor and communicate with it through shared memory or message passing .
- The advantages of this type of system are simplicity, low cost, and easy implementation .
- The disadvantages of this type of system are low scalability, high dependency on the master processor, and possible underutilization of the slave processors .

#### Symmetric multiprocessing system

- In this type of system, all the processors have equal access to the system resources and can perform any task .
- The processors communicate and coordinate with each other through shared memory or message passing .
- The operating system is responsible for scheduling, managing, and allocating tasks to the processors .
- The advantages of this type of system are high scalability, high performance, high reliability, and load balancing .
- The disadvantages of this type of system are complexity, high cost, and synchronization overhead .