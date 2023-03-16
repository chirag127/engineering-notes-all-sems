### Parallel Virtual Machine (PVM) for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- PVM is a software package that enables a network of heterogeneous computers (Unix and/or Windows) to be used as a single large parallel computer .
- PVM can be used to solve large computational problems more cost effectively by using the aggregate power and memory of many computers  .
- PVM provides a set of library routines that can be linked with an application program to perform various tasks such as:
  - Creating and managing a virtual machine of networked computers  .
  - Sending and receiving messages among processes in the virtual machine  .
  - Synchronizing processes and broadcasting messages  .
  - Handling errors and faults in the virtual machine  .
- PVM uses a master-slave model of parallel programming, where the master process spawns and controls the slave processes, and the slave processes perform the computation and communicate with the master and/or other slaves  .
- PVM assigns a unique identifier (TID) to each process in the virtual machine, and uses a routing mechanism to deliver messages to the correct destination  .
- PVM supports dynamic addition and deletion of hosts from the virtual machine, allowing for load balancing and fault tolerance  .
- PVM can be used as a stand-alone software or as a foundation for other heterogeneous network software.
- PVM has a console interface (pvm) that allows the user to interact with the virtual machine, such as adding or removing hosts, showing the status of processes, killing processes, etc..