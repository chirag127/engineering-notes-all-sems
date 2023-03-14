 Here is the content in markdown format for the topic ### Components for Clusters for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing:

### Components for Clusters

The major components of a cluster are:

1. Nodes: Individual computers that act as servers are referred to as nodes in a cluster. Nodes are regular computers that are connected through a network. They have their own CPUs, memory, and storage.
2. Network: Nodes in a cluster are connected through a high-speed network which allows them to communicate and coordinate with each other. The network enables the nodes to work together and function as a single system. Common network technologies for clusters include Gigabit Ethernet, InfiniBand, and Myrinet.
3. Software: Cluster software is required to manage, coordinate, and facilitate communication between the nodes in a cluster. The software includes an operating system, libraries, APIs, and tools for parallel programming, job scheduling, distributing work, communication, synchronization, etc. Examples of cluster software include open-source projects such as Linux, MPICH, Open MPI, etc.
4. Storage: Cluster computing systems require a common storage system that can be accessed by all the nodes in the cluster. The storage system typically consists of network-attached storage (NAS) or a storage area network (SAN). The high-speed cluster network connects the storage system to the nodes. The high bandwidth and low latency of the storage system allow fast access to data for parallel computing tasks.

Advantages: Scalability, cost-effectiveness, high performance.
Disadvantages: Complex to setup and manage, single points of failure in network and shared storage, programming challenges.
Applications: Scientific computing, web services, cloud computing, etc.

Mnemonics:
Nodes like computers
Network like roads
Software like traffic rules
Storage like warehouse