### Deadlock

- A deadlock is a situation in which one or more processes are blocked indefinitely because they are waiting for resources that are held by other processes.
- Deadlocks can occur in operating systems that allow multiple processes to share resources such as memory, files, devices, etc.
- Deadlocks can cause performance degradation, system failure, or data loss.
- Deadlocks can be prevented, avoided, detected, or resolved by using different techniques and algorithms.

#### Necessary Conditions for Deadlock

- According to , there are four necessary conditions for a deadlock to occur in a system:

  - **Mutual exclusion**: The resources involved are non-sharable, meaning that only one process can use a resource at a time.
  - **Hold and wait**: The processes involved are holding some resources and waiting for other resources that are held by other processes.
  - **No preemption**: The resources involved cannot be forcibly taken away from the processes that are holding them.
  - **Circular wait**: The processes involved form a circular chain of waiting, meaning that each process is waiting for a resource that is held by the next process in the chain.

- These conditions are necessary but not sufficient, meaning that they must hold for a deadlock to occur, but they do not guarantee that a deadlock will occur.

#### Methods for Handling Deadlock

- According to  and , there are four main methods for handling deadlock in an operating system:

  - **Deadlock prevention**: This method ensures that at least one of the necessary conditions for deadlock does not hold in the system, thus preventing deadlock from occurring. For example, this can be done by imposing constraints on resource allocation, such as limiting the number of resources that a process can request or hold, or requiring a process to request all the resources it needs at once.
  - **Deadlock avoidance**: This method allows the system to dynamically allocate resources to processes, but only if doing so does not lead to a potential deadlock situation. For example, this can be done by using an algorithm that tracks the current and future resource requests and availability, such as the Banker's algorithm, and denies requests that could result in deadlock.
  - **Deadlock detection**: This method allows the system to detect deadlock after it has occurred, and then take some action to resolve it. For example, this can be done by using an algorithm that periodically checks for cycles in the resource allocation graph, such as the Wait-for graph algorithm, and then terminates or restarts some of the processes involved in the deadlock.
  - **Deadlock recovery**: This method is used in conjunction with deadlock detection, and specifies what action to take to resolve the deadlock. For example, this can be done by using one or more of the following strategies: aborting all or some of the processes involved in the deadlock, preempting some of the resources held by the processes involved in the deadlock, or rolling back the processes involved in the deadlock to a previous state.

#### References

: Deadlock Prevention in Operating System (OS) - Scaler Topics. (2022, February 15). https://www.scaler.com/topics/operating-system/deadlock-prevention-in-operating-system/

: Deadlock in Operating System: What is, Circular Wait (Examples) - Guru99. (2023, January 31). https://www.guru99.com/deadlock-in-operating-system.html

: Deadlock in OS | Scaler Topics. (2022, February 23). https://www.scaler.com/topics/operating-system/deadlock-in-os/

: Introduction of Deadlock in Operating System - GeeksforGeeks. (n.d.). https://www.geeksforgeeks.org/introduction-of-deadlock-in-operating-system/

: Deadlock - Wikipedia. (n.d.). https://en.wikipedia.org/wiki/Deadlock