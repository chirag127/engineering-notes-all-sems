## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed consensus, atomic broadcast, leader election, and distributed transactions.
- Agreement protocols can be classified into different types, depending on the assumptions they make about the system model, the communication model, the failure model, and the adversary model.
- Some common types of agreement protocols are:
  - **Crash fault-tolerant protocols**: These protocols assume that processes may fail by crashing, but do not behave maliciously. They also assume that the communication is reliable and synchronous, meaning that messages are delivered within a known bounded time. Examples of crash fault-tolerant protocols are Paxos, Raft, and Two-Phase Commit.
  - **Byzantine fault-tolerant protocols**: These protocols assume that processes may fail by behaving arbitrarily, or even colluding with other faulty processes. They also assume that the communication is unreliable and asynchronous, meaning that messages may be lost, delayed, duplicated, or reordered. Examples of Byzantine fault-tolerant protocols are PBFT, Zyzzyva, and Tendermint.
  - **Randomized protocols**: These protocols use randomization techniques, such as coin tossing or sampling, to achieve agreement with high probability, even in the presence of failures or adversaries. They also relax the synchrony assumption, and allow for partial or eventual synchrony, meaning that messages are delivered within some unknown or variable time. Examples of randomized protocols are Ben-Or, Rabin, and HoneyBadgerBFT.
- Agreement protocols typically have the following properties or guarantees:
  - **Validity**: The decision value must be valid, meaning that it must be proposed by some correct process, or satisfy some predefined condition.
  - **Agreement**: All correct processes must agree on the same decision value.
  - **Termination**: All correct processes must eventually decide on some value.
  - **Integrity**: A process can decide at most once, and only on a single value.
- Agreement protocols may also have additional properties or optimizations, such as:
  - **Uniformity**: The agreement property holds even for faulty processes, meaning that they cannot decide on a different value from the correct processes.
  - **Early stopping**: The protocol can terminate in fewer rounds than the worst-case scenario, depending on the actual system behavior or the input values.
  - **Leaderlessness**: The protocol does not rely on a designated leader or coordinator, which may become a bottleneck or a single point of failure.
  - **Adaptivity**: The protocol can adapt to the changing system conditions or parameters, such as the number of failures, the network latency, or the adversary power.