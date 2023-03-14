Grid computing is a distributed architecture of multiple computers connected by networks to accomplish a joint task. These tasks are compute-intensive and difficult for a single machine to handle. Several machines on a network collaborate under a common protocol and work as a single virtual supercomputer to get complex tasks done.

Grid computing is enabled via an open set of standards and protocols such as open grid services architecture (OGSA) that allow communication across heterogeneous systems and environments that are geographically dispersed.

A typical grid computing network consists of three machine types:

- Control node/server: A control node is a server or a group of servers that administers the entire network and maintains the record for resources in a network pool.
- Provider/grid node: A provider or grid node is a computer that contributes its resources to the network resource pool.
- User: A user refers to the computer that uses the resources on the network to complete the task.

Grid computing operates by running specialized software on every computer involved in the grid network. The software coordinates and manages all the tasks of the grid. Fundamentally, the software segregates the main task into subtasks and assigns the subtasks to each computer. This allows all the computers to work simultaneously on their respective subtasks. Upon completion of the subtasks, the outputs of all computers are aggregated to complete the larger main task. The software allows computers to communicate and share information on the portion of the subtasks being carried out. As a result, the computers can consolidate and deliver a combined output for the assigned main task.

Grid computing can be viewed as a subset of distributed computing, where a virtual supercomputer integrates the resources of several independent computers that are distributed across geographies. Computers participating in a grid contribute resources such as processing power, network bandwidth, and storage capacity to perform operations requiring high computational power. The overall grid architecture looks like a single computing entity.

Grid computing has various types and applications, such as:

- Computational grid: A grid that focuses on providing high-performance computing power for compute-intensive applications, such as scientific simulations, weather modeling, etc.
- Data grid: A grid that focuses on providing high-capacity data storage and access for data-intensive applications, such as data mining, data analysis, etc.
- Service grid: A grid that focuses on providing various services, such as web services, database services, etc., to users and applications.
- Desktop grid: A grid that utilizes the idle resources of desktop computers, such as CPU cycles, disk space, etc., to perform tasks, such as volunteer computing, distributed rendering, etc.
- Cloud computing: A grid that provides on-demand access to scalable and elastic resources, such as servers, storage, networks, etc., over the internet, for various applications, such as web hosting, e-commerce, etc.

Some examples of grid computing projects are:

- SETI@home: A project that uses the idle resources of volunteer computers to analyze radio signals from space for signs of extraterrestrial intelligence.
- Folding@home: A project that uses the idle resources of volunteer computers to simulate protein folding and study diseases such as Alzheimer's, Parkinson's, etc.
- World Community Grid: A project that uses the idle resources of volunteer computers to support various humanitarian and scientific research projects, such as cancer, AIDS, clean energy, etc.
- LHC@home: A project that uses the idle resources of volunteer computers to simulate particle collisions at the Large Hadron Collider, the world's largest and most powerful particle accelerator.
- Google File System: A distributed file system that provides high-performance and fault-tolerant data storage and access for Google's applications, such as web search, Gmail, YouTube, etc.

The following diagram illustrates the basic architecture of a grid computing network using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
| Control node    |     | Provider node   |     | User node       |
| (server)        |     | (grid node)     |     | (client)        |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Grid        | |     | | Grid        | |     | | Grid        | |
| | middleware  | |     | | middleware  | |     | | middleware  | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Application | |     | | Application | |