A distributed system is a collection of autonomous computers that communicate and coordinate their actions through message passing. A distributed system has some benefits such as scalability, reliability, and performance, but it also faces some challenges and limitations. One of the main limitations of a distributed system is the absence of a global state and a global clock. This means that there is no single source of truth or time for the whole system, and each component has only a partial and local view of the system. This makes it difficult to design and implement algorithms that require global knowledge or synchronization, such as consensus, deadlock detection, or mutual exclusion.

The following diagram illustrates the basic architecture of a distributed system and its limitations:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Component A    |    |  Component B    |    |  Component C    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Local State    |    |  Local State    |    |  Local State    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Local Clock    |    |  Local Clock    |    |  Local Clock    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       +--------------------+--------------------+
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    |                    |
                    +--------------------+
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Component D    |    |  Component E    |    |  Component F    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Local State    |    |  Local State    |    |  Local State    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Local Clock    |    |  Local Clock    |    |  Local Clock    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

In this diagram, each component has its own local state and clock, which may differ from the others. The components communicate with each other through message passing, which may introduce delays, errors, or losses. There is no global state or clock that can be accessed by all components, and no guarantee that the messages are delivered in the same order or at the same time. Therefore, the components have to deal with the uncertainty and inconsistency of the distributed system.