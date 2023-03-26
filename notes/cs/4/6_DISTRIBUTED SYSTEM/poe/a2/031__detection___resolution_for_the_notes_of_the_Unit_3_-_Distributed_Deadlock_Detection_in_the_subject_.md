 Here is the content in markdown format without any emojis or external links, in a formal tone:

### Detection & Resolution for Distributed Deadlock

1. Detection
- Centralized: Have a central coordinator that maintains global information about resource allocation and detects deadlocks.
- Distributed: Each process keeps track of resources it has acquired and resources it is waiting for. If it detects a deadlock, it informs the central coordinator.

2. Resolution
- Prevention: Never allow a set of processes to enter a deadlock state. For example, impose a total ordering on resource requests and grant resources in that order.
- Avoidance: Allow processes to request resources, but use an algorithm to determine if granting a request might lead to a deadlock. If so, the request is denied.
- Recovery: Allow deadlocks to occur, but have recovery routines that can roll back and undo the effects of processes that have allocated resources and synchronize the state of resources that were not allocated.

The key points to keep in mind are:

- The distributed nature of the system makes deadlock detection more challenging than in centralized systems. Global information is difficult to obtain.
- Resolution techniques like avoidance and recovery may introduce significant overhead. Tradeoffs must be made between performance and deadlock handling.
- The distributed and asynchronous nature of the system can make it difficult to correctly resolve deadlocks. Care must be taken to avoid races and other concurrency-related problems in the resolution algorithms and code.