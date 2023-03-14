## Unit 1 - Overview of Grid Computing Technology

Grid computing is a distributed architecture that uses a group of computers to combine resources and work together to accomplish a joint task. These tasks are compute-intensive and difficult for a single machine to handle. Several machines on a network collaborate under a common protocol and work as a single virtual supercomputer to get complex tasks done.

A typical grid computing network consists of three machine types: control node/server, provider/grid node, and user. The control node is a server or a group of servers that administers the entire network and maintains the record for resources in a network pool. The provider or grid node is a computer that contributes its resources to the network resource pool. The user is the computer that uses the resources on the network to complete the task.

Grid computing operates by running specialized software on every computer involved in the grid network. The software coordinates and manages all the tasks of the grid. Fundamentally, the software segregates the main task into subtasks and assigns the subtasks to each computer. This allows all the computers to work simultaneously on their respective subtasks. Upon completion of the subtasks, the outputs of all computers are aggregated to complete the larger main task. The software allows computers to communicate and share information on the portion of the subtasks being carried out. As a result, the computers can consolidate and deliver a combined output for the assigned main task.

The following diagram illustrates the basic architecture of a grid computing network using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Control Node  |     |   Grid Node 1   |     |   Grid Node 2   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
        |                      |                       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|      User       |     |   Grid Node 3   |     |   Grid Node 4   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```