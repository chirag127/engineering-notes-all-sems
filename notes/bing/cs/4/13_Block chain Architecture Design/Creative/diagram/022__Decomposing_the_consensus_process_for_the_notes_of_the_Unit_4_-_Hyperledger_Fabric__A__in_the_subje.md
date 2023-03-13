The following is a detailed ASCII diagram for decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design.

The diagram illustrates the basic architecture of a Hyperledger Fabric network, which consists of the following components:

- Peers: The nodes that host and execute the chaincode (smart contracts) and maintain the ledger (state and history).
- Orderers: The nodes that provide the ordering service, which ensures a consistent and agreed-upon order of transactions and batches them into blocks.
- Clients: The applications that interact with the network by invoking chaincode, submitting transactions, or querying the ledger.
- Channels: The logical partitions of the network that allow for data isolation and privacy among different sets of participants.
- Endorsement policies: The rules that specify which peers need to endorse (sign) a transaction before it can be committed to the ledger.
- Consensus policies: The rules that specify how the orderers reach agreement on the order and correctness of transactions.

The diagram also shows the steps involved in the consensus process, which can be summarized as follows:

1. A client application submits a transaction proposal to one or more endorsing peers, specifying the chaincode, the channel, and the arguments.
2. The endorsing peers simulate the transaction by executing the chaincode with the given arguments and produce a transaction response, which contains the read/write set (the state changes), the endorsement signature, and a proposal response payload.
3. The client application collects the transaction responses from the endorsing peers and verifies that they meet the endorsement policy. If the endorsement policy is satisfied, the client application creates a transaction message, which contains the transaction proposal and the proposal responses, and broadcasts it to the ordering service.
4. The ordering service receives the transaction messages from different clients and assigns them a unique sequence number based on the consensus algorithm. The ordering service then packages the transactions into blocks and delivers them to the committing peers on the channel.
5. The committing peers validate the transactions by checking the endorsement policy and the read/write set against the current state of the ledger. If the transactions are valid, the committing peers append the block to the ledger and update the state accordingly. If the transactions are invalid, the committing peers mark them as such and do not update the state.

The diagram is drawn using the following symbols:

- [ ]: A box represents a component or a node in the network.
- - or |: A line represents a connection or a communication between components or nodes.
- -> or <-: An arrow represents the direction of the communication or the flow of the data.
- ( ): A parenthesis represents a step or an action in the consensus process.
- ...: An ellipsis represents a repetition or an omission of similar elements for brevity.

The diagram is as follows:

```
    [Client] -> (1) Transaction proposal -> [Peer 1] -\
                                                     \
    [Client] -> (1) Transaction proposal -> [Peer 2] -+-> (2) Transaction response -> [Client] -> (3) Transaction message -> [Orderer 1] -\
                                                     /                                                                           \
    [Client] -> (1) Transaction proposal -> [Peer 3] -/                                                                             \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \
                                                                                                                                    \ 
                                                                                                                                    |
[Orderer 1] -\                                                                                                                      |
             \                                                                                                                      |
[Orderer 2] -+-> (4) Consensus algorithm -> [Orderer 1] -> (4) Block delivery -> [Peer 1] -> (5) Transaction validation -> [Ledger] |
             /                                                                                                                      |
[Orderer 3] -/                                                                                                                      |
                                                                                                                                    |
                                                                                                                                    /
                                                                                                                                    |
[Orderer 1] -> (4) Block delivery -> [Peer 2] -> (5) Transaction validation -> [Ledger]                                             |
                                                                                                                                    |
                                                                                                                                    /
                                                                                                                                    |
[Orderer 1] -> (4) Block delivery -> [Peer 3] -> (5) Transaction validation -> [Ledger]                                             |
                                                                                                                                    |
                                                                                                                                    /
                                                                                                                                    |
[Orderer 1] -> (4) Block delivery -> [Peer 4] -> (5) Transaction validation -> [Ledger]                                             |
                                                                                                                                    |
                                                                                                                                    /
                                                                                                                                    |