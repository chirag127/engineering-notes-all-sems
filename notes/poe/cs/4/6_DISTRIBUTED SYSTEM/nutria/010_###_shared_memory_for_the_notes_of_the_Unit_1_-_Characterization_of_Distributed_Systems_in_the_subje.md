
### Shared Memory for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of DISTRIBUTED SYSTEM

Shared memory is a type of inter-process communication (IPC) mechanism used in distributed systems. It is a form of memory that is shared among multiple processes and can be read and written by any of the participating processes. Shared memory is used to store data that needs to be accessed by multiple processes, such as a database or a shared file system.

**Advantages:**

- High performance: Shared memory is the fastest form of IPC, since data is accessed directly from memory and no serialization or deserialization is required.
- Easy to use: Shared memory is easy to use, as it does not require any special libraries or protocols.
- Low overhead: Since data is stored in memory, there is no need for additional overhead associated with serialization and deserialization.

**Disadvantages:**

- Limited scalability: Shared memory can become a bottleneck when multiple processes need to access the same data.
- Data synchronization: Data synchronization between processes is a complex task and requires additional programming.
- Security: Shared memory is vulnerable to malicious access, since all processes have access to the same data.

**Mnemonics and Learning Tricks:**

- **S**hared **M**emory is **F**ast and **E**asy to **U**se but has **L**imited **S**calability.
- **S**hared **M**emory requires **D**ata **S**ynchronization and **S**ecurity.