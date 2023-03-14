YARN stands for Yet Another Resource Negotiator. It is a resource management framework for distributed computing that separates the processing engine and the management function of MapReduce. YARN architecture consists of multiple components such as Resource Manager, Node Manager, Containers, and Application Master. These components work together to implement the YARN architecture.

The following diagram illustrates the basic architecture of YARN using ASCII characters:

#### YARN

```
+-----------------+        +-----------------+
|                 |        |                 |
|   Client Node   |        |   Resource      |
|                 |        |   Manager       |
|                 |        |                 |
+-----------------+        +-----------------+
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    +-----------------+
       |                        |    |                 |
       |                        |    |   Scheduler     |
       |                        |    |                 |
       |                        |    +-----------------+
       |                        |    |
       |                        |    +-----------------+
       |                        |    |                 |
       |                        |    |   Applications  |
       |                        |    |   Manager       |
       |                        |    |                 |
       |                        |    +-----------------+
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        +-----------------+
       |                        |                 |
       |                        |   Node Manager  |
       |                        |                 |
       |                        +-----------------+
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    +-----------------+
       |                        |    |                 |
       |                        |    |   Container     |
       |                        |    |                 |
       |                        |    +-----------------+
       |                        |    |
       |                        |    +-----------------+
       |                        |    |                 |
       |                        |    |   Application   |
       |                        |    |   Master        |
       |                        |    |                 |
       |                        |    +-----------------+
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        +-----------------+
       |                        |                 |
       |                        |   Node Manager  |
       |                        |                 |
       |                        +-----------------+
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    +-----------------+
       |                        |    |                 |
       |                        |    |   Container     |
       |                        |    |                 |
       |                        |    +-----------------+
       |                        |    |
       |                        |    +-----------------+
       |                        |    |                 |
       |                        |    |   Application   |
       |                        |    |   Master        |
       |                        |    |                 |
       |                        |    +-----------------+
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        +-----------------+
       |                        |                 |
       |                        |   Node Manager  |
       |                        |                 |
       |                        +-----------------+
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |
       |                        |    |