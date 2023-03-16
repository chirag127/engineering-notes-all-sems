### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in distributed systems, where a set of processors need to agree on a common value, even if some of them are faulty or malicious.
- The problem is named after the Byzantine Generals Problem, which is a metaphor for the situation where several generals of the Byzantine army need to coordinate their attack or retreat plan, but some of them may be traitors who send conflicting messages  .
- A solution to the Byzantine agreement problem requires that the following properties are satisfied :
  - **Termination**: Every non-faulty processor eventually decides on a value.
  - **Agreement**: All non-faulty processors decide on the same value.
  - **Validity**: If all non-faulty processors start with the same value, then they decide on that value.
- A necessary condition for solving the Byzantine agreement problem is that the number of faulty processors is less than one-third of the total number of processors .
- A possible solution to the Byzantine agreement problem is the **EAC protocol** proposed by El-Attar and Chen, which works as follows:
  - Each processor broadcasts its initial value to all other processors.
  - Each processor collects the values received from all other processors and forms a vector of values, sorted in ascending order.
  - Each processor computes the median of the vector and broadcasts it to all other processors.
  - Each processor collects the medians received from all other processors and forms another vector of medians, sorted in ascending order.
  - Each processor computes the median of the second vector and decides on that value.
- The EAC protocol satisfies the termination, agreement and validity properties, and can tolerate up to (n-1)/3 faulty processors, where n is the total number of processors.
- The EAC protocol has a message complexity of O(n^2) and a time complexity of O(1), where n is the total number of processors.