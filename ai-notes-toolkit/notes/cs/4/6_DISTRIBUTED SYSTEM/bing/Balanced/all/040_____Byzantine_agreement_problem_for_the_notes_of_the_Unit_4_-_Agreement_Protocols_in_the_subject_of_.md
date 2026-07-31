# Byzantine Agreement Problem

The Byzantine agreement problem is a fundamental problem in fault-tolerant distributed computing. It requires a set of parties in a distributed system to agree on a value even if some of the parties are corrupted or faulty. The corrupted parties may behave arbitrarily, sending conflicting or misleading messages to different parties, or remaining silent. The problem is also known as the Byzantine generals problem, the interactive consistency problem, or the source congruency problem.

The problem was first defined and solved by Lamport et al. in 1982, using the analogy of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The problem is to find an algorithm that allows the loyal generals to agree on a common plan, while tolerating a certain number of traitors.

Some of the main concepts and results related to the Byzantine agreement problem are:

- A Byzantine agreement protocol is a distributed algorithm that allows the parties to reach agreement on a value, despite the presence of Byzantine faults. A Byzantine fault is any deviation from the normal behavior of a party, such as sending incorrect or inconsistent messages, crashing, or colluding with other faulty parties.
- A Byzantine agreement protocol is said to be correct if it satisfies the following properties:
  - **Validity**: If all the parties start with the same value, then they all decide on that value.
  - **Agreement**: All the parties decide on the same value.
  - **Termination**: All the parties eventually decide on a value.
- A Byzantine agreement protocol is said to be t-resilient if it can tolerate up to t faulty parties, and it is correct for any number of parties n > t.
- A Byzantine agreement protocol is said to be deterministic if the decision of each party depends only on its initial value and the messages it receives, and it is randomized if the decision of each party may also depend on some random choices.
- A Byzantine agreement protocol is said to be synchronous if there is a known upper bound on the message delivery time, and it is asynchronous if there is no such bound. A synchronous protocol can also use rounds, where each party sends and receives messages only at certain predefined times.
- A Byzantine agreement protocol is said to be oral if it uses only point-to-point messages, and it is signed if it uses digital signatures or other cryptographic techniques to authenticate the messages.
- A Byzantine agreement protocol is said to be binary if the parties can only decide on two possible values, such as 0 or 1, and it is multivalued if the parties can decide on any value from a given domain.
- A Byzantine agreement protocol is said to be uniform if the decision of each party does not depend on its initial value, and it is non-uniform otherwise.
- A Byzantine agreement protocol is said to be interactive if the parties exchange messages with each other, and it is non-interactive if the parties only receive messages from a common source.

Some of the main challenges and limitations of the Byzantine agreement problem are:

- It is impossible to achieve Byzantine agreement in an asynchronous system with one or more faulty parties, as shown by Fischer et al. in 1985. This is known as the FLP impossibility result, and it implies that any asynchronous Byzantine agreement protocol must either sacrifice termination or agreement in some cases.
- It is impossible to achieve deterministic Byzantine agreement in a synchronous system with more than one-third of the parties being faulty, as shown by Lamport et al. in 1982. This is known as the lower bound on the resilience of deterministic Byzantine agreement, and it implies that any deterministic Byzantine agreement protocol must have n > 3t.
- It is possible to achieve randomized Byzantine agreement in a synchronous system with less than half of the parties being faulty, as shown by Rabin in 1983. This is known as the upper bound on the resilience of randomized Byzantine agreement, and it implies that any randomized Byzantine agreement protocol can have n > 2t.
- It is possible to achieve oral Byzantine agreement in a synchronous system with less than one-third of the parties being faulty, as shown by Lamport et al. in 1982. This is known as the upper bound on the resilience of oral Byzantine agreement, and it implies that any oral Byzantine