The following is a detailed ASCII diagram for Beyond Chaincode for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design.

Beyond Chaincode is a project that aims to enable the execution of chaincodes using Intel SGX for Hyperledger Fabric. Intel SGX is a technology that allows applications to run in a secure enclave, isolated from the rest of the system. This way, the chaincode logic and data can be protected from unauthorized access or tampering, even by the endorsing peers or the orderers.

The basic architecture of Beyond Chaincode consists of the following components:

- FPC Client: A client application that interacts with the FPC chaincode through the Fabric SDK. The FPC client also manages the attestation process and the encryption/decryption of the transaction arguments and responses.
- FPC Shim: A modified version of the Fabric chaincode shim that implements the FPC protocol and interfaces with the FPC chaincode enclave. The FPC shim is responsible for verifying the endorsements and the enclave signatures, as well as handling the state encryption/decryption.
- FPC Chaincode Enclave: A secure enclave that runs the FPC chaincode logic and maintains a private ledger state. The FPC chaincode enclave is created and attested by the FPC Enclave Registry and communicates with the FPC Shim through the FPC Enclave Chaincode API.
- FPC Enclave Registry: A chaincode that maintains a registry of all the FPC chaincode enclaves in the network and their attestation evidence. The FPC Enclave Registry is used by the FPC Shim and the FPC Client to verify the authenticity and integrity of the FPC chaincode enclave.
- FPC Validation Plugin: A custom validation plugin that extends the Fabric validation system chaincode (VSCC) and implements the FPC validation rules. The FPC Validation Plugin checks the validity and consistency of the FPC transactions and the FPC chaincode enclave signatures.

The diagram below illustrates the basic architecture of Beyond Chaincode and the flow of a FPC transaction:

```
+-------------------+                  +-------------------+
|                   |                  |                   |
|   FPC Client      |                  |   FPC Client      |
|                   |                  |                   |
+-------------------+                  +-------------------+
       |  |                                   |  |
       |  | Fabric SDK                        |  | Fabric SDK
       |  |                                   |  |
       |  +-----------------------------------+  |
       |      invoke/query                    |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       v                                       v  |
+-------------------+                  +-------------------+
|                   |                  |                   |
|   FPC Shim        |                  |   FPC Shim        |
|                   |                  |                   |
+-------------------+                  +-------------------+
       |  |                                   |  |
       |  | FPC Protocol                     |  | FPC Protocol
       |  |                                   |  |
       |  +-----------------------------------+  |
       |   invoke/query                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       v                                       v  |
+-------------------+                  +-------------------+
|                   |                  |                   |
| FPC Chaincode     |                  | FPC Chaincode     |
| Enclave           |                  | Enclave           |
|                   |                  |                   |
+-------------------+                  +-------------------+
       |  |                                   |  |
       |  | FPC Enclave Chaincode API        |  | FPC Enclave Chaincode API
       |  |                                   |  |
       |  +-----------------------------------+  |
       |   invoke/query                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |  |
       |                                       |