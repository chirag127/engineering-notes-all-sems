 Here is the content in markdown format for the topic ### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM:

### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- **Majority voting**: Each process votes for a correct value based on the inputs it receives. The value that receives a majority of votes is chosen as the final output. For example, if there are 5 processes, the value chosen by at least 3 processes is selected. This works well if the probability of faulty processes is less than 50%.
- **Weighted majority voting**: Each process is assigned a weight based on its reliability. The value which achieves a weighted majority is selected as the final output. This is useful if processes have different failure probabilities. The processes with higher reliability are given higher weights.
- **Triple modular redundancy (TMR)**: The system consists of 3 modules running the same algorithm on the same input and the outputs are compared using majority voting. If 2 out of 3 modules agree, then their decision is accepted. This can tolerate only 1 faulty module and improves reliability.
- **N-modular redundancy (NMR)**: The system consists of N modules and uses a majority voting scheme. This can tolerate up to (N-1)/2 faulty modules but the cost and complexity also increase with N.

Some advantages of voting protocols are simplicity, low resource overhead and ability to mask faults. Disadvantages are they do not work if there are too many faulty processes and performance can degrade if a large number of computations need to be performed to reach agreement.

Voting protocols are useful in applications where high reliability is required such as aircraft control systems, nuclear reactor control, etc. They can be combined with other techniques like replication and time-outs to further improve fault tolerance.