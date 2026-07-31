### Interactive Consistency Problem

Interactive consistency, also known as distributed consensus, is a fundamental problem in computer science. The goal of distributed consensus is to reach an agreement in a distributed system in the presence of faults. This problem was introduced by Pease, Shostak, and Lamport.

A protocol for the interactive consistency problem should meet the following conditions:
- **Agreement**: All non-faulty processors agree on the same vector (V1, V2, …, Vn).
- **Validity**: If the ith processor is non-faulty and the initial value is Vi, then the ith value to be agreed on by all non-faulty processors must be Vi.

In the interactive consistency problem, every processor broadcasts its initial value to all other processors. The initial values of the processors may be different.

This problem is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a result.