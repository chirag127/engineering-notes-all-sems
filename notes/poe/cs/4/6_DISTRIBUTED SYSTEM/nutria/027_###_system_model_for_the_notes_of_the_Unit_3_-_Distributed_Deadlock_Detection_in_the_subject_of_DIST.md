
### System Model for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of DISTRIBUTED SYSTEM

* Distributed deadlock detection is the process of detecting deadlocks in distributed systems. 
* A distributed system is a collection of autonomous computers that communicate with each other to achieve a common goal.
* In a distributed system, a deadlock is a situation in which two or more processes are waiting for each other to finish their respective tasks before they can continue. 
* In other words, each process is waiting for a resource held by another process, which in turn is waiting for a resource held by the first process. 
* This creates an impasse, where no process can progress until the resources are released by the other processes.
* Deadlock detection algorithms are used to identify deadlocks in distributed systems. 
* These algorithms can be classified into two categories: centralized and distributed. 
* Centralized algorithms rely on a single node, or coordinator, to detect deadlocks. 
* On the other hand, distributed algorithms rely on communication among the nodes of the distributed system to detect deadlocks.
* An example of a distributed deadlock detection algorithm is the Chandy-Misra-Haas algorithm. 
* This algorithm uses a graph-based approach to identify deadlocks. 
* It works by constructing a directed graph with the processes as nodes and the resources they are waiting for as edges. 
* A cycle in the graph indicates a deadlock. 
* The algorithm also uses a distributed algorithm to propagate information about the resources held by each process. 
* This allows the algorithm to detect deadlocks more quickly.
* Mnemonics and learning tricks for distributed deadlock detection include:
  * **D**etect **D**eadlocks by **D**rawing **D**irected **G**raphs with **P**rocesses as **N**odes and **R**esources as **E**dges.
  * **C**heck for **C**ycles to **I**dentify **D**eadlocks with the **H**andy-**M**isra-**H**aas **A**lgorithm.