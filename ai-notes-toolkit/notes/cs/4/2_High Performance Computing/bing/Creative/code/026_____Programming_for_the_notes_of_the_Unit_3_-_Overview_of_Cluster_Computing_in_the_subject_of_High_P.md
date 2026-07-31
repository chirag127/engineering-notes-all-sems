# Programming for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network and using them as a single system for performing complex tasks  .
- Cluster computing provides benefits such as faster computational speed, enhanced data integrity, higher availability, load balancing and scalability  .
- Cluster computing can be classified into different types based on the architecture, topology, communication, scheduling and application of the nodes. Some common types are:
  - Beowulf cluster: A cluster of commodity hardware that runs Linux or other free software and uses standard network protocols.
  - High-availability cluster: A cluster that ensures minimal downtime and data loss by using redundant hardware, software and network components.
  - Load-balancing cluster: A cluster that distributes the workload among the nodes to optimize performance and resource utilization.
  - High-performance cluster: A cluster that uses specialized hardware and software to achieve maximum speed and efficiency for computationally intensive applications.
- Cluster computing requires programming models and tools that can exploit the parallelism and communication among the nodes. Some common programming models and tools are:
  - Message passing: A programming model that involves explicit sending and receiving of data between the nodes using a library such as MPI (Message Passing Interface) or PVM (Parallel Virtual Machine).
  - Shared memory: A programming model that involves accessing a common memory space by the nodes using a library such as OpenMP (Open Multi-Processing) or POSIX threads.
  - Distributed memory: A programming model that involves accessing distributed data structures by the nodes using a library such as Coarray Fortran or UPC (Unified Parallel C).
  - MapReduce: A programming model that involves applying a map function to process data in parallel and a reduce function to aggregate the results using a framework such as Hadoop or Spark.
  - Cloud computing: A programming model that involves accessing remote computing resources and services over the internet using a platform such as AWS (Amazon Web Services) or Google Cloud.