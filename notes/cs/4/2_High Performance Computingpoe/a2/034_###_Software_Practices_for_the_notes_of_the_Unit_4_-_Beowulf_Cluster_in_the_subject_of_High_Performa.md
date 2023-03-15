 Here is the content in markdown format for the topic -

### Software Practices for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

#### Message Passing Interface (MPI)
- MPI is a standardized and portable message-passing system for distributed-memory parallel computers.
- It allows processes to communicate with each other by sending and receiving messages.
- MPI has point-to-point communication functions that allow two processes to exchange messages with each other.
- It also has collective communication functions that allow groups of processes to coordinate their work together.
- MPI programs must explicitly specify when and how processes will communicate with one another. This explicitness gives the programmer significant control over the performance of the parallel program.

Mnemonic - 'MPI passes messages between processes to parallelize computation'

#### Parallel Virtual Machine (PVM)
- PVM is a software system that permits a heterogeneous collection of Unix and/or Windows computers hooked together by a network to be used as a single large parallel computer.
- The aggregate computing power of a PVM cluster can be used to solve computationally intensive problems.
- PVM provides an easy-to-use software environment for coordinating the simultaneous use of widely distributed, heterogeneous resources.
- In PVM, the programmer identifies chunks of a job that can be executed in parallel, called "tasks", and the system automatically handles the details of load balancing and communication.

Advantages - Easy to program and portable. Supports heterogeneous systems.

Disadvantages - Less efficient and flexible than MPI. Limited to few thousand processors.

#### Globus Toolkit
- The Globus Toolkit is an open source software toolkit used for building grid systems and applications.
- It includes software services and libraries for resource monitoring, discovery, and management, as well as communication and authentication.
- The Globus toolkit utilizes standard technologies such as HTTPS, GSI, and GRAM to address computer architectures, wide area networks, and security which enables resource sharing, application integration, and collaboration across institutional boundaries.
- It provides the infrastructure necessary to share computing power, databases, instruments, and other resources across organizational and geographical boundaries.

Applications - Grid computing, high throughput computing, data intensive computing, collaborative computing.