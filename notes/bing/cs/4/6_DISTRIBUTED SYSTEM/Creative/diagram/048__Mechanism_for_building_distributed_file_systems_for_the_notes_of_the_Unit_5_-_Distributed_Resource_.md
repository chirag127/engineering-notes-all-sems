A distributed file system (DFS) is a file system that allows access to files from multiple hosts sharing via a computer network. A DFS can have different mechanisms for building and managing the file system, such as file models, file accessing models, file sharing semantics, and file replication.

The following diagram illustrates the basic architecture of a DFS using a client-server model, where clients can access files stored on servers via a network. The servers can also communicate with each other to synchronize the file data and metadata.

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Client 1     |     |    Client 2     |     |    Client 3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Server 1     |-----|    Server 2     |-----|    Server 3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    File 1       |     |    File 2       |     |    File 3       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```