One of the algorithms for distributed deadlock detection is the **Chandy-Misra-Haas** algorithm, which is an **edge-chasing** algorithm. In this algorithm, a special message called **probe** is used to detect deadlock in distributed systems. A probe is a triplet (i, j, k) which denotes that process P_i has initiated the deadlock detection and the message is sent from process P_j to process P_k. A process sends a probe to all its dependent processes and waits for a reply. If a process receives a probe from itself, it detects a deadlock and initiates a recovery procedure. Otherwise, it forwards the probe to its dependent processes and sends a reply to the sender.

The following diagram illustrates the basic architecture of a distributed deadlock detection system using the Chandy-Misra-Haas algorithm:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Process P1   |     |    Process P2   |     |    Process P3   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
      |  ^                    |  ^                    |  ^
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      v  |                    v  |                    v  |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Process P4   |     |    Process P5   |     |    Process P6   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
      |  ^                    |  ^                    |  ^
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      |  |                    |  |                    |  |
      v  |                    v  |                    v  |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Process P7   |     |    Process P8   |     |    Process P9   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+

```

The arrows indicate the direction of the probe messages. For example, P1 sends a probe (1, 1, 4) to P4, and P4 sends a probe (1, 4, 7) to P7. If P7 sends a probe (1, 7, 1) to P1, then P1 detects a deadlock involving P1, P4, and P7.