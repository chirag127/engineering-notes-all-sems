### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P<sub>i</sub>, and the message is being sent by the home site of process P<sub>j</sub> to the home site of process P<sub>k</sub>.
- The home site of a process is the site where the process is executing, and it is responsible for sending and receiving probes on behalf of the process.
- The algorithm works as follows:
  - A process P<sub>i</sub> that is waiting for a resource initiates the deadlock detection by sending a probe (i, i, k) to the home site of the process P<sub>k</sub> that holds the resource.
  - The home site of P<sub>k</sub> checks if P<sub>k</sub> is waiting for another resource. If yes, it forwards the probe (i, k, l) to the home site of the process P<sub>l</sub> that holds the resource. If no, it discards the probe.
  - This process continues until either a probe reaches a process that is not waiting for any resource, or a probe returns to the initiator process P<sub>i</sub>.
  - If a probe returns to P<sub>i</sub>, it means that there is a cycle in the dependency graph, and hence a deadlock. P<sub>i</sub> can then initiate a recovery action, such as aborting one of the processes in the cycle.
  - If a probe reaches a process that is not waiting for any resource, it means that there is no cycle in the dependency graph, and hence no deadlock. The probe is then discarded.

- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable. They do not require any global information or coordination among the sites, and they only use a small number of messages.
- The disadvantages of edge chasing algorithms are that they may generate false positives, meaning that they may detect a deadlock that does not exist. This can happen if the dependency graph changes during the execution of the algorithm, or if there are multiple initiators of the deadlock detection. They may also generate false negatives, meaning that they may miss a deadlock that exists. This can happen if the probes are lost or delayed due to network failures or congestion.