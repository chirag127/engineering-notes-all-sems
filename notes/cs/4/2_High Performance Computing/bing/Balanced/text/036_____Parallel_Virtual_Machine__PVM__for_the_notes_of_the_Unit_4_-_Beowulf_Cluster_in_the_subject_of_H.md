### Parallel Virtual Machine (PVM) for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- PVM is a software tool for parallel networking of computers.
- It allows a network of heterogeneous Unix and/or Windows machines to be used as a single distributed parallel processor.
- It can solve large computational problems more cost effectively by using the aggregate power and memory of many computers .
- It provides a message-passing interface for communication among the processors.
- It supports dynamic addition and deletion of machines to the virtual machine.
- It supports fault tolerance and load balancing.
- It can be used as stand-alone software or as a foundation for other heterogeneous network software.
- It consists of three components: the PVM daemon, the PVM library, and the PVM console.
- The PVM daemon runs on each machine and manages the communication and computation on that machine.
- The PVM library provides the application programming interface (API) for writing PVM programs.
- The PVM console is a user interface for controlling and monitoring the PVM virtual machine.
- Some of the commands that can be used in the PVM console are:
  - add: to add machines to the virtual machine
  - conf: to show the configuration of the virtual machine
  - ps: to show the running processes and their task IDs (TIDs)
  - kill: to stop a running process
  - halt: to stop the virtual machine