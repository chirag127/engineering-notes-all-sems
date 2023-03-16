### Parallel Virtual Machine (PVM) for Beowulf Cluster

- PVM is a software system that enables a collection of heterogeneous computers to be used as a coherent and flexible concurrent computational resource, or a "parallel virtual machine". 
- PVM can be used to create a Beowulf cluster, which is a type of high-performance computing system that consists of a group of inexpensive computers connected by a local area network and running Linux or another Unix-like operating system. 
- PVM provides a set of library functions that allow the programmer to
  - create and manage a parallel virtual machine dynamically by adding or deleting computers as needed
  - spawn parallel tasks on the computers of the parallel virtual machine
  - exchange data and messages between tasks using various communication patterns (point-to-point, broadcast, multicast, etc.)
  - synchronize tasks using barriers, semaphores, or message tags
  - handle errors and faults in the parallel virtual machine
- PVM supports heterogeneous computing, meaning that the computers in the parallel virtual machine can have different architectures, operating systems, and network protocols.
- PVM is portable and runs on most Unix-like systems, as well as Windows and Mac OS X.
- PVM is free and open source, and can be downloaded from http://www.csm.ornl.gov/pvm/pvm_home.html
- PVM has been used for a variety of applications, such as computational chemistry, bioinformatics, image processing, climate modeling, and distributed rendering.
- PVM can also be used to combine multiple Beowulf clusters into a grid of clusters, as shown in Figure 10.1.

![Figure 10.1: PVM used to create a Grid of clusters.](https://flylib.com/books/1/50/1/html/2/images/10fig01.gif)