Termination detection is a fundamental problem in distributed systems, where the goal is to determine if a distributed computation has terminated. A distributed computation is terminated if every process is idle and there is no message in transit between any processes. There are different algorithms for termination detection, such as Huang's algorithm, Dijkstra-Scholten algorithm, and the snapshot-based algorithm. Here, I will draw a detailed ASCII diagram for the snapshot-based algorithm, which is based on the following idea:

- When a process goes from active to idle, it issues a request to all other processes to take a local snapshot, and also requests itself to take a local snapshot.
- When a process receives the request, if it agrees that the requester became idle before itself, it grants the request by taking a local snapshot for the request.
- A request is successful if all processes have taken a local snapshot for it. The requester or any external agent may collect all the local snapshots of a request.

The following diagram illustrates the basic architecture of a snapshot-based termination detection algorithm:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| Process P1      |       | Process P2      |       | Process P3      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| State: Active   |       | State: Active   |       | State: Idle     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| Request: None   |       | Request: None   |       | Request: None   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| Snapshot: None  |       | Snapshot: None  |       | Snapshot: None  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| Messages:       |       | Messages:       |       | Messages:       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |