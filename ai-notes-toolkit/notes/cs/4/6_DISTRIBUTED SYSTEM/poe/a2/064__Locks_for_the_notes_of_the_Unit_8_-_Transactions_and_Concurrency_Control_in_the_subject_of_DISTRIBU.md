 Here is the markdown content for the given topic:

### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

1. Locks are mechanisms used to restrict access to resources in a system to avoid inconsistent reads and writes.
2. Two main types of locks:
 - Exclusive lock: Only one process can obtain an exclusive lock on a resource at a time. Other processes requesting the lock are blocked until it is released. Used to protect critical sections of code that should not be executed by multiple processes simultaneously.
 - Shared lock: Multiple processes can obtain a shared lock on a resource simultaneously as long as no process holds an exclusive lock on the resource. Used to control read access to shared resources.
3. Deadlock: A set of processes are blocked indefinitely, waiting for each other to release locks. Can be avoided by:
 - Requiring processes to request locks in a fixed order
 - Releasing all locks held by a process when it requests a new lock
4. Two-phase locking: A protocol that prevents deadlock by requiring that processes obtain all the locks they need in a fixed order before entering the critical section. Releases all locks when the critical section completes. Ensures that no deadlocks via lock requests can occur.
5. Optimistic concurrency control: Allows processes to access data resources without acquiring locks,validating that no other process has modified the data before committing updates. If another process has updated the data, the validating process rolls back and retries. Avoids blocking but may result in wasted work if conflicts are common.