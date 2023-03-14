### Design goals for the notes of the Unit 3 - Permissioned Blockchains in the subject of Block chain Architecture Design

The following diagram illustrates the basic architecture of a permissioned blockchain system, using the example of a supply chain network.

```
+-----------------+        +-----------------+        +-----------------+
| Supplier        |        | Manufacturer    |        | Retailer        |
|                 |        |                 |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | Validation  | |        | | Validation  | |        | | Validation  | |
| | Node        | |        | | Node        | |        | | Node        | |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | Ledger      | |        | | Ledger      | |        | | Ledger      | |
| | (Blockchain)| |        | | (Blockchain)| |        | | (Blockchain)| |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
                                 |
                                 |
                                 v
                          +-----------------+
                          | Regulator       |
                          |                 |
                          | +-------------+ |
                          | | Validation  | |
                          | | Node        | |
                          | +-------------+ |
                          |                 |
                          | +-------------+ |
                          | | Ledger      | |
                          | | (Blockchain)| |
                          | +-------------+ |
                          |                 |
                          +-----------------+
```

In a permissioned blockchain system, the participants are known and authorized to join the network. They can have different roles and permissions, such as validating transactions, reading the ledger, or writing to the ledger. The validation nodes use a consensus protocol to agree on the state of the ledger, which is replicated across all nodes. The ledger records the transactions and events that occur in the network, such as the transfer of goods or payments. The ledger is secured by cryptographic mechanisms that ensure its integrity and immutability.

Some of the design goals for permissioned blockchains are:

- **Security**: The system should protect the confidentiality, integrity, and availability of the data and the network. The system should prevent unauthorized access, tampering, or denial of service attacks. The system should also ensure the authenticity and accountability of the participants and their actions.
- **Scalability**: The system should be able to handle a large number of transactions and participants without compromising the performance or the security. The system should also be able to adapt to the changing needs and demands of the network.
- **Efficiency**: The system should minimize the resource consumption and the operational costs of the network. The system should also optimize the throughput and the latency of the transactions and the consensus protocol.
- **Interoperability**: The system should be able to communicate and exchange data with other systems and platforms, such as other blockchains, legacy systems, or external services. The system should also comply with the standards and regulations of the domain and the jurisdiction.
- **Governance**: The system should have a clear and transparent mechanism for defining and enforcing the rules and policies of the network. The system should also have a way to resolve disputes and handle exceptions. The system should also allow for the participation and feedback of the stakeholders and the users.