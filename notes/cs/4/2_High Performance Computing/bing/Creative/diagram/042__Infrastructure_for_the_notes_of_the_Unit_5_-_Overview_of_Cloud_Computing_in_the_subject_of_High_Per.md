According to the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing, cloud computing is the delivery of computing resources over the internet, such as storage, processing power, databases, networking, analytics, artificial intelligence, and software applications. Cloud computing offers cost savings, scalability, high performance, economies of scale, and more.

Cloud infrastructure is the term used to describe the components needed for cloud computing, which includes hardware, abstracted resources, storage, and network resources. Cloud infrastructure is the tools needed to build a cloud. Cloud infrastructure can be categorized into three parts: computing, networking, and storage.

The following diagram illustrates the basic architecture of a cloud infrastructure using ASCII characters:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Computing     |    |   Networking    |    |   Storage       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Hypervisor     |    |  Load Balancer  |    |  File System    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Management     |    |  Firewall       |    |  Database       |
|  Software       |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Deployment     |    |  Router         |    |  Object Store   |
|  Software       |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Server         |    |  Switch         |    |  Disk           |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```