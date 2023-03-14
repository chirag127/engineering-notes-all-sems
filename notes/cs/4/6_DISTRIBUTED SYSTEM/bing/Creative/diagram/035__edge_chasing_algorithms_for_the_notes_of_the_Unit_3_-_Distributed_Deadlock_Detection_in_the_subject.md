The edge chasing algorithm is a distributed deadlock detection algorithm that uses a special message called probe to detect cycles in the wait-for graph. A probe is a triplet (i, j, k) which denotes that process P i has initiated the deadlock detection and the message is being sent by the home site of process P j to the home site of process P k . The probe message circulates along the edges of the wait-for graph to detect a cycle. When a blocked process receives the probe message, it forwards the probe message along its outgoing edges in the wait-for graph. A process P i declares the deadlock if probe messages initiated by process P i returns to itself.

The following diagram illustrates the basic architecture of the edge chasing algorithm using ASCII characters:

```
+-----+    probe(i,j,k)    +-----+    probe(i,k,l)    +-----+
| P i | -----------------> | P j | -----------------> | P k |
+-----+                    +-----+                    +-----+
  ^                         ^                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          v
  |                         |                        +-----+
  |                         |                        | P l |
  |                         |                        +-----+
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          |
  |                         |                          v
  |                         |                        +-----+
  |                         +----------------------> | P m |
  |                                                  +-----+
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    |
  |                                                    v
  +--------------------------------------------------+-----+
                                                   | P n |
                                                   +-----+
```

In this diagram, process P i initiates the deadlock detection and sends a probe message (i, i, j) to the home site of process P j . Process P j is blocked and waiting for process P k , so it forwards the probe message (i, j, k) to the home site of process P k . Process P k is blocked and waiting for process P l , so it forwards the probe message (i, k, l) to the home site of process P l . Process P l is blocked and waiting for process P m , so it forwards the probe message (i, l, m) to the home site of process P m . Process P m is blocked and waiting for process P n , so it forwards the probe message (i, m, n) to the home site of process P n . Process P n is blocked and waiting for process P i , so it forwards the probe message (i, n, i) to the home site of process P i . Process P i receives the probe message initiated by itself and declares the deadlock.