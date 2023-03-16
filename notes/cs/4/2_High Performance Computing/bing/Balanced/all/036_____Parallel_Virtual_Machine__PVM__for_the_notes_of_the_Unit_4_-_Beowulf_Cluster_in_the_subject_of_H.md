# Parallel Virtual Machine (PVM) for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- Parallel Virtual Machine (PVM) is a software tool for parallel networking of computers.
- It is designed to allow a network of heterogeneous Unix and/or Windows machines to be used as a single distributed parallel processor.
- PVM can be used as stand-alone software or as a foundation for other heterogeneous network software.
- PVM provides the following features  :
  - Dynamic addition and deletion of machines to the parallel virtual machine.
  - Task creation and management on the machines of the parallel virtual machine.
  - Message passing communication between tasks using explicit send and receive operations.
  - Group communication operations such as broadcast, barrier, and reduce.
  - Fault tolerance and error recovery mechanisms.
  - Portable and scalable performance across different architectures and platforms.
- PVM consists of three components  :
  - The PVM daemon (pvmd), which runs on each machine and manages the resources and communication of that machine.
  - The PVM library (libpvm), which provides the application programming interface (API) for the user to write PVM programs in C, C++, Fortran, or Java.
  - The PVM console (pvm), which is a command-line tool for the user to interact with the parallel virtual machine, such as adding or deleting machines, spawning or killing tasks, and monitoring the status of the system.
- PVM uses a unique identifier called task identifier (tid) to refer to each task in the parallel virtual machine  .
- PVM uses a message passing model to exchange data between tasks, where each message has a tag, a data type, and a length  .
- PVM supports both blocking and non-blocking communication, as well as buffered and unbuffered communication  .
- PVM also supports group communication, where a group is a collection of tasks that can communicate with each other using collective operations such as broadcast, barrier, reduce, scatter, and gather  .
- PVM can be used to combine multiple Beowulf clusters at a site into a Grid of clusters, where each cluster is a parallel virtual machine and can communicate with other clusters using PVM functions.
- PVM is a widely used software for network parallel computing, and has been applied to various domains such as scientific computing, image processing, artificial intelligence, and distributed databases  .

: https://www.csm.ornl.gov/pvm/pvm_home.html
: https://en.wikipedia.org/wiki/Parallel_Virtual_Machine
: https://etutorials.org/Linux+systems/cluster+computing+with+linux/Part+II+Parallel+Programming/Chapter+10+Parallel+Virtual+Machine/
: http://parallel.vub.ac.be/documentation/pvm/
: https://direct.mit.edu/books/book/2089/PVMA-Users-Guide-and-Tutorial-for-Network-Parallel