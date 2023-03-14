### Shared memory for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Shared memory is a form of memory architecture where physically separated memories can be addressed as a single shared address space.
- Shared memory can be implemented in distributed systems, where there is no physical shared memory, by using distributed shared memory (DSM) systems .
- DSM systems provide a virtual address space that is shared between all nodes in the distributed system  .
- DSM systems can be achieved via software or hardware. Software DSM systems can be implemented in the operating system, or as a programming library or language. Hardware DSM systems can use cache coherence circuits or network interface controllers.
- DSM systems can use different approaches to implement the shared memory model, such as:
  - Page-based approach: using virtual memory techniques to map pages of shared memory to local memory .
  - Shared-variable approach: using routines to access shared variables that are stored in a distributed manner.
  - Object-based approach: using object-oriented principles to access shared data that are encapsulated in objects.
- DSM systems have some advantages, such as:
  - Scaling well with a large number of nodes.
  - Hiding the message passing from the programmers .
  - Handling complex and large databases without replication or sending the data to processes.
  - Providing large virtual memory space.
  - Making programs more portable due to common programming interfaces.
  - Shielding programmers from sending or receiving primitives.
- DSM systems also have some disadvantages, such as:
  - Being generally slower to access than non-distributed shared memory.
  - Having to provide additional protection against simultaneous accesses to shared data.
  - Incurring a performance penalty due to network latency and consistency maintenance .
  - Giving little programmer control over the actual messages being generated.
  - Requiring programmers to understand consistency models to write correct programs.
- DSM systems can be compared with message passing systems, which are another way of communication and coordination in distributed systems. Some differences are:
  - In message passing, variables have to be marshalled, while in DSM, variables are shared directly.
  - In message passing, the cost of communication is obvious, while in DSM, the cost of communication is invisible.
  - In message passing, processes are protected by having private address space, while in DSM, processes could cause error by altering data.
  - In message passing, processes should execute at the same time, while in DSM, processes can execute asynchronously.
  - In message passing, programs are usually longer and harder to understand, while in DSM, programs are usually shorter and easier to understand.

- A possible mnemonic to remember the advantages and disadvantages of DSM systems is:

  - **S**calable, **H**ides message passing, **H**andles databases, **P**rovides memory space, **M**akes programs portable, **S**hields programmers: these are the advantages of **SHH PM'S** systems.
  - **S**lower, **P**rotection needed, **P**erformance penalty, **L**ittle control, **C**onsistency models: these are the disadvantages of **SPPLC** systems.