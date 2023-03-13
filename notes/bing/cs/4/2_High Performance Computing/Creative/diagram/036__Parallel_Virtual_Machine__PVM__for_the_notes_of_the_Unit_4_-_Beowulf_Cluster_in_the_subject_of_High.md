Parallel Virtual Machine (PVM) is a software tool for parallel networking of computers. It allows a network of heterogeneous Unix and/or Windows machines to be used as a single distributed parallel processor. PVM consists of three components: a daemon process (pvmd) that runs on each machine, a library of functions (libpvm) that provides the interface for writing parallel programs, and a console program (pvm) that allows the user to start, monitor, and control the parallel applications.

The following diagram illustrates the basic architecture of a PVM system:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  pvmd           |    |  pvmd           |    |  pvmd           |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  libpvm         |    |  libpvm         |    |  libpvm         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  PVM program    |    |  PVM program    |    |  PVM program    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Machine A      |    |  Machine B      |    |  Machine C      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
      |                     |                     |
      |                     |                     |
      +---------------------+---------------------+
                            |
                            |
                      +-----------------+
                      |                 |
                      |  pvm            |
                      |                 |
                      +-----------------+
                      |                 |
                      |  User machine   |
                      |                 |
                      +-----------------+
```

In this diagram, three machines (A, B, and C) are running PVM programs that communicate with each other through the libpvm functions. Each machine also has a pvmd process that manages the local resources and communicates with other pvmds. The user machine runs the pvm console program that allows the user to start, monitor, and control the PVM programs on the other machines. The communication between the machines is done through the network. PVM supports various network protocols, such as TCP/IP, UDP, and shared memory. PVM also supports dynamic addition and deletion of machines, fault tolerance, and load balancing. PVM is widely used for developing parallel applications in various domains, such as scientific computing, image processing, artificial intelligence, and distributed systems.