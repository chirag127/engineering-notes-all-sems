### Deadlock Characterization

A deadlock is a situation in which a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process  . Deadlocks prevent processes from completing their execution and waste system resources. 

There are four necessary conditions for a deadlock to occur    :

- **Mutual exclusion**: The resources involved are non-sharable, meaning that only one process can use a resource at a time.
- **Hold and wait**: The processes involved are holding at least one resource and waiting for another resource that is held by some other process.
- **No preemption**: The resources involved cannot be forcibly taken away from the processes that are holding them.
- **Circular wait**: The processes involved form a circular chain of waiting, meaning that each process is waiting for a resource that is held by the next process in the chain.

These four conditions are also known as the **Coffman conditions**, named after the researchers who first identified them  .

To deal with the deadlock problem, there are four possible methods :

- **Deadlock prevention**: Ensure that at least one of the four necessary conditions does not hold by imposing some constraints on how processes can request and use resources.
- **Deadlock avoidance**: Allow the four necessary conditions to hold, but use some information about the processes and resources to avoid allocating resources in a way that could lead to a deadlock.
- **Deadlock detection**: Allow the four necessary conditions to hold and the deadlock to occur, but use some mechanism to detect the deadlock and recover from it.
- **Deadlock ignorance**: Do nothing to prevent, avoid, or detect deadlocks, and assume that they will not occur or that they are not a serious problem. This is the approach used by some operating systems, such as Windows and Linux.