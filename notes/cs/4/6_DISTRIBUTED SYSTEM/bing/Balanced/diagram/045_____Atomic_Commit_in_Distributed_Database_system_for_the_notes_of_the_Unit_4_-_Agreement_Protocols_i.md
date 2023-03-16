### Atomic Commit in Distributed Database System

- A distributed database system consists of multiple database sites that are connected by a communication network.
- A distributed transaction is a transaction that accesses data from multiple sites and updates them atomically.
- Atomicity means that either all the updates are committed or none of them are committed, leaving the database in a consistent state.
- Atomic commit is the process of coordinating the decision to commit or abort a distributed transaction among all the participating sites.
- Atomic commit protocols are algorithms that ensure the atomicity of distributed transactions in the presence of failures, such as site crashes, network partitions, or message losses.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking.
  - Blocking protocols require some sites to wait for the recovery of other sites before making a final decision. Examples of blocking protocols are the two-phase commit (2PC) protocol and the three-phase commit (3PC) protocol.
  - Non-blocking protocols allow some sites to make a final decision without waiting for the recovery of other sites. Examples of non-blocking protocols are the Paxos commit protocol and the FLAC protocol.
- The performance and reliability of atomic commit protocols depend on various factors, such as the number of sites, the number of messages, the failure rate, the recovery time, and the network latency.