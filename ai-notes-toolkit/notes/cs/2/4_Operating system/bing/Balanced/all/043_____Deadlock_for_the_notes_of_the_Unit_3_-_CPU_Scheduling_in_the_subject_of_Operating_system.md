# Deadlock

A deadlock is a situation in which one or more processes are blocked indefinitely because they are waiting for resources that are held by other processes. Deadlock can occur in a multiprogramming system when processes compete for a finite number of resources, such as CPU, memory, disk, printer, etc. Deadlock can also occur in a distributed system when processes communicate and synchronize with each other over a network.

## Conditions for Deadlock

According to , there are four necessary conditions for deadlock to occur in a system:

- **Mutual exclusion**: The resources involved are non-sharable, meaning that only one process can use a resource at a time. If another process requests that resource, it has to wait until the resource is released.
- **Hold and wait**: The processes involved are holding at least one resource and waiting for another resource that is held by some other process.
- **No preemption**: The resources involved cannot be forcibly taken away from the processes that are holding them. The processes have to voluntarily release the resources when they are done with them.
- **Circular wait**: The processes involved are waiting for resources in a circular chain, meaning that each process is waiting for a resource that is held by the next process in the chain. There is no way to break the cycle of waiting.

## Methods for Handling Deadlock

According to , there are three main methods for handling deadlock in a system:

- **Deadlock prevention**: This method aims to prevent deadlock from occurring by ensuring that at least one of the four necessary conditions is not satisfied. For example, the system can enforce a strict order of resource allocation, or limit the number of resources that a process can request, or allow preemption of resources under certain circumstances.
- **Deadlock avoidance**: This method assumes that deadlock may occur, but tries to avoid it by carefully allocating resources to processes. For example, the system can use an algorithm such as Banker's algorithm to determine if a resource request is safe or unsafe, and grant or deny the request accordingly. The system can also keep track of the resource allocation state and the resource requests of each process, and avoid entering a deadlock state.
- **Deadlock detection and recovery**: This method allows deadlock to occur, but tries to detect and recover from it. For example, the system can periodically run a deadlock detection algorithm, such as a resource allocation graph algorithm, to check if there is a cycle of waiting processes in the system. If a deadlock is detected, the system can use a recovery strategy, such as aborting or rolling back some processes, or preempting some resources, to break the deadlock.