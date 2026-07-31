# Solution to Byzantine Agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties to agree on a value even if some of the parties are corrupted or faulty.
- The problem was first defined by Lamport who also gave a solution under the situation of processor failure. The problem is also known as the interactive consistency problem or the Byzantine Generals problem.
- The Byzantine Generals problem is an analogy that illustrates the difficulty of achieving consensus in a distributed system. The scenario is as follows :

  - Several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger.
  - After observing the enemy, they must decide upon a common plan of action. However, some of the generals may be traitors and try to prevent the loyal generals from reaching agreement.
  - The generals must have an algorithm to guarantee that: (a) All loyal generals decide upon the same plan of action, and (b) A small number of traitors cannot cause the loyal generals to adopt a bad plan.

- A solution to the Byzantine agreement problem must satisfy the following properties:

  - **Validity**: If all parties start with the same value, then they must all decide on that value.
  - **Agreement**: All honest parties must decide on the same value.
  - **Termination**: All honest parties must eventually decide on a value.

- A simple solution to the Byzantine agreement problem is to use a majority voting scheme, where each party broadcasts its value to all other parties, and then decides on the value that is received by the majority of the parties. However, this solution only works if there are more than two-thirds of honest parties in the system, i.e., if the number of faulty parties is less than one-third of the total number of parties.
- A more general solution to the Byzantine agreement problem is to use a recursive algorithm that involves multiple rounds of message exchange, where each party sends and receives messages from a subset of other parties, and then decides on a value based on the received messages. This solution can tolerate any number of faulty parties, as long as they are less than half of the total number of parties.
- One example of such a recursive algorithm is the Byzantine Agreement protocol by Pease, Shostak, and Lamport , which works as follows:

  - The protocol assumes that there are n parties, and that each party has a unique identifier from 1 to n. The protocol also assumes that there is a source party, denoted by p1, that has an initial value v, and that all other parties have no initial value.
  - The protocol consists of m rounds, where m is the maximum number of faulty parties in the system. In each round, each party sends and receives messages from a subset of other parties, and then updates its value based on the received messages. The subset of parties that each party communicates with depends on the round number and the party's identifier.
  - In the first round, the source party p1 broadcasts its value v to all other parties. Each party that receives v from p1 sets its value to v, and each party that does not receive v from p1 sets its value to null.
  - In the second round, each party pi, where i > 1, sends its value to all parties with identifiers greater than i. Each party that receives a value from pi sets its value to that value, and each party that does not receive a value from pi sets its value to null.
  - In the third round, each party pi, where i > 2, sends its value to all parties with identifiers greater than i. Each party that receives a value from pi sets its value to that value, and each party that does not receive a value from pi sets its value to null.
  - And so on, until the m-th round, where each party pi, where i > m, sends its value to all parties with identifiers greater than i. Each party that receives a value from pi sets its value to that value, and each party that does not receive a value from pi sets its value to null.
  - After the m-th round, each party decides on its value as follows: If the party has a non-null value, then it decides on that value. If the party has a null value, then it