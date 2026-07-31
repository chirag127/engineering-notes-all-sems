### File directories for the notes of the Unit 5 - I/O Management and Disk Scheduling in the subject of Operating system

- A file directory is a data structure that stores information about the files in a file system, such as their names, sizes, attributes, and locations on the disk.
- A file directory can have different levels of organization, such as a single-level directory, a two-level directory, a tree-structured directory, or an acyclic-graph directory.
- A single-level directory is the simplest form of a file directory, where all the files are stored in the same directory. This makes it easy to locate and access files, but it can cause problems with naming conflicts, security, and scalability.
- A two-level directory is a file directory that has one level for the user and another level for the files. Each user has a separate directory that contains only their own files. This solves the naming conflict problem, but it can still have issues with security and scalability.
- A tree-structured directory is a file directory that has a hierarchical structure, where each directory can contain subdirectories and files. This allows for more flexibility and organization, but it can also increase the complexity and overhead of searching and navigating the directory.
- An acyclic-graph directory is a file directory that allows for sharing of files and directories among users. A file or a directory can have multiple names and multiple parents, forming a graph structure. This can save disk space and improve efficiency, but it can also introduce problems with cycles, aliases, and consistency.

- I/O management is the process of controlling and coordinating the input and output devices and operations in a computer system. It involves the following components and functions:
  - I/O devices: These are the hardware components that perform input and output operations, such as keyboards, mice, monitors, printers, disks, etc.
  - I/O controllers: These are the hardware components that interface between the I/O devices and the system bus, such as device drivers, adapters, ports, etc.
  - I/O buffers: These are the memory areas that temporarily store data during I/O operations, such as caches, spoolers, queues, etc.
  - I/O modules: These are the software components that manage the I/O devices, controllers, and buffers, such as device handlers, interrupt handlers, I/O schedulers, etc.
  - I/O system calls: These are the interface between the user programs and the I/O modules, such as open, read, write, close, etc.

- Disk scheduling is the process of deciding the order and manner of servicing the requests for disk I/O operations. It aims to optimize the performance, efficiency, and fairness of the disk system. It involves the following factors and algorithms:
  - Seek time: This is the time required for the disk head to move to the desired track on the disk.
  - Rotational latency: This is the time required for the desired sector to rotate under the disk head.
  - Transfer time: This is the time required to transfer the data between the disk and the memory.
  - Disk bandwidth: This is the total amount of data transferred per unit time.
  - Disk utilization: This is the percentage of time the disk is busy servicing requests.
  - Disk response time: This is the average time required to complete a disk request.
  - Disk throughput: This is the average number of requests serviced per unit time.
  - Disk fairness: This is the degree of satisfaction of the different users or processes that share the disk.
  - FCFS (First Come First Served): This is the simplest disk scheduling algorithm, where the requests are serviced in the order they arrive. It is fair, but it can have poor performance and high response time.
  - SSTF (Shortest Seek Time First): This is the disk scheduling algorithm, where the requests are serviced in the order of increasing seek time. It can improve the performance and reduce the seek time, but it can also cause starvation and unfairness for some requests.
  - SCAN (Elevator): This is the disk scheduling algorithm, where the disk head moves in one direction and services the requests along the way, until it reaches the end of the disk, then it reverses the direction and repeats the process. It can improve the performance and fairness, but it can also cause long waiting time for some requests.
  - C-SCAN (Circular SCAN): This is the disk scheduling algorithm, where the disk head moves in one direction and services the requests along the way, until it reaches the end of the disk, then it jumps to the other end of the disk and repeats the process. It can improve the performance and fairness, but it can also cause long waiting time for some requests.
  - LOOK: This is the disk scheduling algorithm, where the disk head