### Programming for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network and using them as a single system for high-performance tasks  .
- Cluster computing can provide faster computational speed, enhanced data integrity, higher availability, and better scalability than a single computer .
- Cluster computing can be classified into different types based on the degree of coupling, the architecture, the communication, and the application  .
  - Degree of coupling: loosely coupled clusters have independent nodes that communicate over a network, while tightly coupled clusters have nodes that share memory or disk space.
  - Architecture: symmetric clusters have nodes that perform the same role and function, while asymmetric clusters have nodes that perform different roles and functions.
  - Communication: message passing clusters use explicit messages to exchange data between nodes, while shared memory clusters use a common memory space to access data.
  - Application: homogeneous clusters have nodes that run the same operating system and software, while heterogeneous clusters have nodes that run different operating systems and software.
- Cluster computing requires programming models and tools that can exploit the parallelism and the communication between nodes  .
  - Programming models: MPI (Message Passing Interface) is a standard for message passing programming that supports point-to-point and collective communication. OpenMP (Open Multi-Processing) is a standard for shared memory programming that supports parallel loops and regions. MapReduce is a framework for distributed data processing that supports parallel map and reduce functions.
  - Tools: compilers, debuggers, performance analyzers, and libraries that can help programmers develop, test, optimize, and run cluster applications. Examples of tools are GCC, GDB, PAPI, BLAS, and LAPACK.