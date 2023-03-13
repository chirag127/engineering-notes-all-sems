### Edge Chasing Algorithms for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the edges of the wait-for graph .
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k .
- The algorithm works as follows :
  - A process P_i that is waiting for a resource held by another process P_j initiates the deadlock detection by sending a probe (i, i, j) to the home site of P_j.
  - When the home site of P_j receives the probe, it checks if P_j is waiting for another process P_k. If yes, it forwards the probe (i, j, k) to the home site of P_k. If no, it discards the probe.
  - This process continues until either the probe reaches a process that is not waiting for any other process, or the probe returns to the initiator process P_i. In the latter case, a deadlock is detected and reported to all the processes involved in the cycle.
- The advantages of edge chasing algorithms are:
  - They are simple and easy to implement.
  - They do not require global knowledge of the system or a central coordinator.
  - They can detect deadlocks in a distributed manner without blocking the normal execution of the processes.
- The disadvantages of edge chasing algorithms are:
  - They may generate a large number of probe messages that consume network bandwidth and increase the detection latency.
  - They may fail to detect some deadlocks if the wait-for graph changes dynamically during the detection process.
  - They may report false deadlocks if there are multiple initiators or duplicate probes in the system.
- An example of edge chasing algorithm is the Chandy-Misra-Haas algorithm for the AND request model, which is based on the following rules :
  - A process P_i sends a probe (i, i, j) to the home site of P_j only if it is blocked on all the resources it has requested and P_j holds one of them.
  - A process P_i sends a probe (i, j, k) to the home site of P_k only if it has received a probe (i, l, j) from the home site of P_l and P_k holds a resource that P_j has requested.
  - A process P_i reports a deadlock when it receives a probe (i, j, i) from the home site of P_j.
- A possible mnemonic to remember the edge chasing algorithm is: **P**robe **E**very **D**eadlocked **G**raph **E**dge.
- A possible learning trick to understand the edge chasing algorithm is to draw the wait-for graph and label the probes with their triplets, then follow the path of the probes until they either reach a non-waiting process or return to the initiator process .
- A possible ascii diagram to illustrate the edge chasing algorithm is:

```
    P1  P2  P3  P4
S1  *   *   -   -
S2  -   *   *   -
S3  -   -   *   *
S4  *   -   -   *

P1 -> P2 -> P3 -> P4 -> P1 (deadlock cycle)

P1 sends (1, 1, 2) to P2
P2 sends (1, 2, 3) to P3
P3 sends (1, 3, 4) to P4
P4 sends (1, 4, 1) to P1
P1 detects deadlock and reports to P2, P3, P4
```