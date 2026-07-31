### Interactive Consistency Problem

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending conflicting or incorrect messages, or remaining silent .
- Interactive consistency is a generalization of the consensus problem, where the goal is to reach agreement on a single value among all non-faulty nodes.
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems.
- Interactive consistency is also known as the Byzantine Generals Problem, which is a metaphor for the situation where a group of generals must coordinate an attack or retreat, but some of them may be traitors who try to sabotage the plan .
- Interactive consistency is a hard problem to solve, especially in asynchronous or partially synchronous systems, where there is no global clock or bounded message delays .
- Interactive consistency requires at least 3t + 1 nodes to be solvable, where t is the maximum number of Byzantine nodes .
- Interactive consistency can be solved using various algorithms, such as broadcast, consensus, or secret sharing algorithms  .
- Interactive consistency algorithms must satisfy the following properties :
  - Validity: If a node is non-faulty, then its value is inferred correctly by all non-faulty nodes.
  - Agreement: All non-faulty nodes infer the same value for each node.
  - Termination: All non-faulty nodes eventually infer the values of all nodes.