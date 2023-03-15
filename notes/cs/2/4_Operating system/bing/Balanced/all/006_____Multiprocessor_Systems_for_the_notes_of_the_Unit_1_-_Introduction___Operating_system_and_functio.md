# Multiprocessor Systems

- A multiprocessor system is a computer system that has two or more central processing units (CPUs) that work in parallel to perform the required operations .
- The main objective of using a multiprocessor system is to increase the execution speed and throughput of the system .
- Multiprocessor systems are also called tightly coupled systems because the CPUs share the same computer bus, memory, clock, and peripheral devices .
- There are two main types of multiprocessor systems: asymmetric multiprocessing system and symmetric multiprocessing system .

## Asymmetric Multiprocessing System

- In this type of system, one processor behaves as a master and the other processors behave as slaves .
- The master processor is responsible for scheduling, managing, and allocating tasks to the slave processors .
- The slave processors execute the tasks assigned by the master processor and communicate with it through interrupts or messages .
- The advantages of this type of system are simplicity, low cost, and easy implementation .
- The disadvantages of this type of system are low scalability, high dependency on the master processor, and poor load balancing .

## Symmetric Multiprocessing System

- In this type of system, all the processors have equal status and access to the shared resources .
- The processors communicate and cooperate with each other through a common memory or a message-passing mechanism .
- The tasks are distributed among the processors by a common operating system or a distributed operating system .
- The advantages of this type of system are high scalability, high performance, and good load balancing .
- The disadvantages of this type of system are complexity, high cost, and synchronization overhead .