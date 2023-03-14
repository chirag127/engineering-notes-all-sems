### Grid Computing Model and Protocols

Grid computing is a distributed architecture of multiple computers connected by networks to accomplish a joint task. These tasks are compute-intensive and difficult for a single machine to handle. Several machines on a network collaborate under a common protocol and work as a single virtual supercomputer to get complex tasks done. 

Grid computing can be seen as a special type of parallel computing that relies on complete computers (with onboard CPUs, storage, power supplies, network interfaces, etc.) connected to a computer network (private or public) by a conventional network interface, such as Ethernet. This is in contrast to the traditional notion of a supercomputer, which has many processors connected by a local high-speed computer bus. 

Grid computing combines computers from multiple administrative domains to reach a common goal, to solve a single task, and may then disappear just as quickly. The size of a grid may vary from small—confined to a network of computer workstations within a corporation, for example—to large, public collaborations across many companies and networks. 

Grid computing is enabled via an open set of standards and protocols such as open grid services architecture (OGSA) that allow communication across heterogeneous systems and environments that are geographically dispersed. 

Grid computing operates by running specialized software on every computer involved in the grid network. The software coordinates and manages all the tasks of the grid. Fundamentally, the software segregates the main task into subtasks and assigns the subtasks to each computer. This allows all the computers to work simultaneously on their respective subtasks. Upon completion of the subtasks, the outputs of all computers are aggregated to complete the larger main task. The software allows computers to communicate and share information on the portion of the subtasks being carried out. As a result, the computers can consolidate and deliver a combined output for the assigned main task. 

A typical grid computing network consists of three machine types: 

- Control node/server: A control node is a server or a group of servers that administers the entire network and maintains the record for resources in a network pool.
- Provider/grid node: A provider or grid node is a computer that contributes its resources to the network resource pool.
- User: A user refers to the computer that uses the resources on the network to complete the task.

Grid computing has many applications in various domains such as scientific, mathematical, academic, commercial, and web services. Some examples of grid computing projects are SETI@home, Folding@home, World Community Grid, and LHC@home. 

Grid computing uses different types of protocols to enable communication and coordination among the grid nodes. Some of the protocols are:  

- TCP based protocols: These protocols use the transmission control protocol (TCP) as the underlying transport layer protocol. TCP provides reliable, ordered, and error-checked delivery of data. Some examples of TCP based protocols are GridFTP, GridRPC, and Globus Toolkit.
- UDP based protocols: These protocols use the user datagram protocol (UDP) as the underlying transport layer protocol. UDP provides fast, unreliable, and unordered delivery of data. Some examples of UDP based protocols are UDT, UFTP, and Fast Data Transfer (FDT).
- Application layer protocols: These protocols are implemented at the application layer of the network stack. They provide specific functionalities and services for grid computing applications. Some examples of application layer protocols are OGSA, OGSI, and WSRF.