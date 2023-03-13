The following is a detailed ASCII diagram for KYC for the notes of the Unit 6 - Use case 1 in the subject of Blockchain Architecture Design.

The diagram illustrates the basic architecture of a blockchain-based decentralized KYC system that allows different service providers to share and verify the identity and address of the customers. The system consists of four main components: the customers, the service providers, the KYC smart contract, and the blockchain ledger.

The customers are the individuals or entities who want to use the services of the service providers. They have to register their identity and address information with one of the service providers and get a unique KYC ID. The customers can also update or revoke their information at any time.

The service providers are the entities that offer various services to the customers, such as banking, insurance, e-commerce, etc. They have to comply with the KYC regulations and verify the identity and address of the customers before providing the services. They can use the KYC smart contract to access the information of the customers who have registered with other service providers, and also to share their own information with other service providers.

The KYC smart contract is a program that runs on the blockchain and implements the logic and rules of the KYC system. It acts as an intermediary between the service providers and the customers, and ensures that the information is securely stored, updated, and verified on the blockchain ledger. The KYC smart contract also maintains a mapping of the KYC IDs and the service providers who have verified them.

The blockchain ledger is a distributed database that records the history of transactions and events in the KYC system. It provides immutability, transparency, and accountability for the KYC information. The blockchain ledger is maintained by a network of nodes that validate and append new blocks of data to the ledger.

The diagram shows an example of how the KYC system works. The steps are as follows:

1. Customer A registers with Service Provider 1 and provides their identity and address information. Service Provider 1 verifies the information and assigns a KYC ID to Customer A. Service Provider 1 also invokes the KYC smart contract to store the information and the KYC ID on the blockchain ledger.
2. Customer A wants to use the service of Service Provider 2. Customer A provides their KYC ID to Service Provider 2. Service Provider 2 invokes the KYC smart contract to check if the KYC ID is valid and if Service Provider 2 has verified it before.
3. The KYC smart contract returns the information of Customer A and the list of service providers who have verified the KYC ID. Service Provider 2 verifies the information and adds itself to the list of verifiers. Service Provider 2 also invokes the KYC smart contract to update the list of verifiers on the blockchain ledger.
4. Customer A can now use the service of Service Provider 2. Service Provider 2 can also access the information of Customer A from the blockchain ledger at any time.
5. Customer A updates their address information with Service Provider 1. Service Provider 1 verifies the new information and invokes the KYC smart contract to update the information on the blockchain ledger. The KYC smart contract also notifies the other service providers who have verified the KYC ID of Customer A about the update.
6. Customer A revokes their information with Service Provider 1. Service Provider 1 invokes the KYC smart contract to delete the information and the KYC ID from the blockchain ledger. The KYC smart contract also notifies the other service providers who have verified the KYC ID of Customer A about the revocation.

The diagram is drawn using the following ASCII symbols:

- + : corner of a box
- - : horizontal line of a box
- | : vertical line of a box
- > : arrow pointing right
- < : arrow pointing left
- ^ : arrow pointing up
- v : arrow pointing down
- / : diagonal line of a box
- \ : diagonal line of a box
- = : double horizontal line
- # : double vertical line
- * : asterisk for bullet point
- ( ) : parentheses for labels

The diagram is as follows:

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|   Customer A     |     | Service Provider |     | Service Provider |
|                  |     |        1         |     |        2         |
+------------------+     +------------------+     +------------------+
       |  |                     |  |                     |  |
       |  |                     |  |                     |  |
       |  |