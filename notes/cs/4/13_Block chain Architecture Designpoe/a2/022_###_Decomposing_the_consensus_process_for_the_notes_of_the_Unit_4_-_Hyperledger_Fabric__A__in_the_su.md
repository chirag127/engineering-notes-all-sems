 Here is the content in markdown format for the topic -

### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

The consensus process in Hyperledger Fabric involves the following steps -

1. **Client proposes a transaction** - The client submits a transaction proposal to the network. The proposal is delivered to the targeted peers (`endorsers`) based on the transaction target.

2. **Endorsers validate and endorse** - The endorsers simulate the transaction on their local stores and validate its correctness. If valid, they sign and endorse the transaction and send it back to the client.

3. **Client sends endorsed proposal for ordering** - The client collects endorsements and sends the endorsed proposal to the ordering service for ordering.

4. **Ordering service orders transactions** - The ordering service orders transactions into a block and creates a block hash.

5. **Block is delivered to committers** - The ordered block is delivered to the committing peers (`committers`).

6. **Committers validate and commit** - The committers validate the transactions in the block and commit the block to the ledger.

7. **Ledger is updated** - The ledger state is updated with the committed transactions.

Some key points to note -

- Consensus is reached on the ordering of transactions, not on the content of transactions.
- Individual organizations validate transactions independently. There is no single point of global validation.
- Some organizations are responsible for ordering transactions (ordering service) and committing blocks to the ledger (committing peers).
- The consensus process is pluggable and different implementations can be used. For example, Kafka can be used as the ordering service instead of the default noops implementation.

Advantages - Decentralization, permissioned blockchain, scalability through parallelization, confidentiality through channels.

Disadvantages - Complex setup and configuration, less transparency than public blockchains.