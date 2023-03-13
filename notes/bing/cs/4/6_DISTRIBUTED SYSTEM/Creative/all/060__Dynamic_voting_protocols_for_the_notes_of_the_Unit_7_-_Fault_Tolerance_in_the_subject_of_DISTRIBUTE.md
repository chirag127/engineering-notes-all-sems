### Dynamic voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Dynamic voting protocols are a technique for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A replicated file consists of multiple copies of the same file stored at different sites in the system  .
- A dynamic voting protocol assigns a weight to each copy of a replicated file and requires a quorum of weights to access or update the file  .
- A quorum is a subset of sites that collectively have enough votes to perform an operation on the file.
- The weights and quorums are dynamically adjusted based on the availability and connectivity of the sites  .
- A dynamic voting protocol ensures that any two quorums have at least one site in common, which guarantees mutual exclusion and consistency of the file  .
- A dynamic voting protocol also ensures that there is always at least one quorum available, which guarantees availability of the file  .
- A dynamic voting protocol can be implemented using a coordinator site that maintains the weights and quorums of the replicated file and grants or denies requests from other sites  .
- Alternatively, a dynamic voting protocol can be implemented using a distributed algorithm that allows the sites to communicate and agree on the weights and quorums of the replicated file without a coordinator.

#### Advantages of dynamic voting protocols

- Dynamic voting protocols can improve the availability and performance of replicated files by adapting to the changing conditions of the distributed system  .
- Dynamic voting protocols can reduce the communication and synchronization overhead of accessing and updating replicated files by minimizing the number of sites involved in a quorum  .
- Dynamic voting protocols can tolerate site failures and network partitions by allowing the surviving and connected sites to form a quorum and access or update the file  .

#### Disadvantages of dynamic voting protocols

- Dynamic voting protocols can increase the complexity and cost of maintaining the consistency and recovery of replicated files by requiring the dynamic adjustment of weights and quorums  .
- Dynamic voting protocols can introduce the possibility of deadlocks and livelocks when multiple sites request to access or update the same file concurrently  .
- Dynamic voting protocols can suffer from performance degradation and unavailability when the coordinator site fails or becomes isolated from the rest of the system  .

#### Example of a dynamic voting protocol

- Suppose there are four sites A, B, C, and D that store copies of a replicated file F  .
- Initially, each site has a weight of 1 and the quorum requirement is 2  .
- This means that any two sites can form a quorum and access or update F  .
- If site A fails, the coordinator site (say B) can detect the failure and reduce the quorum requirement to 1  .
- This means that any surviving site can form a quorum and access or update F  .
- If site A recovers, the coordinator site can detect the recovery and increase the quorum requirement to 2  .
- This means that any two sites can form a quorum and access or update F  .
- If site B and C become disconnected from site A and D, the coordinator site can detect the partition and assign different weights and quorums to the two subnetworks [^