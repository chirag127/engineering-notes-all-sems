# Parallel Programming with MPL for Beowulf Cluster

- A Beowulf cluster is a private network of computers (usually Alpha or Intel boxes) running a stripped down version of Linux .
- A Beowulf cluster can function like a single massively parallel computer by using a parallel programming API like MPI or PVM .
- MPI (Message Passing Interface) and PVM (Parallel Virtual Machine) are libraries that permit the programmer to divide a task among a group of networked computers, and collect the results of processing .
- MPI and PVM provide routines for sending and receiving messages, synchronizing processes, broadcasting data, and performing collective operations.
- MPI is more widely used than PVM, and has several implementations for clusters, such as MPICH, LAM/MPI, and Open MPI .
- Parallel programming with MPI requires the programmer to specify the number of processes, the communication topology, the data distribution, and the synchronization points.
- Parallel programming with MPI can improve the performance of applications that have high computational demands, such as numerical simulations, image processing, and Monte Carlo methods .
- Parallel programming with MPI can also exploit the scalability and fault tolerance of Beowulf clusters, by allowing the programmer to adjust the number of processes and handle errors .