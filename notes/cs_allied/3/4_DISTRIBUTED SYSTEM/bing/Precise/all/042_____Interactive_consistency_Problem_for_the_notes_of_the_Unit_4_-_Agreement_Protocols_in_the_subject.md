# Interactive Consistency Problem

The interactive consistency problem is a fundamental problem in computer science and distributed systems. It was introduced by Pease, Shostak, and Lamport. The goal of distributed consensus is to reach an agreement in a distributed system in the presence of faults.

In the interactive consistency problem, every processor broadcasts its initial value to all other processors. The initial values of the processors may be different. A protocol for the interactive consistency problem should meet the following conditions:

1. **Agreement**: All non-faulty processors agree on the same vector (V1, V2, …, Vn).
2. **Validity**: If the ith processor is non-faulty and the initial value is Vi, then the ith value to be agreed on by all non-faulty processors must be Vi.

This problem is also known as the Byzantine Agreement Problem, where there are a total of n processes, at most m of which can be faulty. The communication medium is reliable and fully connected, and the receiver always knows the identity of the sender of a message. The system is synchronous, where in each round, a process receives messages, performs computation, and sends messages.