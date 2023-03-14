 Here is the content in markdown format for the topic -

### Requirements for the consensus protocols for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design

The consensus protocols for blockchain should satisfy the following requirements:

1. Agreement - The nodes in the network should agree on the same value for the blockchain state. There should be no disagreement between the nodes regarding the order of transactions or the current state of the blockchain.
2. Validity - The consensus protocol should never approve an invalid transaction or block. Only valid transactions should be added to the blockchain.
3. Termination - The consensus protocol should eventually terminate and reach a decision. It should not be an endless process.
4. Liveness - The consensus protocol should not prevent valid transactions or blocks from being permanently added to the blockchain. There should be a reasonable time limit within which consensus is achieved.
5. Safety - The consensus protocol should be safe. The system should not reach a state where two blocks have the same height on the blockchain. There should not be any forks in the blockchain.
6. Chain Quality - The consensus protocol should produce a high-quality blockchain with fast transaction finality and high throughput. The performance of the blockchain should not degrade with increasing number of nodes in the network.

Some useful mnemonics to remember the requirements are -

- Agree to validate
- Terminate liveness safely
- Chain quick quality

The Byzantine Fault Tolerance consensus protocols like Practical Byzantine Fault Tolerance (PBFT) and Proof-of-Authority (POA) satisfy all the above requirements and are suitable for permissioned blockchains. Proof-of-Work and Proof-of-Stake are more suitable for public blockchains but may compromise on factors like performance and quality.

The detailed notes can include diagrams, examples, codes, advantages, and disadvantages of different consensus protocols and their applications in various blockchain use cases. The content can be made elaborate based on the depth of knowledge expected for exams.