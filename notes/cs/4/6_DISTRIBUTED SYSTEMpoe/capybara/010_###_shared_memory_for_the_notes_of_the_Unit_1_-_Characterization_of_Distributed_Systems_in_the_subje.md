### Shared Memory for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

Shared memory is a form of inter-process communication that enables processes to share a common area of memory. Multiple processes can access and update the shared memory, which facilitates data sharing and communication between processes. In distributed systems, shared memory is used to enable communication between processes running on different machines.

#### How Shared Memory Works

Shared memory involves the creation of a shared memory segment that is accessible by multiple processes. The shared memory segment is created by one process, and other processes can access it using a shared memory key. Once a process has access to the shared memory segment, it can read from and write to it just like it would with any other area of memory.

#### Advantages of Shared Memory

- Shared memory is fast since it allows for direct communication between processes without the need for message passing.
- It is efficient since it eliminates the overhead associated with message passing.
- Shared memory allows for large amounts of data to be shared between processes without the need to copy the data.

#### Disadvantages of Shared Memory

- Shared memory can lead to synchronization issues between processes since multiple processes are accessing and updating the same area of memory.
- If a process crashes, it can corrupt the shared memory segment and cause issues for other processes accessing the same segment.

#### Examples of Shared Memory

Shared memory is used in many different types of distributed systems, such as:

- Distributed databases
- Distributed file systems
- Distributed computing environments

#### Learning Trick

To remember the advantages of shared memory, think of the acronym FEE:

- Fast
- Efficient
- Eliminates copying of data