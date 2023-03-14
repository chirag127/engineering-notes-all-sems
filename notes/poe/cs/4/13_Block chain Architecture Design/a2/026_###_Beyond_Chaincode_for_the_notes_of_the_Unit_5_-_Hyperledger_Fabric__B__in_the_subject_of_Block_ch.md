 Here is the content in markdown format for the topic ### Beyond Chaincode for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design:

### Beyond Chaincode

Beyond chaincode, there are a few other ways to implement business logic on Hyperledger Fabric:

- **External chaincode** - Chaincode can be written to simply proxy requests to an external system. The external system would host the core business logic. This allows leveraging existing services/systems and not having to rewrite all logic in chaincode.
- **Event-driven chaincode** - Chaincode could be implemented to react to events (blockchain events or external events) and perform certain actions as a result. This could enable more complex, reactive business logic.
- ** Compiler Integrations** - There are experimental integrations available for compiling code written in other languages (Go, JavaScript, etc.) into chaincode. This could make it easier to write complex logic. However, there are more restrictions on what that code can access for security reasons.

Advantages:
- Leverage existing systems/logic
- Potential for more complex logic

Disadvantages:
- External dependencies introduce additional operational complexity
- May be harder to keep logic decentralized and maintain high throughput
- Less battle-tested - newer ways of implementing chaincode logic

In general, for most basic use cases, standard chaincode functions provide a good balance of simplicity and capability. As blockchain use cases get more complex, these additional options are available to help meet the needs - but they should be evaluated carefully.