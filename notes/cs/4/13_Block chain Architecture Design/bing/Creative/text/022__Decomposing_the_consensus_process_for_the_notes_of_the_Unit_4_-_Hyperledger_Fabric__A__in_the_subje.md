### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus is a process in computer science used to achieve agreement on a single data value among distributed processes or systems.
- Consensus in Hyperledger Fabric is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate the blocks of transactions that need to be committed to the ledger.
- Consensus in Hyperledger Fabric must ensure the following in the network:
  - Confirms the correctness of all transactions in a proposed block, according to endorsement and consensus policies.
  - Agrees on order and correctness and hence on results of execution (implies agreement on global state).
  - Interfaces and depends on smart-contract layer to verify correctness of an ordered set of transactions in a block.
- Consensus in Hyperledger Fabric must satisfy two properties to guarantee agreement among nodes: safety and liveness.
  - Safety means that each node is guaranteed the same sequence of inputs and results in the same output on each node. When the nodes receive an identical series of transactions, the same state changes will occur on each node. The algorithm must behave identical to a single node system that executes each transaction atomically one at a time.
  - Liveness means that each non-faulty node will eventually receive every submitted transaction, assuming that communication does not fail.
- Consensus in Hyperledger Fabric is broken out into 3 phases: Endorsement, Ordering, and Validation .
  - Endorsement is driven by policy (m out of n signatures) upon which participants endorse a transaction. Endorsement policies define which organizations must approve a transaction before it can be committed to the ledger.
  - Ordering phase will get the endorsed transactions and agrees to the order to be committed to the ledger. Ordering nodes are responsible for ordering transactions into blocks and broadcasting them to the network. Ordering nodes can use different algorithms to reach consensus on the order of transactions, such as Solo (for development) or Kafka (for production).
  - Validation takes a block of ordered transactions and validates the correctness of the result. Validation nodes check that the transactions have been endorsed by the required organizations, that there are no conflicts or duplicates, and that the transactions are well-formed. Valid transactions are marked as valid and written to the ledger, while invalid transactions are marked as invalid and not written to the ledger.