 Here is the content in markdown format for the topic ### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Architectural models for Distributed Systems

The architectural models for distributed systems are:

1. Client-Server model:
- In this model, there are dedicated server processes that provide resources or services to client processes.
- Clients connect to the servers, request services and get responses.
- Eg: Web server and web browser.

Mnemonic: The boss(server) serves the customers(clients).

2. Peer-to-Peer model:
- In this model, all processes have equal responsibilities and capabilities.
- There is no dedicated server.
- Peers communicate with each other and share resources.
- Eg: BitTorrent, Skype.

Mnemonic: Friends(peers) sharing with each other.

3. Message Passing model:
- Processes communicate by exchanging messages.
- Messages are passed asynchronously.
- The processes may be arranged in client-server or peer-to-peer architectures.
- Eg: Email, multiplayer online games.

Advantages:
- Loose coupling between processes. Processes are independent and interact via messages.
- Scalable as more processes can be added easily.

Disadvantages:
- Processes must agree on a message format and protocol.
- Process synchronization can be difficult.
- Ordering of messages may be uncertain.

Applications: Distributed simulation systems, multi-player online games, etc.

[Include ascii diagrams and examples if required]