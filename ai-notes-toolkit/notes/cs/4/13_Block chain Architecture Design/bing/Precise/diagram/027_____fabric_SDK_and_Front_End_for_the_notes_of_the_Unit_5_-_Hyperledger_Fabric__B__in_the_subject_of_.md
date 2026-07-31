### Fabric SDK and Front End

Hyperledger Fabric is a blockchain framework implementation that allows components, such as consensus and membership services, to be plug-and-play. Fabric SDKs provide a way for developers to interact with a Fabric network.

1. **Fabric SDKs**: Fabric SDKs are available in multiple programming languages, including Node.js, Java, and Go. These SDKs provide APIs for developers to interact with a Fabric network, including submitting transactions, querying the ledger, and managing the lifecycle of chaincode.

2. **Front End**: The front end of a Fabric application typically interacts with the Fabric network through a Fabric SDK. The front end can be developed using any web development framework and can provide a user interface for users to interact with the blockchain network.

3. **Chaincode**: Chaincode is the smart contract logic that runs on the Fabric network. It is written in a supported programming language, such as Go or Java, and is deployed and managed using the Fabric SDKs.

4. **Ledger**: The ledger in Fabric is a distributed database that stores the state of the blockchain network. The ledger is updated through the submission of transactions, which are validated and committed by the network's consensus mechanism.

5. **Consensus**: Fabric supports pluggable consensus mechanisms, allowing different networks to use different consensus algorithms. The consensus mechanism is responsible for validating and ordering transactions before they are committed to the ledger.

6. **Membership Services**: Fabric provides a membership service that manages the identities of the participants in the network. This service is responsible for issuing and validating digital certificates, which are used to authenticate and authorize transactions on the network.

Overall, the Fabric SDKs and front end provide a way for developers to build applications that interact with a Fabric blockchain network. These tools allow developers to submit transactions, query the ledger, and manage the lifecycle of chaincode on the network. The front end provides a user interface for users to interact with the blockchain network, while the Fabric SDKs provide the APIs for the front end to communicate with the network.