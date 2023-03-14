### Proof of Work (PoW) for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design

- Proof of work (PoW) is a **decentralized consensus mechanism** that requires network members to expend **effort in solving an encrypted hexadecimal number**.
- Proof of work is also called **mining**, in reference to receiving a **reward** for work done.
- Proof of work allows for **secure peer-to-peer transaction processing** without needing a **trusted third party**.
- Proof of work was adapted for digital tokens by **Hal Finney** in 2004 through the idea of \"reusable proof of work\" using the 160-bit secure hash algorithm 1 (SHA-1).
- Proof of work forms the basis of many cryptocurrencies, such as **Bitcoin**, which became the first widely adopted application of Finney's PoW idea in 2009.
- Proof of work is used to **prevent the 51% attack or double-spends**, which are scenarios where some nodes try to act against the consensus or spend the same tokens twice.
- Proof of work is based on the concept of **Byzantine Fault Tolerance (BFT)**, which is a system capable of withstanding failures associated with the Byzantine Generals’ Problem.
- The Byzantine Generals’ Problem is a classic dilemma in distributed computing, where a group of generals must agree on a common strategy to attack or retreat, but some of them may be traitors who send false messages.
- Proof of work solves the Byzantine Generals’ Problem by requiring nodes to **prove** that they have done some **work** to validate a block of transactions, such as solving a complex mathematical problem.
- The mathematical problem involves finding a **nonce**, which is a random number that, when combined with the block data and hashed, produces a result that meets a certain **difficulty** criterion.
- The difficulty criterion is a parameter that adjusts the **target** value of the hash, which determines how hard it is to find a valid nonce.
- The difficulty is adjusted periodically to maintain a **constant block time**, which is the average time it takes to produce a new block.
- The first node to find a valid nonce and broadcast it to the network is the **winner** of the block, and receives the **block reward** and the **transaction fees**.
- The other nodes then **verify** the validity of the nonce and the block, and **append** it to their copy of the blockchain.
- The longest chain of blocks is considered the **valid** one, and any conflicting blocks are discarded as **orphan** blocks.
- Proof of work creates a **healthy and transparent** closed economy, where nodes are incentivized to contribute to the network security and honesty.
- Proof of work also creates a **randomized** and **fair** selection process for block winners, where the probability of winning is proportional to the **hashing power** of the node.
- Hashing power is the measure of the **computing resources** that a node can dedicate to mining.
- Proof of work at scale requires **vast amounts of energy**, which only increases as more miners join the network.
- Proof of work is also vulnerable to **centralization** and **collusion**, where large mining pools or entities can gain a majority of the hashing power and influence the network.
- Proof of work is being challenged by alternative consensus mechanisms, such as **proof of stake**, which are more **energy-efficient** and **secure**.

Some possible mnemonics and learning tricks for proof of work are:

- PoW = Proof of Work = Puzzle of Work = Puzzle of nonce
- Nonce = Number used ONCE = Number that makes hash ONCE in a while
- Difficulty = D for Down = Target value goes Down as difficulty goes up
- Block time = B for Balance = Balance between too fast and too slow
- Block reward = B for Bitcoin = Bitcoin is the first and most famous block reward
- Transaction fees = T for Tip = Tip the miner for validating your transaction
- Byzantine Fault Tolerance = BFT = Big Fault Test = Test for big faults like traitors
- Hashing power = HP = High Performance = High performance means more hashing power
- Proof of stake =