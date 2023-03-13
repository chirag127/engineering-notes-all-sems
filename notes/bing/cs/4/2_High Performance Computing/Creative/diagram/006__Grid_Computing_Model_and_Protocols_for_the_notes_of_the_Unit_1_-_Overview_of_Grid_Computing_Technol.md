Grid computing is a distributed architecture of multiple computers connected by networks to accomplish a joint task. These tasks are compute-intensive and difficult for a single machine to handle. Several machines on a network collaborate under a common protocol and work as a single virtual supercomputer to get complex tasks done.

Grid computing is enabled via an open set of standards and protocols such as open grid services architecture (OGSA) that allow communication across heterogeneous systems and environments that are geographically dispersed. Grid protocols play a major role in implementing services that facilitate global grid computing. They can be classified into core protocols and application protocols. Core protocols are those that are essential for the basic functioning of the grid, such as resource discovery, resource allocation, security, monitoring, and fault tolerance. Application protocols are those that are specific to the domain or application of the grid, such as data management, workflow management, and scientific computing.

The following diagram illustrates the basic architecture of a grid computing system using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Application    |    |  Application    |    |  Application    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Middleware     |    |  Middleware     |    |  Middleware     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Operating      |    |  Operating      |    |  Operating      |
|  System         |    |  System         |    |  System         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Hardware       |    |  Hardware       |    |  Hardware       |
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
                  |  Grid Protocol  |
                  |                 |
                  +-----------------+
                            |
                            |
                            v
                  +-----------------+
                  |                 |
                  |  Grid Services  |
                  |                 |
                  +-----------------+
                            |
                            |
                            v
                  +-----------------+
                  |                 |
                  |  Grid Resources |
                  |                 |
                  +-----------------+
```