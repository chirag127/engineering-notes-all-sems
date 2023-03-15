### Programming for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

In the world of High Performance Computing, cluster computing has become a popular method to achieve high performance. Cluster computing involves a group of computers that work together to solve a problem. In order to make use of cluster computing, programmers need to understand how to write programs that can run on a cluster. Here are some important things to keep in mind when programming for cluster computing:

1. **Parallel Programming:** Writing programs for cluster computing involves parallel programming. This means that the program is divided into small tasks that can be executed simultaneously on different computers in the cluster. The result of these tasks is then combined to obtain the final result.

2. **Message Passing Interface (MPI):** MPI is a standard library used for parallel programming in cluster computing. It provides a set of functions that allow programs to communicate with each other over the network. MPI can be used with many programming languages, including C, C++, and Fortran.

3. **Load Balancing:** In cluster computing, load balancing is an important concept. It involves distributing the workload evenly across all the computers in the cluster. This ensures that no single computer is overloaded and the overall performance of the cluster is optimized.

4. **Fault Tolerance:** Cluster computing involves a large number of computers working together. This increases the chances of hardware or software failures. Programs need to be designed to handle these failures gracefully and continue running without interruption.

5. **Scalability:** Programs designed for cluster computing should be scalable. This means that they should be able to handle an increasing number of computers in the cluster without affecting performance.

Mnemonics and Learning Tricks:

- Remember the acronym PLFS (Parallel programming, Load balancing, Fault tolerance, Scalability) to keep in mind the important concepts of programming for cluster computing.
- Think of the cluster as a team of workers, each with a specific task. The team leader (program) divides the work among the workers (computers) and ensures that each worker is doing its fair share (load balancing). The team leader also makes sure that if one worker falls ill (hardware or software failure), the work is still completed on time (fault tolerance). As the team grows in size (scalability), the team leader needs to be able to manage them efficiently.