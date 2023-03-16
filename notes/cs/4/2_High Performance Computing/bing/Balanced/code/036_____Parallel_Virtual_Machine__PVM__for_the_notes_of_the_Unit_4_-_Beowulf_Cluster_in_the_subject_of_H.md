### Parallel Virtual Machine (PVM) for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- PVM is a software package that enables a network of heterogeneous computers (Unix and/or Windows) to be used as a single large parallel computer .
- PVM can be used to solve large computational problems more cost effectively by using the aggregate power and memory of many computers .
- PVM provides a message-passing interface for communication among the processes running on different machines .
- PVM allows the user to dynamically create and destroy processes, add and delete machines, and handle machine failures and network problems .
- PVM consists of three components: the PVM daemon, the PVM library, and the PVM console .
  - The PVM daemon (pvmd) is a process that runs on each machine and manages the resources and communication of that machine .
  - The PVM library (libpvm) is a set of functions that can be linked with the user's application programs to access the PVM features .
  - The PVM console (pvm) is a program that allows the user to interact with the PVM system, such as adding and deleting machines, spawning and killing processes, and monitoring the status of the system  .
- PVM uses a unique identifier called task ID (tid) to refer to each process in the system .
- PVM supports various data types and data structures, such as integers, floats, doubles, complex numbers, strings, and arrays .
- PVM provides various functions for sending and receiving messages, such as pvm_send, pvm_recv, pvm_psend, pvm_precv, pvm_bcast, pvm_reduce, etc .
- PVM also provides functions for process management, such as pvm_spawn, pvm_exit, pvm_kill, pvm_parent, pvm_mytid, etc .
- PVM can be used to implement various parallel programming models, such as master-slave, pipeline, farm, divide-and-conquer, etc .
- PVM can be integrated with other parallel programming tools, such as MPI, OpenMP, etc .