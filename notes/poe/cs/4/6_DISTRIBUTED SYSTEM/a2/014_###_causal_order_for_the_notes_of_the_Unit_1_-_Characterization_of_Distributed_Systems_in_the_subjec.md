 Here is the content in markdown format:

### Causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Causal order: Messages are delivered in the same order as they were sent. If message M1 causally preceded message M2 (i.e., M1 was sent before M2 and M1's sending somehow depended on M2's sending), then M1 will be delivered before M2.
- Causal order is important for maintaining consistency and correctness in distributed systems. If messages are delivered out of causal order, it can lead to confusing or erroneous behaviour.
- For example, if a bank transfer message M1 is sent after checking the balance using message M2, then M1 and M2 have a causal relationship. Delivering M1 before M2 can lead to an overdraft, which is incorrect. Hence, causal order must be maintained.
- Causal relationships can be complex in distributed systems. Each message can have multiple causes and multiple effects. The distributed system must track all causal relationships and deliver messages accordingly.
- Some ways to implement causal order:
    - Use sequence numbers: Assign incremental sequence numbers to messages and deliver them in sequence number order. This ensures causal order is maintained.
    - Vector clocks: Use vector clocks to track causal dependencies between messages and their senders. Messages with the smallest vector clocks are delivered first, thereby maintaining causal order.
- Advantages: Ensures correctness and consistency.
- Disadvantages: Can reduce performance due to waiting for dependent messages. Tracking causal relationships can be complex to implement.
- Applications: Database systems, distributed transactions, replicated data systems.