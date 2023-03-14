### Edge Chasing Algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to detect cycles in the wait-for graph (WFG) of processes and resources.
- A probe is a triplet (i, j, k) that denotes that process P_i has initiated the deadlock detection and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message circulates along the edges of the WFG to detect a cycle. When a blocked process receives the probe message, it forwards the probe message along its outgoing edges in the WFG. A process P_i declares a deadlock if a probe message initiated by P_i returns to itself.
- Edge chasing algorithms can be divided into four categories based on how the probes are initiated and propagated:

  - Path push-in: Path information is sent from the waiting node to the blocking node.
  - Edge-chasing: Probe messages are sent along the graph edges.
  - Diffusion computation: Echo messages are sent along the graph edges.
  - Global state detection: Sweep-out, sweep-in WFG creation and reduction.

- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm, which is based on the AND request model, where a process can request multiple resources simultaneously and block until it acquires all of them.
- The Chandy-Misra-Haas algorithm uses the following terminologies and data structures:

  - Dependent process: A process P_i is said to be dependent on some other process P_j, if there exists a sequence of processes P_i, P_i1, P_i2, P_i3, ..., P_im, P_j such that in the sequence, each process except P_j is blocked and each process except P_i holds a resource for which the previous process in the sequence is waiting.
  - Locally dependent process: A process P_i is said to be locally dependent on some other process P_j if P_i is dependent on P_j and both are at the same site.
  - A boolean array, dependent_i. Initially, dependent_i[j] is false for all values of i and j. dependent_i[j] is true if process P_j is dependent on process P_i.

- The Chandy-Misra-Haas algorithm works as follows:

  - The algorithm is initiated whenever a process P_i is forced to wait for a resource held by another process P_j. The algorithm can be initiated either by the local site of P_i or by the site where P_i waits.
  - The process of sending a probe is as follows:

    - If P_i is locally dependent on itself, then declare a deadlock.
    - Else, for all P_j and P_k, check the following conditions:

      - P_i is locally dependent on P_j.
      - P_j is waiting on P_k.
      - P_j and P_k are on different sites.

    - If all of the above conditions are true, send a probe (i, j, k) to the home site of P_k.

  - On the receipt of a probe (i, j, k) at the home site of P_k:

    - P_k checks the following conditions:

      - P_k is blocked.
      - dependent_k[i] is false.
      - P_k has not replied to all requests of P_j.

    - If all of the above conditions are true, then:

      - Set dependent_k[i] to true.
      - If k == i, then declare that P_i is deadlocked.
      - Else, for all P_m and P_n, check the following conditions:

        - P_k is locally dependent on P_m.
        - P_m is waiting on P_n.
        - P_m and P_n are on different sites.

      - Send a probe (i, m, n) to the home site of P_n if the above conditions are satisfied.

- The performance of the Chandy-Misra-Haas algorithm is as follows:

  - The algorithm requires at most m(n-1)/2 messages to detect a deadlock, where m is the number of processes and n is the number of sites.
  - The delay in detecting a deadlock is O(n).

- A possible mnemonic to remember the steps of the Chandy-Misra-Haas algorithm is:

  - **C**heck if locally dependent on self, then declare deadlock.
  - **H**unt for locally dependent processes waiting on different