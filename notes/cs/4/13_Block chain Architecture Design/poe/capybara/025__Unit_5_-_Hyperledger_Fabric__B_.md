## Unit 5 - Hyperledger Fabric (B)

In this unit, we will dive deeper into Hyperledger Fabric and its components. Here are some key points to keep in mind:

- Hyperledger Fabric consists of various components, including peers, orderers, and clients.
- Peers are responsible for storing and maintaining the state of the ledger. They communicate with each other to ensure consistency and accuracy of the data.
- Orderers handle the ordering of transactions and ensure that they are added to the ledger in the correct order. They also prevent double-spending and ensure that transactions are valid.
- Clients interact with the network by submitting transactions to the orderer and querying the state of the ledger from the peers.
- Hyperledger Fabric also allows for the use of smart contracts or chaincode, which are self-executing programs that run on the network. They are written in programming languages like Go or JavaScript.
- Chaincode is installed on peers and executed in response to transactions submitted by clients. It can read and write data to the ledger, as well as invoke other chaincode.
- Hyperledger Fabric uses a permissioned network model, which means that participants on the network must be authorized to access it. This is achieved through the use of membership services providers (MSPs) and identity management.
- MSPs are responsible for managing identities and access control on the network. They verify the authenticity of participants and their actions.
- Transactions on Hyperledger Fabric are executed using a consensus protocol called Practical Byzantine Fault Tolerance (PBFT). It ensures that all nodes on the network agree on the order and validity of transactions.
- Hyperledger Fabric also supports private data, which allows for the storage of confidential information that is only visible to authorized parties.
- Finally, Hyperledger Fabric offers scalability and high throughput, making it suitable for enterprise-level applications.

By understanding these key points, you will have a solid foundation for understanding Hyperledger Fabric and its components.