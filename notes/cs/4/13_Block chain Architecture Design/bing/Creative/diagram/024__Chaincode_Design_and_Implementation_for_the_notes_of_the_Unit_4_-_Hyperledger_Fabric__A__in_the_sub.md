The following is a detailed ascii diagram for Chaincode Design and Implementation for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design. The diagram is based on the information from the web search results   .

Chaincode Design and Implementation Diagram
```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Application    |      |  Endorsing      |      |  Chaincode      |
|                 |      |  Peer           |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Invoke/Query   |----->|  Invoke/Query   |----->|  Init/Invoke    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Proposal       |<-----|  Proposal       |<-----|  Response       |
|  Response       |      |  Response       |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Endorsement    |----->|  Endorsement    |----->|  Endorsement    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Transaction    |<-----|  Transaction    |<-----|  Transaction    |
|  Response       |      |  Response       |      |  Response       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram illustrates the basic architecture of a chaincode application, which consists of three main components: the application, the endorsing peer, and the chaincode. The application is the client that invokes or queries the chaincode through the endorsing peer. The endorsing peer is the node that executes the chaincode and validates the transactions. The chaincode is the program that implements the business logic and interacts with the ledger state.

The diagram also shows the flow of messages between the components, which can be summarized as follows:

- The application sends an invoke or query request to the endorsing peer, which creates a proposal for the chaincode.
- The endorsing peer forwards the proposal to the chaincode, which initializes or invokes the chaincode logic and returns a response to the endorsing peer.
- The endorsing peer sends the proposal response back to the application, which checks the endorsement policy and decides whether to proceed with the transaction or not.
- If the application decides to proceed, it sends the endorsement to the endorsing peer, which creates a transaction and submits it to the orderer service for validation and commitment.
- The endorsing peer receives the transaction response from the orderer service and sends it back to the application, which verifies the transaction status and updates its state accordingly.