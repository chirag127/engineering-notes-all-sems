### Parallel Programming with MPL for Beowulf Cluster

- A Beowulf cluster is a private network of computers (usually Alpha or Intel boxes) running a stripped down version of Linux .
- A Beowulf cluster can function like a single massively parallel computer by using a parallel programming API like MPI or PVM .
- MPI (Message Passing Interface) and PVM (Parallel Virtual Machine) are libraries that permit the programmer to divide a task among a group of networked computers, and collect the results of processing.
- MPI is a standard for message-passing communication between processes in a parallel program .
- PVM is a software system that enables a collection of heterogeneous computers to be used as a coherent and flexible concurrent computational resource.
- Parallel programming with MPI or PVM involves writing programs that use the library functions to send and receive messages between processes, and to synchronize and coordinate their execution.
- Some examples of parallel programming with MPI are: Hello World, Manager/Worker, Two-Dimensional Jacobi, Collective Operations, and Parallel Monte Carlo Computation .
- Some advantages of parallel programming with MPI or PVM for Beowulf cluster are: portability, scalability, performance, and flexibility .
- Some challenges of parallel programming with MPI or PVM for Beowulf cluster are: debugging, load balancing, communication overhead, and fault tolerance .