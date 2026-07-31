### Deadlock Characterization

Deadlock is a situation in a computer system where two or more processes are unable to proceed because they are waiting for each other to release resources. Deadlock can occur in a system when the following four conditions are met simultaneously:

1. **Mutual Exclusion**: A resource can only be used by one process at a time.
2. **Hold and Wait**: A process can hold resources while waiting for other resources to be released.
3. **No Preemption**: Resources cannot be forcibly taken away from a process that is currently holding them.
4. **Circular Wait**: A circular chain of processes exists, where each process is waiting for a resource held by the next process in the chain.

These four conditions are known as the Coffman conditions, after the researchers who first described them. In order to prevent deadlock, at least one of these conditions must be negated. This can be done through various deadlock prevention or avoidance techniques, such as resource allocation algorithms or process scheduling policies.

In the context of CPU scheduling, deadlock can occur when processes are competing for access to the CPU or other system resources. Deadlock prevention and avoidance techniques can be used to ensure that processes are able to access the resources they need without causing a deadlock situation. These techniques can include the use of priority scheduling, preemption, or resource allocation algorithms.