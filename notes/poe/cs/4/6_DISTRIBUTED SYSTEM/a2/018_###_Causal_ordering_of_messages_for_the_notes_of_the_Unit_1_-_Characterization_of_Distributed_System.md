 Here is the content in markdown format for the given topic:

### Causal ordering of messages for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Causal ordering ensures that messages are delivered in the same order as they were sent. This is important in distributed systems to maintain consistency and correctness.

**Example:**
Suppose process P1 sends messages m1 and m2 to process P2. Causal ordering ensures that P2 receives m1 before m2.

**Why is causal ordering required?**
- To preserve happening-before relationship between events. If event x happens before event y, then y's effect should be visible to all processes only after x's effect is visible.
- To make distributed programs deterministic and avoid anomalies. Without causal ordering, processes may receive messages in different orders leading to inconsistent states.

**How is causal ordering achieved?**
- Through Lamport timestamps: Each message is stamped with a logical timestamp. The receiver delivers messages in increasing timestamp order. The timestamp of a message is greater than timestamps of all messages that causally preceded it.
- Through FIFO ordering: If processes only send messages to neighbors and messages are delivered to neighbors in FIFO order, then causal ordering is preserved.

**Advantages:**
- Ensures correctness and consistency of distributed programs.
- Preserves happens-before relationship between events.

**Disadvantages:**
- May reduce performance due to delay in delivery of messages. Messages may have to be buffered to maintain ordering.
- Complex to implement. Tracking and comparing causal dependencies between messages adds overhead.

**Applications:** Database systems, distributed shared memory systems.

**Mnemonics:**
Cause before effect.
Messages in, delivered in.