### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing, where a set of parties in a distributed environment need to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport  and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- A solution to the Byzantine agreement problem requires that the following conditions are met:
  - **Agreement**: All honest parties agree on the same value.
  - **Validity**: If all honest parties propose the same value, then they must agree on that value.
  - **Termination**: All honest parties eventually decide on a value.
- A number of solutions to the Byzantine agreement problem exist, depending on the assumptions made about the communication model, the number of corrupted parties, and the type of corruption.
- One of the most well-known solutions is the **Oral Messages Algorithm** by Lamport, Shostak, and Pease. This algorithm assumes that the communication is synchronous, meaning that there is a known upper bound on the message delivery time, and that the messages are authenticated, meaning that the sender and the content of the message cannot be forged. The algorithm also assumes that less than one-third of the parties are corrupted, and that the corruption is arbitrary, meaning that the corrupted parties can behave in any way to disrupt the agreement .
- The Oral Messages Algorithm works as follows  :
  - Each party has an initial value, which is either 0 or 1, and a round number, which starts from 0.
  - In round 0, the source party (the commander in the army scenario) sends its value to all other parties (the lieutenants).
  - In round k > 0, each party that has received a value from the source party in round k-1 sends that value to all other parties.
  - After round k, each party that has received k+1 values from the source party (either directly or indirectly) decides on the majority value among those values.
  - The algorithm terminates after n-1 rounds, where n is the total number of parties.
- The Oral Messages Algorithm guarantees that the agreement, validity, and termination conditions are met, as long as less than one-third of the parties are corrupted  .
- The Oral Messages Algorithm has a high communication complexity, as it requires O(n^2) messages per round, and O(n^3) messages in total  .
- Other solutions to the Byzantine agreement problem include the **Signed Messages Algorithm**, which reduces the communication complexity by using digital signatures, the **Randomized Algorithm**, which relaxes the agreement condition by allowing a small probability of disagreement, and the **Asynchronous Algorithm**, which does not assume a synchronous communication model .