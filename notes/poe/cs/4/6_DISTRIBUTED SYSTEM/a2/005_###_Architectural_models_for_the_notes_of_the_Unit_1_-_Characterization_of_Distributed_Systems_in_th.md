 Here is the content in markdown format for the topic -

### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

The architectural models for distributed systems are:

1. Client-Server Model:
- In this model, clients send requests to the server which processes them and sends back responses.
- The server has more capabilities and resources than the clients.
- Examples: Web browsing, Email, File sharing.
- Advantage: Separation of concerns. Server can be optimized for processing.
- Disadvantage: Single point of failure. If server crashes, service unavailable.

2. Peer-to-peer Model:
- All nodes have similar capabilities and responsibilities.
- Examples: BitTorrent, Skype, Gnutella.
- Advantage: Fault tolerance. No single point of failure.
- Disadvantage: Complex to implement. Heterogeneity of peers and resources.

3. Message Passing Model:
- Systems are built as a collection of processes that communicate via message passing.
- Examples: Erlang, MPI.
- Advantage: Fault tolerance, distribution transparency.
- Disadvantage: Difficult to program. Explicit handling of communication required.

**Mnemonics**:
C-S-P: C(lient)-S(erver)-P(eer-to-peer)

**Learning Trick**: Relate daily examples to the models to understand them easily. Like, ordering food from a restaurant (client-server) and chatting with friends (peer-to-peer).

The models have their own pros and cons and are suitable for different types of applications. The choice of a model depends on the specific requirements and goals of the system being designed.