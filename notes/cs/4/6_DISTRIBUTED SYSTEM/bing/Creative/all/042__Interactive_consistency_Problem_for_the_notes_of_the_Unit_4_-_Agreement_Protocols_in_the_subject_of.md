### Interactive consistency problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency (IC) is the problem in which n nodes, where up to t may be Byzantine (faulty), each with its own private value, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- This problem is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as distributed e-voting, monitoring a content source, or resolving divergent state among the nodes of a distributed system .
- IC is also known as the generals problem, as it can be seen as a generalization of the Byzantine generals problem, where the nodes have to agree on a single value instead of a vector of values .
- IC is impossible to achieve in a fully asynchronous system, as it is impossible to guarantee simultaneously that all honest parties inputs’ are included in the computation (in our case, in the resulting vector of values), and that all honest parties are guaranteed to terminate, as proved in [43] of . This is the reason vector consensus is considered the only achievable equivalent of IC for completely asynchronous systems [25] of .
- IC can be achieved in a synchronous system, where one can make strong assumptions such as negligible message delivery delays and/or detection of absent messages. However, these assumptions are ill-suited for practical, real-world distributed systems which, in their vast majority are mostly asynchronous, i.e., they exhibit only some periods of synchrony during which message delivery is timely .
- To achieve IC in practical, mostly-asynchronous systems, one can leverage prior work on broadcast and randomized Byzantine consensus algorithms, and design algorithms with varying timing assumptions and message complexity .
- One possible algorithm for IC in practical, mostly-asynchronous systems is the following:

  - Each node broadcasts its private value to all other nodes using a reliable broadcast protocol, such as Bracha's broadcast [7] of .
  - Each node collects the values received from the broadcast protocol, and forms a vector of values, where the i-th slot contains the value received from node i, or a special symbol ⊥ if no value was received from node i.
  - Each node runs a multi-valued Byzantine consensus protocol, such as King's consensus [41] of , on the vector of values, and outputs the agreed vector as the final result.

- The algorithm above has the following properties:

  - It requires a single synchronization barrier, which is the broadcast protocol.
  - It tolerates up to t < n/3 Byzantine nodes, where n is the total number of nodes.
  - It has a message complexity of O(n^2) for the broadcast protocol, and O(n^4) for the consensus protocol.
  - It guarantees that all non-faulty nodes output the same vector of values, and that for each non-faulty node, the corresponding slot in the vector contains that node’s private value.

- A possible mnemonic to remember the algorithm above is:

  - **B**roadcast your value
  - **C**ollect the values in a vector
  - **C**onsensus on the vector

- A possible ascii diagram to illustrate the algorithm above is:

```
  Node 1 (private value = 1)    Node 2 (private value = 2)    Node 3 (private value = 3)    Node 4 (private value = 4)
  
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            | 
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            |
  |                            |                            |                            | 
  |                            |                            |                            |
  |                            |                            |                            |
  |