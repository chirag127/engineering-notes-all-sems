# Deadlock

A deadlock is a situation in which one or more processes are unable to proceed because they are waiting for some resources that are held by other processes. Deadlock can occur in operating systems that allow multiple processes to share resources such as CPU, memory, disk, printer, etc. Deadlock can cause performance degradation, system failure, or user frustration.

## Necessary Conditions for Deadlock

According to , there are four necessary conditions for deadlock to occur in a system:

- **Mutual exclusion**: The resources involved are non-sharable, meaning that only one process can use a resource at a time.
- **Hold and wait**: The processes involved are holding some resources while waiting for other resources that are held by other processes.
- **No preemption**: The resources involved cannot be forcibly taken away from the processes that are holding them.
- **Circular wait**: The processes involved form a circular chain of waiting, meaning that each process is waiting for a resource that is held by the next process in the chain.

## Methods for Handling Deadlock

According to  and , there are three main methods for handling deadlock in operating systems:

- **Deadlock prevention**: This method aims to ensure that at least one of the necessary conditions for deadlock is never satisfied. For example, by imposing a strict order on resource allocation, circular wait can be prevented. However, this method may impose some restrictions on resource utilization and process behavior.
- **Deadlock avoidance**: This method requires the operating system to have some information about the resource requirements and the current state of the system. Based on this information, the operating system can make safe decisions on resource allocation, meaning that it can avoid allocating resources that may lead to deadlock. However, this method may incur some overhead in maintaining and updating the information.
- **Deadlock detection and recovery**: This method allows deadlock to occur, but periodically checks the system for the presence of deadlock. If deadlock is detected, the operating system can take some actions to recover from it, such as terminating or rolling back some processes, or preempting some resources. However, this method may involve some cost in detecting and resolving deadlock.

## References

: Deadlock Prevention in Operating System (OS) - Scaler Topics. (2022, February 15). https://www.scaler.com/topics/operating-system/deadlock-prevention-in-operating-system/

: Deadlock in Operating System: What is, Circular Wait (Examples) - Guru99. (2023, January 31). https://www.guru99.com/deadlock-in-operating-system.html

: Deadlock in OS | Scaler Topics. (2022, February 23). https://www.scaler.com/topics/operating-system/deadlock-in-os/