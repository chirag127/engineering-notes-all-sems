## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed consensus, atomic broadcast, leader election, and distributed transactions.
- Agreement protocols can be classified into different types, depending on the assumptions they make about the system model, the communication model, the failure model, and the adversary model.
- Some common types of agreement protocols are:
  - **Crash fault-tolerant protocols**: These protocols assume that processes may fail by crashing, but do not behave maliciously. They also assume that the communication is reliable and synchronous, meaning that messages are delivered within a known bounded time. Examples of crash fault-tolerant protocols are Paxos, Raft, and Two-Phase Commit.
  - **Byzantine fault-tolerant protocols**: These protocols assume that processes may fail by behaving arbitrarily, or even colluding with other faulty processes. They also assume that the communication is reliable, but may be asynchronous, meaning that messages may be delayed arbitrarily or even lost. Examples of Byzantine fault-tolerant protocols are PBFT, Zyzzyva, and Tendermint.
  - **Asynchronous fault-tolerant protocols**: These protocols assume that processes may fail by crashing, but do not behave maliciously. They also assume that the communication is unreliable and asynchronous, meaning that messages may be delayed arbitrarily, lost, duplicated, or reordered. Examples of asynchronous fault-tolerant protocols are Ben-Or, Chandra-Toueg, and Bracha.
- Agreement protocols typically have the following properties:
  - **Validity**: If all processes start with the same initial value, then they must decide on that value.
  - **Agreement**: No two correct processes decide on different values.
  - **Termination**: Every correct process eventually decides on some value.
  - **Integrity**: If a process decides on a value, then that value must have been proposed by some process.
- Agreement protocols may also have additional properties, such as:
  - **Uniform agreement**: No two processes, whether correct or faulty, decide on different values.
  - **Uniform validity**: If a process decides on a value, then that value must have been the initial value of some process.
  - **Uniform integrity**: If a process decides on a value, then that value must have been proposed by some correct process.
  - **Non-triviality**: There exists some execution in which processes decide on different values.