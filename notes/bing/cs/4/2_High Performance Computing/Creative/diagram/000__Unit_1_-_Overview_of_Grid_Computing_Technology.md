## Unit 1 - Overview of Grid Computing Technology

Grid computing is a distributed architecture that uses a group of computers to combine resources and work together to accomplish a joint task. These tasks are compute-intensive and difficult for a single machine to handle. Several machines on a network collaborate under a common protocol and work as a single virtual supercomputer to get complex tasks done.

Grid computing follows distributed computing architecture. Grid computing is application oriented. They work in a decentralized management system. They can use existing hardware. Can easily associate with other organization. Tasks and instructions can be performed in parallel speeding. They are capable of using CPUs extended power.

The following diagram illustrates the basic architecture of a grid computing system:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Application 1  |    |  Application 2  |    |  Application 3  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Middleware    |    |   Middleware    |    |   Middleware    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Operating     |    |   Operating     |    |   Operating     |
|   System 1      |    |   System 2      |    |   System 3      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hardware 1    |    |   Hardware 2    |    |   Hardware 3    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       +--------------------+--------------------+
                            |
                            |
                            v
                    +-----------------+
                    |                 |
                    |   Grid Server   |
                    |                 |
                    +-----------------+
```

The top layer consists of high-level applications, such as an application to perform predictive modeling. The second layer, also known as middleware, manages and allocates resources requested by applications. The third layer consists of operating systems that run on different hardware platforms. The fourth layer consists of hardware devices, such as CPUs, memory, disks, etc. The grid server is a central component that coordinates the communication and collaboration among the grid nodes.