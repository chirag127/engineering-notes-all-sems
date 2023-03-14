### Dynamic voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

Dynamic voting protocols are used in distributed systems to ensure fault tolerance by allowing nodes to reach consensus on a value, even in the presence of crashed or malicious nodes. In this protocol, each node has a vote, and the votes are dynamically reassigned depending on the state of the system. Here is a detailed explanation of dynamic voting protocols:

1. Nodes start with equal votes - In the beginning, all nodes have an equal number of votes. This ensures that each node has an equal say in the decision-making process.

2. Nodes can change their votes - If a node detects a fault or crash in another node, it can change its vote to reflect this. For example, if a node crashes, its vote can be transferred to a node that is still functioning.

3. Nodes can reassign their own votes - A node can also reassign its own vote to another node if it believes that the other node is more trustworthy or has more information.

4. Nodes can add or remove votes from the system - In some dynamic voting protocols, nodes can add or remove votes from the system. This can be useful in situations where new nodes join the system or when nodes are known to be unreliable.

5. Consensus is reached through a voting process - Once all nodes have cast their votes, a consensus value can be determined. This value is then broadcasted to all nodes in the system.

Advantages of dynamic voting protocols:

- Dynamic voting protocols can handle the presence of failed or malicious nodes in the system, ensuring fault tolerance.

- These protocols are flexible and can adapt to changes in the system, such as the addition or removal of nodes.

- Dynamic voting protocols can handle asynchronous communication between nodes.

Disadvantages of dynamic voting protocols:

- Dynamic voting protocols can be vulnerable to attacks by malicious nodes that attempt to manipulate the voting process.

- These protocols can be complex to implement and require careful tuning to ensure that they work correctly.

Mnemonics and learning tricks:

- One possible mnemonic for remembering the steps of dynamic voting protocols is "Equal, Change, Reassign, Add/Remove, Vote" (ECRAV).

- Another trick is to think of the voting process as a game of musical chairs. Each node has a chair (vote), and when a node leaves the game (crashes), its chair is removed. The remaining nodes then have to quickly reassign their votes to the remaining chairs before the music stops (consensus is reached).