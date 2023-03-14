 Here is the content in markdown format:

### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

The consensus process in Hyperledger Fabric involves the following steps:

1. Peer to peer gossip - Peers gossip with each other to spread transactions and blocks across the network. This is a continuous process and happens asynchronously.
2. Leader election - When a peer wants to propose a block, it starts an instance of leader election to decide which peer will create the block proposal. The peer that wins the leader election creates the block proposal.
3. Block proposal - The winning peer of the leader election creates a block proposal which contains a set of endorsed transactions.
4. Endorsement - The block proposal is sent to the peer's endorsers (other organizations) to endorse the proposal. The endorsers simulate and validate the transactions in the proposal and endorse it.
5. Ordering - The endorsers then send the endorsed block proposal to the ordering service. The ordering service orders the endorsements and creates a block containing the ordered and endorsed transactions.
6. Commitment - The ordering service sends the block to the committing peers (one peer from each organization). The committing peers validate and commit the block.
7. BlockDistribution - The committing peers then distribute the committed block to the peers in their organization. The peers validate the block and the transactions and add the block to their blockchain.

Some key points to remember:

- The consensus process is decentralized and happens asynchronously across multiple peers and organizations.
- No single peer is responsible for the entire consensus process. Different steps are carried out by different peers.
- The ordering service is responsible for ordering transactions and creating blocks but it does not validate transactions or modify the blockchain.
- Validation happens at multiple steps (endorsement, commitment, block distribution) to ensure high integrity of the blockchain.

Mnemonics:

PELEODCBB - Peer gossip, Leader election, Endorsement, Ordering, Commitment, Block distribution, Block addition

This mnemonic represents the steps in the consensus process. Easy to remember and can be helpful in recollecting the steps.