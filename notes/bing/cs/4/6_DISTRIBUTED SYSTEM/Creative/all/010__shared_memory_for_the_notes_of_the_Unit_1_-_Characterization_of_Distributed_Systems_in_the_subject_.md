### Shared memory for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Distributed shared memory (DSM) is a technique that implements the shared memory model on a distributed system that has no physically shared memory.
- DSM provides a virtual address space that is shared among all the nodes in the distributed system, and allows the nodes to communicate and synchronize through reading and writing to the shared memory.
- DSM can be achieved via software or hardware. Software DSM relies on the operating system or the middleware to manage the memory consistency and coherence among the nodes. Hardware DSM uses special hardware components such as cache coherence circuits and network interface controllers to implement the shared memory model.
- There are three main ways of implementing DSM: page-based, object-based, and tuple-based.
  - Page-based DSM divides the shared memory into fixed-size pages and distributes them among the nodes. Each page has a home node that is responsible for keeping track of the page status and location. When a node wants to access a page that is not in its local memory, it sends a request to the home node and obtains a copy of the page. The home node also maintains the coherence of the page by invalidating or updating the copies when a write operation occurs.
  - Object-based DSM organizes the shared memory into objects that can be accessed by invoking methods. Each object has a manager node that controls the access and consistency of the object. When a node wants to access an object that is not in its local memory, it sends a request to the manager node and obtains a copy of the object. The manager node also maintains the coherence of the object by using a locking mechanism or a versioning scheme.
  - Tuple-based DSM represents the shared memory as a collection of tuples that can be inserted, read, or removed by the nodes. Each tuple has a name and a value, and can be accessed by using pattern matching. When a node wants to access a tuple that is not in its local memory, it sends a request to a tuple space that stores and manages the tuples. The tuple space also maintains the coherence of the tuples by using a transactional mechanism or a replication scheme.

- The advantages of DSM are:
  - It provides a simple and familiar programming model that abstracts away the details of the underlying distributed system.
  - It allows the programmers to handle synchronization in the shared memory model, which is easier than using message passing or remote procedure calls.
  - It enables the development of parallel and distributed applications that can exploit the large memory and processing power of the distributed system.
  - It improves the performance and scalability of the applications by reducing the communication overhead and exploiting the locality of the data.

- The disadvantages of DSM are:
  - It introduces the complexity and overhead of maintaining the memory consistency and coherence among the nodes, which can affect the performance and correctness of the applications.
  - It requires the nodes to have a common view of the shared memory, which can be difficult to achieve in a dynamic and heterogeneous distributed system.
  - It may suffer from false sharing, which occurs when multiple nodes access different parts of the same page or object, causing unnecessary coherence actions and network traffic.