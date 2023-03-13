YARN is the acronym for Yet Another Resource Negotiator. It is a resource management framework for Hadoop that separates the processing engine and the management function of MapReduce. YARN consists of multiple components such as Resource Manager, Node Manager, Containers, and Application Master. These components work together to allocate and execute applications on the cluster.

#### YARN

The following diagram illustrates the basic architecture of YARN using ASCII characters.

```
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|   Client Node    |       |   Resource       |       |   Node Manager   |
|                  |       |   Manager (RM)   |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Submit/monitor  |       |  Cluster         |       |  Manage          |
|  applications    |       |  resource        |       |  containers      |
|                  |       |  allocation      |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+

       |                  |       |                  |       |                  |
       |                  |       |                  |       |                  |
       |                  |       |                  |       |                  |
       |                  |       |                  |       |                  |
       |                  |       |                  |       |                  |
       |                  |       |                  |       |                  |
       |                  |       |                  |       |                  |
       |                  |       |                  |       |                  |
       |                  |       |                  |