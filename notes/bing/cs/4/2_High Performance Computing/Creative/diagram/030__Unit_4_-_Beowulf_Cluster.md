## Unit 4 - Beowulf Cluster

A Beowulf cluster is a computer cluster of what are normally identical, commodity-grade computers networked into a small local area network with libraries and programs installed which allow processing to be shared among them. The result is a high-performance parallel computing cluster from inexpensive personal computer hardware.

A Beowulf cluster is scalable to a nearly unlimited number of computers, limited only by the overhead of the network. Provisioning of operating systems and other software for a Beowulf Cluster can be automated using software, such as Open Source Cluster Application Resources.

The following diagram illustrates the basic architecture of a Beowulf cluster using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Master Node   |     |   Compute Node  |     |   Compute Node  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Linux OS       |     |  Linux OS       |     |  Linux OS       |
|  Cluster        |     |  Cluster        |     |  Cluster        |
|  Software       |     |  Software       |     |  Software       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  CPU            |     |  CPU            |     |  CPU            |
|  Memory         |     |  Memory         |     |  Memory         |
|  Disk           |     |  Disk           |     |  Disk           |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Network        |     |  Network        |     |  Network        |
|  Interface      |     |  Interface      |     |  Interface      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                    |                    |
       |                    |                    |
       +--------------------+--------------------+
                            |
                            |
                      +-----+-----+
                      |           |
                      |   Switch  |
                      |           |
                      +-----+-----+
                            |
                            |
                      +-----+-----+
                      |           |
                      |   Router  |
                      |           |
                      +-----+-----+
                            |
                            |
                      +-----+-----+
                      |           |
                      | Internet  |
                      |           |
                      +-----------+
```

The master node is the central controller of the cluster. It manages the scheduling and distribution of tasks to the compute nodes, as well as the communication and data transfer between them. The master node also provides access to the cluster from the outside world, such as the internet .

The compute nodes are the workers of the cluster. They execute the tasks assigned by the master node, using their own CPU, memory, disk and network resources. The compute nodes do not need to have any user interface or display, as they are controlled by the master node .

The switch is a device that connects the master node and the compute nodes in a local area network. It allows fast and reliable data transfer between them, using protocols such as Ethernet .

The router is a device that connects the local area network to the internet. It allows the master node to communicate with external users or services, such as web servers, databases, or cloud platforms .

The internet is the global network of networks that provides access to various online resources and applications. It can be used by the master node to obtain input data, store output data, or run distributed or hybrid computations .