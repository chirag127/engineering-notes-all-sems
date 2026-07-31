### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Lamport’s Logical Clock** was created by Leslie Lamport. It provides a basis for the more advanced Vector Clock Algorithm .
- Due to the absence of a Global Clock in a Distributed Operating System, Lamport Logical Clock is needed .
- Logical clocks are based on capturing chronological and causal relationships of processes and ordering events .
- The idea behind Lamport clocks is to disregard physical time and capture just a “happens-before” relationship between a pair of events .
- **Vector Clocks** extend the capabilities of Lamport Clocks to allow us to understand the ordering across multiple processes which cross communicate .
- They can also be invaluable in understanding the flow of messages in a distributed system .
- As a data level, Vector clocks are vectors of event counters .