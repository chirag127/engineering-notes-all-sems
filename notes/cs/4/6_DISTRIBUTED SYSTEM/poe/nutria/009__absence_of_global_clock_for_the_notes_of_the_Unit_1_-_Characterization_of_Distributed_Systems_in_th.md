
### Absence of Global Clock

* Distributed systems lack a single, global clock that all nodes can access. 
* This means that nodes must use their own local clocks to coordinate their activities. 
* This can lead to issues such as clock drift, where the time on one node is slightly different from the time on another node. 
* Clock synchronization algorithms are used to mitigate this issue by allowing nodes to adjust their local clocks so that they are more closely aligned. 
* Without a global clock, distributed systems must rely on other techniques to coordinate activities, such as message passing, shared memory, and distributed transactions.