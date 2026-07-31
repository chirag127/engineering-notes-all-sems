## Unit 4 - Agreement Protocols

Agreement protocols are a class of protocols used in distributed systems to ensure that all processes in the system agree on a certain value or state. These protocols are essential for the correct functioning of distributed systems, as they allow processes to coordinate their actions and make decisions based on a common understanding of the system state.

Some common types of agreement protocols include:

1. **Consensus protocols:** These protocols are used to ensure that all processes in the system agree on a single value. This is typically achieved through a series of rounds, where processes propose values and vote on them until a single value is chosen by a majority of processes.

2. **Byzantine agreement protocols:** These protocols are a variant of consensus protocols that are designed to tolerate Byzantine faults, where some processes may behave arbitrarily or maliciously. Byzantine agreement protocols typically require a larger number of rounds and more complex voting mechanisms to ensure that all correct processes agree on a single value, even in the presence of faulty processes.

3. **Atomic commit protocols:** These protocols are used to ensure that a set of transactions are either all committed or all aborted, even in the presence of failures. Atomic commit protocols typically involve a coordinator process that collects votes from all participating processes and decides whether to commit or abort the transactions based on the votes received.

4. **Leader election protocols:** These protocols are used to elect a leader process among a group of processes. The leader process is responsible for coordinating the actions of the other processes and making decisions on behalf of the group. Leader election protocols typically involve a series of rounds, where processes propose themselves as leaders and vote on the proposals until a single leader is elected.

Agreement protocols are a fundamental building block of distributed systems, and are used to ensure the correctness and consistency of the system state in the presence of failures and asynchrony. They are an active area of research, with many different protocols and variations being proposed and studied.