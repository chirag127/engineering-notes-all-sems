### Proof of Work (PoW) for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design

- Proof of work (PoW) is a **decentralized system** used to verify the accuracy of transactions on the blockchain network.
- Proof of work removes the need for a central authority like a bank, business, or government agency to monitor and manage transactions and their corresponding accounts.
- Proof of work lets blockchain networks operate by **consensus rules** rather than “trust”.
- Proof of work is based on the concept of **hashes**, which are mathematical functions that transform any input data into a fixed-length output.
- Hashes have two important properties: they are **one-way** (meaning it is easy to compute the output from the input, but hard to reverse the process) and they are **collision-resistant** (meaning it is very unlikely that two different inputs will produce the same output).
- When a block of transactions is closed, the hash of the block must be verified before a new block can be opened. This is where proof of work comes in.
- Proof of work requires the block's hash to satisfy a certain condition, such as having a specific number of leading zeros. This condition is called the **difficulty**.
- The difficulty is adjusted periodically to ensure that the average time between blocks remains constant, usually around 10 minutes for Bitcoin.
- To find a valid hash, the block's data is combined with a random number called a **nonce**. The nonce is changed repeatedly until a valid hash is found.
- The process of finding a valid hash is called **mining**, and it requires a lot of computational power and energy.
- The first miner who finds a valid hash broadcasts the block to the network, and the other nodes verify the block and add it to the blockchain.
- The miner who finds the valid hash is rewarded with newly created coins and transaction fees. This is the incentive for miners to participate in the proof of work system.
- Proof of work ensures that the blockchain is **secure** and **immutable**, as any attempt to alter a block would require recomputing the hashes of all subsequent blocks, which would be impractical and costly.
- Proof of work also ensures that the blockchain is **democratic** and **transparent**, as anyone can join the network and verify the transactions.
- However, proof of work also has some drawbacks, such as high energy consumption, low scalability, and vulnerability to attacks such as 51% attacks, where a malicious miner or group of miners controls more than half of the network's computing power and can manipulate the blockchain.
- Therefore, some blockchain developers are exploring alternative verification systems, such as proof of stake, proof of authority, or proof of space.