# Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of a distributed system can execute concurrently, without having to wait for each other.
  - No global clock: There is no global notion of time in a distributed system, and the components may have different local clocks that are not synchronized.
  - Independent failures: The components of a distributed system may fail independently, without affecting the whole system.
  - Heterogeneity: The components of a distributed system may have different hardware, software, network, and data formats.
  - Scalability: A distributed system should be able to accommodate an increasing number of components and users, without degrading the performance or functionality of the system.
  - Transparency: A distributed system should hide the complexity and diversity of its components from the users, and provide a uniform and consistent interface to access the system.
- A distributed system can be classified into different types based on the degree of coupling among the components, such as:
  - Client-server systems: A client-server system consists of a set of servers that provide services to a set of clients. The clients and servers communicate through a network using a request-reply protocol. The servers are usually centralized and have a fixed location, while the clients are distributed and mobile.
  - Peer-to-peer systems: A peer-to-peer system consists of a set of peers that act as both clients and servers. The peers communicate through a network using a message-passing protocol. The peers are usually decentralized and have no fixed location, and they can join and leave the system dynamically.
  - Distributed object systems: A distributed object system consists of a set of objects that encapsulate data and behavior. The objects communicate through a network using a remote method invocation protocol. The objects are usually distributed and heterogeneous, and they can be replicated and migrated across the system.
  - Distributed file systems: A distributed file system consists of a set of files that are stored and accessed by a set of processes. The files communicate through a network using a file access protocol. The files are usually distributed and replicated, and they provide a consistent and transparent view of the file system to the processes.
  - Distributed database systems: A distributed database system consists of a set of databases that are stored and manipulated by a set of transactions. The databases communicate through a network using a database access protocol. The databases are usually distributed and replicated, and they provide a consistent and transparent view of the data to the transactions.