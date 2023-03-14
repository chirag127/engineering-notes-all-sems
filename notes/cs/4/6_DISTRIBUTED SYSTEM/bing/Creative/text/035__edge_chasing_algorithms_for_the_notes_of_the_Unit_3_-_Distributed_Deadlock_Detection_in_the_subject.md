### Edge Chasing Algorithms

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to detect cycles in the wait-for graph (WFG) of processes and resources.
- A probe is a triplet (i, j, k) that denotes that process P_i has initiated the deadlock detection and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message circulates along the edges of the WFG to detect a cycle. When a blocked process receives the probe message, it forwards the probe message along its outgoing edges in the WFG.
- A process P_i declares a deadlock if a probe message initiated by P_i returns to itself.
- Edge chasing algorithms can be divided into four categories based on how the probes are initiated and propagated:

  - Path push-in: Path information is sent from the waiting node to the blocking node.
  - Edge-chasing: Probe messages are sent along the graph edges.
  - Diffusion computation: Echo messages are sent along the graph edges.
  - Global state detection: Sweep-out, sweep-in WFG creation and reduction.

- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm, which is based on the AND request model and uses the following data structures and terminologies:

  - Dependent process: A process P_i is said to be dependent on some other process P_j, if there exists a sequence of processes P_i, P_i1, P_i2, ..., P_im, P_j such that in the sequence, each process except P_j is blocked and each process except P_i holds a resource for which the previous process in the sequence is waiting.
  - Locally dependent process: A process P_i is said to be locally dependent on some other process P_j if P_i is dependent on P_j and both are at the same site.
  - A boolean array, dependent_i. Initially, dependent_i[j] is false for all values of i and j. dependent_i[j] is true if process P_j is dependent on process P_i.

- The algorithm works as follows:

  - Process of sending probe:

    - If process P_i is locally dependent on itself, then declare a deadlock.
    - Else, for all P_j and P_k, check the following conditions:

      - Process P_i is locally dependent on process P_j.
      - Process P_j is waiting on process P_k.
      - Process P_j and P_k are on different sites.

    - If all of the above conditions are true, send probe (i, j, k) to the home site of process P_k.

  - On the receipt of probe (i, j, k) at the home site of process P_k:

    - Process P_k checks the following conditions:

      - Process P_k is blocked.
      - dependent_k[i] is false.
      - Process P_k has not replied to all requests of process P_j.

    - If all of the above conditions are true, then:

      - Set dependent_k[i] to true.
      - If k == i, then declare that P_i is deadlocked.
      - Else, for all P_m and P_n, check the following conditions:

        - Process P_k is locally dependent on process P_m.
        - Process P_m is waiting on process P_n.
        - Process P_m and P_n are on different sites.

      - Send probe (i, m, n) to the home site of process P_n if the above conditions are satisfied.

- The performance of the algorithm is as follows:

  - The algorithm requires at most m(n-1)/2 messages to detect a deadlock, where m is the number of processes and n is the number of sites.
  - The delay in detecting the deadlock is O(n).