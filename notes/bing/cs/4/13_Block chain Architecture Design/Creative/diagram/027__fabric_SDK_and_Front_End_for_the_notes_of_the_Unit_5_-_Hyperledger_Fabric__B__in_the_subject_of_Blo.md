The following is a detailed ASCII diagram for fabric SDK and Front End for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design.

The diagram shows how a client application can use the Hyperledger Fabric SDK for Node.js to interact with a Fabric network. The SDK provides APIs to submit transactions, query the ledger, and listen for events. The client application can also use the SDK to manage identities, channels, and smart contracts.

The diagram is based on the fabric-samples repository, which contains several examples of Fabric applications and network configurations. The diagram assumes that the Fabric network consists of two organizations, Org1 and Org2, each with one peer and one certificate authority. The network also has an orderer service and a channel named mychannel. The client application is using a smart contract named fabcar, which is deployed on the channel.

The diagram uses the following symbols:

- C: Client application
- S: Fabric SDK for Node.js
- P: Peer node
- O: Orderer node
- CA: Certificate authority
- L: Ledger
- E: Event hub
- W: World state
- T: Transaction proposal
- R: Transaction response
- B: Block
- Q: Query
- A: Query result
- D: Smart contract deployment
- U: Smart contract upgrade
- I: Identity enrollment
- M: Channel management
- N: Channel configuration

The diagram shows the following steps:

1. The client application uses the Fabric SDK to enroll an identity with the certificate authority of its organization. The SDK returns a user object that contains the identity credentials and can be used for subsequent operations.
2. The client application uses the Fabric SDK to create a channel object that represents the channel on the network. The SDK uses the user object and the channel configuration to connect to the peers and the orderer of the channel.
3. The client application uses the Fabric SDK to create a contract object that represents the smart contract on the channel. The SDK uses the user object and the smart contract name to connect to the peers that have the smart contract installed.
4. The client application uses the Fabric SDK to submit a transaction proposal to the peers. The SDK sends the transaction proposal to the endorsing peers of the smart contract, which execute the transaction and return a transaction response.
5. The client application uses the Fabric SDK to verify the transaction response from the peers. The SDK checks the endorsement policy of the smart contract and the signatures of the endorsing peers to ensure that the transaction is valid.
6. The client application uses the Fabric SDK to submit the transaction to the orderer. The SDK sends the transaction response to the orderer, which validates the transaction and adds it to a block.
7. The orderer broadcasts the block to the peers on the channel. The peers validate the block and append it to their ledger. The peers also update their world state with the changes from the transactions in the block.
8. The client application uses the Fabric SDK to listen for events from the peers. The SDK connects to the event hubs of the peers and receives notifications of block events and transaction events. The client application can use the events to confirm that the transaction has been committed to the ledger.
9. The client application uses the Fabric SDK to query the ledger or the world state. The SDK sends the query to one or more peers on the channel, which return the query result.
10. The client application uses the Fabric SDK to deploy or upgrade a smart contract on the channel. The SDK sends a smart contract deployment or upgrade proposal to the peers, which install the smart contract and return a transaction response. The client application then follows the same steps as submitting a transaction to commit the smart contract deployment or upgrade to the ledger.

The diagram is shown below:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Client         |     |  Fabric SDK     |     |  Fabric Network |
|  Application    |     |  for Node.js    |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |