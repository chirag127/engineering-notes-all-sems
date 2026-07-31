### Interactive Consistency Problem

- Interactive consistency was introduced by Pease, Shostak, and Lamport.
- Distributed consensus is a fundamental problem in computer science.
- The goal of distributed consensus is to reach an agreement in a distributed system in the presence of faults.
- A protocol for the interactive consistency problem should meet the following conditions:
    - Agreement: All non-faulty processors agree on the same vector (V1, V2, …, Vn).
    - Validity: If the ith processor is non-faulty and the initial value is Vi, then the ith value to be agreed on by all non-faulty processors must be Vi.
- Interactive consistency is the problem in which n nodes, where up to t may be Byzantine, each with its own private value, run an algorithm that allows all non-faulty nodes to infer the values of each other node.
- This problem is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a solution.