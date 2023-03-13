The following diagram illustrates the basic architecture of a cluster middleware and SSI for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing.

```
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    Node 1       |    Node 2       |    Node 3       |    Node 4       |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    OS 1         |    OS 2         |    OS 3         |    OS 4         |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    SSI          |    SSI          |    SSI          |    SSI          |
|    Middleware   |    Middleware   |    Middleware   |    Middleware   |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    User-level   |    User-level   |    User-level   |    User-level   |
|    Environment  |    Environment  |    Environment  |    Environment  |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    User         |    User         |    User         |    User         |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
```

The cluster middleware and SSI layer provides a unified view of the cluster to the user, the applications, and the network. It supports features such as:

- Single root file system
- Single process space
- Single I/O space
- Single IPC space
- Single network space
- Single administration space
- Load balancing
- Fault tolerance
- High availability

The user-level environment consists of tools and libraries that enable parallel and distributed computing on the cluster, such as:

- Message passing interface (MPI)
- Parallel virtual machine (PVM)
- MapReduce
- OpenMP
- Distributed shared memory (DSM)
- Grid computing
- Cloud computing

The user can interact with the cluster as if it were a single machine, without being aware of the underlying hardware and software details. The user can run applications, access files, communicate with other processes, and manage the cluster resources using the SSI middleware and user-level environment.